// MCP stdio handshake harness for code-review-graph (home replication evidence).
// Spawns the exact production command/env and proves initialize + tools/list +
// prompts/list + resources/list, checking the 5 excluded mutating tools are absent.
import { spawn } from "node:child_process";

const ALLOWLIST = [
  "get_minimal_context_tool",
  "list_graph_stats_tool",
  "detect_changes_tool",
  "get_review_context_tool",
  "get_impact_radius_tool",
  "get_affected_flows_tool",
  "query_graph_tool",
  "semantic_search_nodes_tool",
  "get_architecture_overview_tool",
  "list_communities_tool",
  "get_community_tool",
  "list_flows_tool",
  "get_flow_tool",
  "get_hub_nodes_tool",
  "get_bridge_nodes_tool",
  "get_surprising_connections_tool",
  "get_knowledge_gaps_tool",
  "get_suggested_questions_tool",
  "find_large_functions_tool",
  "traverse_graph_tool",
  "get_docs_section_tool",
  "get_wiki_page_tool",
  "list_repos_tool",
  "cross_repo_search_tool",
  "refactor_tool",
];

const EXCLUDED = [
  "apply_refactor_tool",
  "build_or_update_graph_tool",
  "embed_graph_tool",
  "generate_wiki_tool",
  "run_postprocess_tool",
];

const child = spawn("code-review-graph", ["serve", "--tools", ALLOWLIST.join(",")], {
  env: {
    ...process.env,
    HF_HUB_OFFLINE: "1",
    TRANSFORMERS_OFFLINE: "1",
  },
  stdio: ["pipe", "pipe", "pipe"],
  shell: false,
});

let nextId = 1;
const pending = new Map();
const stderrTail = [];
const stdoutTail = [];

function send(method, params = {}) {
  const id = nextId++;
  const msg = { jsonrpc: "2.0", id, method, params };
  child.stdin.write(JSON.stringify(msg) + "\n");
  return new Promise((resolve, reject) => {
    pending.set(id, { resolve, reject });
    setTimeout(() => {
      if (pending.has(id)) {
        pending.delete(id);
        reject(new Error(`timeout waiting ${method}`));
      }
    }, 60000);
  });
}

child.stdout.on("data", (chunk) => {
  const text = chunk.toString();
  stdoutTail.push(text);
  if (stdoutTail.length > 30) stdoutTail.shift();
  for (const line of text.split("\n")) {
    if (!line.trim()) continue;
    let msg;
    try {
      msg = JSON.parse(line);
    } catch {
      continue;
    }
    if (msg.id && pending.has(msg.id)) {
      const { resolve } = pending.get(msg.id);
      pending.delete(msg.id);
      resolve(msg);
    }
  }
});

child.stderr.on("data", (chunk) => {
  const text = chunk.toString();
  stderrTail.push(text);
  if (stderrTail.length > 20) stderrTail.shift();
});

child.on("exit", (code, signal) => {
  for (const { reject } of pending.values()) {
    reject(new Error(`server exited code=${code} signal=${signal}`));
  }
});

try {
  const init = await send("initialize", {
    protocolVersion: "2024-11-05",
    capabilities: {},
    clientInfo: { name: "crg-home-replication-handshake", version: "1.0.0" },
  });
  child.stdin.write(
    JSON.stringify({ jsonrpc: "2.0", method: "notifications/initialized" }) + "\n",
  );

  const tools = await send("tools/list");
  const prompts = await send("prompts/list");
  const resources = await send("resources/list");

  const toolNames = (tools.result?.tools ?? []).map((t) => t.name).sort();
  const promptNames = (prompts.result?.prompts ?? []).map((p) => p.name);
  const resourceCount = (resources.result?.resources ?? []).length;
  const excludedPresent = EXCLUDED.filter((name) => toolNames.includes(name));
  const missingAllowlist = ALLOWLIST.filter((name) => !toolNames.includes(name));

  const summary = {
    server: "code-review-graph",
    initialize_ok: !!init.result?.serverInfo,
    server_info: init.result?.serverInfo ?? null,
    tools: toolNames.length,
    prompts: promptNames.length,
    resources: resourceCount,
    missing_from_allowlist: missingAllowlist,
    excluded_present: excludedPresent,
    tool_names: toolNames,
  };
  console.log(JSON.stringify(summary, null, 2));

  const okParts = {
    initialize_ok: summary.initialize_ok,
    tools_match_allowlist: toolNames.length === ALLOWLIST.length,
    no_missing: missingAllowlist.length === 0,
    no_excluded: excludedPresent.length === 0,
    resources_zero: resourceCount === 0,
  };
  const ok =
    Object.values(okParts).every(Boolean);
  console.log("OK_PARTS: " + JSON.stringify(okParts));
  if (!ok) {
    console.error("STDERR TAIL:", stderrTail.join("").slice(-2000));
    process.exit(1);
  }
  child.kill();
  process.exit(0);
} catch (err) {
  console.error("HANDSHAKE FAILED:", err.message);
  console.error("STDERR TAIL:", stderrTail.join("").slice(-2000));
  child.kill();
  process.exit(1);
}

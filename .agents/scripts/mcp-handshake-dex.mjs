// MCP stdio handshake harness for dex_ppirtv (PPI-Install audit evidence).
// Spawns the launcher with the workspace passed explicitly (audit smoke) and
// proves initialize + tools/list against the required PPIRTV toolset.
import { spawn } from "node:child_process";
import path from "node:path";

const REQUIRED_TOOLS = [
  "spt_validate",
  "goal_start",
  "goal_status",
  "ppirtv_checkout",
  "goal_gate_check",
  "goal_meeting_open",
  "goal_meeting_add_turn",
  "goal_meeting_close",
  "evidence_add",
  "mm_memory_mining",
  "goal_regress",
  "goal_verdict",
  "flow_archive",
  "ppirtv_trace",
];

const workspace = process.argv[2] ?? "C:\\CodexProjetos\\code-review-graph";
const userProfile = process.env.USERPROFILE;
if (!userProfile) {
  console.error("USERPROFILE not set");
  process.exit(1);
}
const principlesPath = path.join(
  userProfile,
  ".agents",
  "memories",
  "principles",
  "operational-contract.json",
);
const graphifyCommand = path.join(
  userProfile,
  "AppData",
  "Roaming",
  "Python",
  "Python314",
  "Scripts",
  "graphify.exe",
);

const child = spawn(
  "C:\\Program Files\\nodejs\\node.exe",
  ["C:\\CodexProjetos\\dex-PPIRTV\\dist\\launcher.js", "--workspace", workspace],
  {
    cwd: "C:\\CodexProjetos\\dex-PPIRTV",
    env: {
      ...process.env,
      PPIRTV_WORKSPACE_ROOT: "C:\\CodexProjetos",
      PPIRTV_PRINCIPLES_PATH: principlesPath,
      PPIRTV_GRAPHIFY_RECALL: "1",
      PPIRTV_GRAPHIFY_COMMAND: graphifyCommand,
      PPIRTV_GRAPHIFY_GRAPH_PATH: "C:\\CodexProjetos\\book-to-skill\\graphify-out\\graph.json",
      PPIRTV_GRAPHIFY_TIMEOUT_MS: "5000",
    },
    stdio: ["pipe", "pipe", "pipe"],
    shell: false,
  },
);

let nextId = 1;
const pending = new Map();
const stderrTail = [];

function send(method, params = {}) {
  const id = nextId++;
  child.stdin.write(JSON.stringify({ jsonrpc: "2.0", id, method, params }) + "\n");
  return new Promise((resolve, reject) => {
    pending.set(id, { resolve, reject });
    setTimeout(() => {
      if (pending.has(id)) {
        pending.delete(id);
        reject(new Error(`timeout waiting ${method}`));
      }
    }, 90000);
  });
}

child.stdout.on("data", (chunk) => {
  for (const line of chunk.toString().split("\n")) {
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
  stderrTail.push(chunk.toString());
  if (stderrTail.length > 40) stderrTail.shift();
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
    clientInfo: { name: "ppi-install-audit-handshake", version: "1.0.0" },
  });
  child.stdin.write(
    JSON.stringify({ jsonrpc: "2.0", method: "notifications/initialized" }) + "\n",
  );
  const tools = await send("tools/list");
  const prompts = await send("prompts/list");
  const resources = await send("resources/list");

  const toolNames = (tools.result?.tools ?? []).map((t) => t.name).sort();
  const missing = REQUIRED_TOOLS.filter((name) => !toolNames.includes(name));
  const summary = {
    server: "dex_ppirtv",
    workspace,
    initialize_ok: !!init.result?.serverInfo,
    server_info: init.result?.serverInfo ?? null,
    tools: toolNames.length,
    prompts: (prompts.result?.prompts ?? []).length,
    resources: (resources.result?.resources ?? []).length,
    required_tools_present: REQUIRED_TOOLS.length - missing.length,
    missing_required: missing,
    tool_names: toolNames,
  };
  console.log(JSON.stringify(summary, null, 2));
  if (!summary.initialize_ok || missing.length > 0) {
    console.error("STDERR TAIL:", stderrTail.join("").slice(-3000));
    process.exit(1);
  }
  child.kill();
  process.exit(0);
} catch (err) {
  console.error("HANDSHAKE FAILED:", err.message);
  console.error("STDERR TAIL:", stderrTail.join("").slice(-3000));
  child.kill();
  process.exit(1);
}

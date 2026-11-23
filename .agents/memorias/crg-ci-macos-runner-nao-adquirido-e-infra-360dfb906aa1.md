---
implementation_version: v2
layer: L2
slug: crg-ci-macos-runner-nao-adquirido-e-infra-360dfb906aa1
tags:
  - "#auto-memory/reference"
---

# crg-ci-macos-runner-nao-adquirido-e-infra

Espelho da auto-memory do host ZCode (arquivo crg-ci-macos-runner-nao-adquirido-e-infra.md, tipo reference).

CI do CRG com job `E2E MCP client (macos-latest)` cancelado depois

No CI do fork do CRG, um run vermelho só em `E2E MCP client (macos-latest)` pode ser falta de runner, não defeito. Medido em 2026-11-23 nos runs 45269249594 e 45269542345 (commits `0ec8978d` e `844c4744`): o job ficou 17 minutos e meio na fila e foi cancelado; nos runs verdes do mesmo dia ele leva 2 minutos.

**Como diagnosticar antes de mexer em código:**

```
gh api repos/dex-agent/dex-code-review-graph/check-runs/<id-do-job>/annotations
gh run view <run> -R dex-agent/dex-code-review-graph --json jobs --jq '.jobs[] | select(.name | startswith("E2E MCP client"))'
```

- Causa de infra quando as anotações dizem `The job was not acquired by Runner of type hosted even after multiple attempts` e `Due to capacity constraints, jobs targeting macOS arm64 runners may experience longer queue times`.
- Confirmar que os irmãos `E2E MCP client (ubuntu-latest)` e `(windows-latest)` do mesmo run passaram.
- O job aparece como `cancelled`, sem runner, sem passos e sem log (`gh run view --job --log` sai vazio; a API de logs devolve `BlobNotFound`). Não adianta procurar falha de teste.

**Cura:** `gh run rerun <run> --failed -R dex-agent/dex-code-review-graph` no commit mais recente e vigia (`chama-o-vigia`) no mesmo número de run; o attempt passa a 2. Run de commit já superado não se re-roda: o HEAD é que precisa ficar verde. Provado em 2026-11-23: a segunda tentativa do run 45269542345 passou com os 21 jobs verdes e o job macOS em 3 minutos e 38 segundos, mesmo código que tinha ficado 17 minutos na fila.

**Limite:** o job não é check obrigatório (comentário no `ci.yml`), mas o vermelho aparece na main. Se o re-run falhar pela mesma anotação, é capacidade do GitHub: declarar como infra pendente e repetir mais tarde, sem "consertar" teste.

Relaciona: [[crg-cura-ci-8-classes-20261119]], [[crg-pr6-effect-fn-revisao-20261123]].

#auto-memory/reference

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^crg-ci-macos-runner-nao-adquirido-e-infra-360dfb906aa1-content

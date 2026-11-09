---
fotografia_id: 20261108-crg-test-path
revision: 3fb1ab318f9c92f5bbb5d1d7f9b4462a24a5ff04
observed_at: 2026-11-08
---

# Decisões do corte de classificação por caminho

- **D-01** O mantenedor delimitou as convenções de diretório a componentes do caminho relativo ao checkout. O bead `crg-08x` registra os dois falsos positivos de origem. O [RED](../receipts/crg-test-path/red.json) acrescenta a raiz Jest e os padrões vizinhos.
- **D-02** A identidade nativa continua gravada no grafo. O parser comum e o enriquecimento Jedi recebem a raiz que o chamador já conhecia. A [prova A/B](../receipts/crg-test-path/cli.json) verifica arestas exatas e `indirect=false` para os controles positivos.
- **D-03** A seleção nativa da CI ganhou os casos de fronteira. A [prova focada](../receipts/crg-test-path/green.json) registra os seletores e o resultado. O [Trilho](../PLAN-TASKS/2026-11-08-crg-test-path.md) documenta o verdict.
- **D-04** O mantenedor trata a reclassificação de índices antigos no bead `crg-k4q`. A validade semântica de um índice já gravado precisa de prova própria.

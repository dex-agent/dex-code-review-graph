---
implementation_version: v2
layer: L2
slug: dex-audio-motor-contrato-novo-20261121-afec3eca0d8f
tags:
  - "#auto-memory/reference"
---

# dex-audio-motor-contrato-novo-20261121

Espelho da auto-memory do host ZCode (arquivo dex-audio-motor-contrato-novo-20261121.md, tipo reference).

CONTRATO NOVO do áudio da casa (2026-11-21): a rota viva é dex-audio-motor (motor.py enviar --uso dex-pai --texto-arquivo + --idempotency-key, recibo JSON com message_id); a ponte antiga ~/.dex-agent/.../send-dex-agent-audio-summary.ps1 está SUPERSEDED — chamar o .ps1 morre sem JSON (pago 2x sem recibo até ler o SKILL.md)

A skill `dex-audio` mudou de contrato (vista em 2026-11-21): a rota viva é a skill irmã **`dex-audio-motor`**; a ponte antiga `~/.dex-agent/skills/dex-agent-audio-summary/scripts/send-dex-agent-audio-summary.ps1` está **SUPERSEDED** — chamá-la abre PowerShell e termina sem JSON nenhum (2 envios pagos sem recibo até ler a fonte — regra: 2 erros = PARE E LEIA O SKILL.md).

**Contrato certo**:
```bash
python -B "$USERPROFILE/.agents/skills/dex-audio-motor/scripts/motor.py" enviar \
  --uso dex-pai --texto-arquivo <resumo.txt> --idempotency-key <chave>
```
- Saída JSON com `ok`, `message_id` (recibo Telegram), `chat_id`, `motor_efetivo`, `voz_efetiva`, `fallback_usado` — EXIGIR `message_id`.
- Erros tipados: exit 1 contato não resolvido; 2 entrada inválida; 3 skill irmã ausente; 4 falha TTS/envio.
- Conferir contato antes: `motor.py resolver --uso dex-pai` (destino canônico vem da skill `dex-contatos`, loja `~/.dex-contatos`).
- CLI completa: `enviar/resolver/motores/selftest`, tríade `--help/--schema/--usage`; suíte `tests/test_motor.py`.
- Dedupe por idempotency-key: repetir o mesmo comando devolve o recibo anterior sem novo envio (usar para CONFERIR entrega pendente, não para reenviar).

Modo áudio contínuo da burrinha (dono, reafirmado 2026-11-19): áudio apenas em avanço substancial/achado muito importante, tom gauchinha, texto normalizado, destino `--uso dex-pai`. Espelho napkin: `DEX-AUDIO-MOTOR-CONTRATO-NOVO` no napkin do CRG.

Relacionado: [[identidade-git-dex-agent-rewrite-20261121]]

#auto-memory/reference

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^dex-audio-motor-contrato-novo-20261121-afec3eca0d8f-content

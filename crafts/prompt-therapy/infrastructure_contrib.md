# prompt-therapy: System Infrastructure contribution (Rule-14 property 1)

The rows this craft adds to the one manifest; same seven cells as `dyad/infrastructure/INFRASTRUCTURE.md`.

| component | partition | version | purpose | license | replacement | profile |
|-----------|-----------|---------|---------|---------|-------------|---------|
| anthropic (Python SDK) | library | 2.8.0 pinned (`pip index versions anthropic`, 2026-11-15) | the Claude adapter behind the provider interface (`scripts/provider.py`, d-work #3); imported only when the adapter is built | MIT | another provider's SDK behind the same interface | operating |

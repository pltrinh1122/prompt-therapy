# prompt-therapy: instance System Infrastructure (Rule-14 property 1)

This system's own operating rows, as observed on the hosts that run them; joined to the core's and the crafts' rows as
one manifest. Same seven cells as `dyad/infrastructure/INFRASTRUCTURE.md`.

| component | partition | version | purpose | license | replacement | profile |
|-----------|-----------|---------|---------|---------|-------------|---------|
| Docker | library | observed on the operator's machine at the first run (d-work #3, H1) | the evaluation container of plan #3 revision 5: `workstation-corpus/ops/3-h1-provider-evaluation.sh` runs the adversarial set in `docker run --rm` of an image built from `python:3.12-slim` | Apache-2.0 (Docker Engine) | the bare-host run of plan #3 revision 4 (Python 3.12+ and git on the host) | operating |
| ant (Anthropic CLI) | library | observed on the operator's machine at the first run (d-work #3, H1) | the operator's sign-in to the Claude API and the short-lived token each evaluation run takes (`dmc:provider-auth`, outcome sign-in) | MIT | an API key in the operator's shell (`dmc:provider-auth`, its last outcome) | operating |

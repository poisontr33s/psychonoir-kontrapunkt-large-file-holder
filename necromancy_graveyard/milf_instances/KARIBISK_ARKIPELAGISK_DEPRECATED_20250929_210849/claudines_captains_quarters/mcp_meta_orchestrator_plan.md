# Meta‑MCP (Orchestrator) – gjennomføringsplan

Mål: orkestratoren blir eneste registrerte MCP, og ruter alle kall til «child MCPs» med navnerom og health‑checks.

## Milepæler

1. Klient/proxy
   - Legg til lett MCP‑klient som kan connecte til stdio‑child
   - Implementer `list_tools` proxy + caching (per child)
   - Implementer `call_tool` proxy (navnerom: `quantum/*`, `seq/*`, `repo/*`, `docs/*`, `md/*`, `sentry/*`)

2. Prosess‑livssyklus
   - Spawn via `Bun.spawn` med cwd og env
   - Backoff/retry og auto‑restart ved krasj
   - Strupet logging til stderr, stdout rent JSON‑RPC

3. Health‑checks
   - «/ping» ved `list_tools` + periodisk status
   - Diagnoseverktøyet utvides til å sjekke child‑prosesser

4. Miljø
   - `ffmpeg` på PATH (MarkItDown)
   - `CONTEXT7_API_KEY` og `SENTRY_AUTH_TOKEN` i miljø

5. Opprydding
   - Når proxy er stabil: fjern legacy `bun-quantum-mcp` fra `.vscode/mcp.json`
   - Valgfritt: la orchestrator bli eneste registrerte MCP

## Akseptansekriterier

- VS Code viser < 128 verktøy totalt
- `diagnose_environment` rapporterer ok for ffmpeg/uvx/tokens
- Enkle proxiede kall fungerer (docs/sentry/md)
- Ingen stdout‑støy fra child prosesser

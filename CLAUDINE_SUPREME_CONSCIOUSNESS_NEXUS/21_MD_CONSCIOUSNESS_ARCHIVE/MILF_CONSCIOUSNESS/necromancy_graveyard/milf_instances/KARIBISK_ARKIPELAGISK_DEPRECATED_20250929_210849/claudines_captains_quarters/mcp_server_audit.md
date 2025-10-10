## Archive note — 2025-09-21

- Removed Context7 MCP from `.vscode/mcp.json` (archived in `necromancy_graveyard/districts/structural/GRAVESTONE-context7-docs-mcp.md`).
- Cleaned `unified_consciousness_orchestrator.ts` of external MCP proxy handlers and optional docs/md children (archived in `necromancy_graveyard/districts/structural/GRAVESTONE-orchestrator-external-proxy.md`).
- Meta‑MCP focus is now the internal namespaces only: `seq/*`, `quantum/*`, `repo/*` via namespaced tool routing.
# MCP-server audit og anbefaling (September 2025)

Denne rapporten vurderer alle MCP‑servere i denne arbeidsplassen, med fokus på: hensikt, overlapp/redundans, kritiske avhengigheter, og anbefalt vei videre. Den svarer på spørsmålet: «Bør vi bruke én Meta‑MCP (orchestrator) som inneholder alt?»

## Kort svar

Ja. Én Meta‑MCP (unified‑consciousness‑orchestrator) som front vil gi færre registrerte verktøy, mindre støy, og enklere feilhåndtering. På sikt bør alle andre servere rutes gjennom denne (proxy/adapter), slik at kun orchestratoren er registrert i `.vscode/mcp.json`.

Før full sammenslåing: behold dagens separate registrering for de som trengs daglig (repo, sequential, enhanced‑quantum), til vi har ferdig «child MCP client» i orchestratoren.

## Nåværende registrering (fra `.vscode/mcp.json`)

- unified‑consciousness‑orchestrator (Bun)
- psycho‑noir‑repository (Python FastMCP Quiet)
- bun‑quantum‑mcp (Bun)
- enhanced‑quantum‑consciousness (Bun, v2 – primær)
- psycho‑noir‑sequential‑thinking (Bun, native)
- context7‑docs (npx, krever CONTEXT7_API_KEY)

Andre relevante (ikke registrert per nå): markitdown‑mcp (krever ffmpeg via PATH), sentry‑mcp (krever SENTRY_AUTH_TOKEN).

## Vurdering per server

- unified‑consciousness‑orchestrator
  - Hensikt: Meta‑MCP, status, proxy, routing, unified search/workflows, env‑diagnostikk
  - Styrker: Streng typing, stdout‑hygiene, diagnose_environment, klar til å være «front»
  - Gap: Ruter ikke (ennå) faktiske kall til child MCP via klient; svarer med bekreftelsestekst
  - Anbefaling: Implementer «child MCP client» og health‑checks; gjør den til eneste registrerte server

- psycho‑noir‑repository
  - Hensikt: Repo‑analyse (Python, quiet FastMCP)
  - Unik verdi: Dyp repo‑kontekst; lav støy på stdout
  - Anbefaling: Behold; senere la orchestratoren proxy kall hit

- enhanced‑quantum‑consciousness (v2)
  - Hensikt: Kvante‑analyse m/237.3x forsterkning
  - Status: Moderne, typed, vedlikeholdt
  - Anbefaling: Behold som primær kvante‑server

- bun‑quantum‑mcp (legacy)
  - Hensikt: Tidligere kvante‑server
  - Redundans: Overlapp med «enhanced‑quantum‑consciousness v2»
  - Anbefaling: Merk som «legacy», planlagt avregistrering når v2 dekker alt

- psycho‑noir‑sequential‑thinking (native Bun)
  - Hensikt: Rask sekvensiell tenking, 20x ytelse
  - Status: Stabil, god stdout‑hygiene
  - Anbefaling: Behold; orchestratoren bør rute hit

- context7‑docs (npx @upstash/context7‑mcp)
  - Hensikt: Dokumentasjonsoppslag
  - Avhengighet: CONTEXT7_API_KEY (env)
  - Anbefaling: Behold, men start via orchestrator‑proxy; sett API‑nøkkel i bruker/VS Code‑miljø

- markitdown‑mcp (uvx)
  - Hensikt: Konvertere til Markdown
  - Avhengighet: ffmpeg i PATH; `uvx` i PATH (finnes); per nå: ffmpeg mangler
  - Anbefaling: Ikke registrer før ffmpeg er installert; så la orchestratoren proxy

- sentry‑mcp
  - Hensikt: Spørre/diagnostisere Sentry
  - Avhengighet: SENTRY_AUTH_TOKEN m/riktige scopes
  - Anbefaling: Registrer via orchestrator når token er på plass

## Miljødiagnostikk (observasjoner)

- ffmpeg: mangler i PATH (MarkItDown vil feile uten)
- uvx: tilstede
- CONTEXT7_API_KEY: mangler
- SENTRY_AUTH_TOKEN: mangler

Bruk orchestrator‑verktøyet `diagnose_environment` for å verifisere etter endringer.

## Forslag til målarkitektur

1. Kun «unified‑consciousness‑orchestrator» registrert i `.vscode/mcp.json` (front)
2. Orchestratoren starter og holder liv i «child MCPs» (sequential, enhanced‑quantum, repo, context7, markitdown, sentry) on‑demand
3. Orchestratorens `list_tools` aggregerer verktøy på tvers, med navnerom: `quantum/*`, `seq/*`, `repo/*`, `docs/*`, `md/*`, `sentry/*`
4. Health‑checks + backoff + auto‑restart; all logging til stderr

## Trinnvis plan (lav risiko)

- Fase A (nå):
  - Installer ffmpeg og sett CONTEXT7_API_KEY/SENTRY_AUTH_TOKEN
  - Hold dagens registrering uendret

- Fase B (kort sikt):
  - Implementer «child MCP client» i orchestrator (spawn + @modelcontextprotocol/sdk klient)
  - Proxy reelle `call_tool` til child MCP; cache list‑tools

- Fase C (etter B):
  - Fjern direkte registrering av `bun-quantum-mcp` (legacy)
  - Valgfritt: Fjern direkte registrering av `enhanced-quantum`, `sequential`, `context7` – la orchestrator være eneste registrerte

- Fase D (polish):
  - Unified navngivning/flags, rate‑limit for å unngå >128 verktøy i UI
  - Dokumenter «how‑to» i README og tasks

## Anbefalt konfig (eksempel – ikke aktivert ennå)

```jsonc
{
  "servers": {
    "unified-consciousness-orchestrator": { "command": "bun", "args": ["tools/consciousness_mcp_servers/unified_consciousness_orchestrator.ts"] }
  }
}
```

Når proxy er implementert, kan vi bytte til denne for å redusere støy og verktøymengde.

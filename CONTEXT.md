# CONTEXT.md — MRCD Session State

**Update this file at the end of every AI assistant session before closing.**
**Load this file at the start of every session after GEMINI.md.**

---

## Current Phase & Task

Phase 1 Gate Passed. We have finalized the Content Matrix and generated the initial `framework.json` file embodying the psychological flow. We are now entering Phase 2 — Core Engine & Logic. Next task: 2.1 Vite Scaffolding.

---

## Phase 1 Complete

- [x] 1.1 Ideation & Brainstorming Document
- [x] 1.2 Project Brief
- [x] 1.3 Technical Specifications
- [x] 1.4 Repository boilerplate setup (README, .gitignore, etc.)
- [x] 1.5 CONTEXT.md setup
- [x] 1.6 Development Plan
- [x] 1.7 Content Matrix (Questions, Triggers, Personas)
- [x] 1.8 Phase 1 Gate (Ready for UI Scaffolding)

---

## Phase 2 Next Up (Core Engine & Logic)

- [ ] 2.1 Vite Scaffolding
- [ ] 2.2 Asset Integration
- [ ] 2.3 State Store
- [ ] 2.4 Base Layouts
- [ ] 2.5 Media Triggers
- [ ] 2.6 Questionnaire UI
- [ ] 2.7 Persona Calculator
- [ ] 2.8 Phase 2 Gate

---

## Architecture Decisions

| Decision | Detail |
|---|---|
| Architecture | Decoupled frontend-only SPA (React/Vite). No backend/DB for v1 prototype. |
| Logic/Content | Driven entirely by `public/config/framework.json`. Allows researchers to update tests via Git commits without touching code. |
| State Management | Zustand or React Context for tracking node traversal, scores, and leakage. |
| Visuals | "Dark & Neural" aesthetic. Real-time SVG/Canvas schematic node map. |
| Export | `html2canvas` + `jsPDF` to generate downloadable profile image + detailed psychological report. |
| Hosting | Vercel / Netlify / GitHub Pages with CI/CD linked to GitHub. |

---

## Open Questions & Risks

| Ref | Item | Status |
|---|---|---|
| R1 | PDF Export Layout | Open — Ensuring jsPDF perfectly captures the DOM SVG and text layout across different browsers. |
| R2 | Mobile Scrollytelling Performance | Open — Ensuring the background visualization SVG is performant while cards scroll over it on mobile. |

---

## File Map

*Populated as files are created. Add each file on the session it is first written.*

| File | Purpose |
|---|---|
| `GEMINI.md` | AI assistant standing brief |
| `CONTEXT.md` | Session state handoff (this file) |
| `SETUP.md` | Installation and local development guide |
| `README.md` | High-level project overview |
| `.gitignore` | Repo exclusion rules |
| `docs/MRCD 00 Ideation and Brainstorming.md` | Core psychological framework and UX logic |
| `docs/MRCD 01 Project Brief.md` | Project goals, scope, requirements, and user stories |
| `docs/MRCD 02 Technical Specification.md` | Architecture, state shape, JSON schema, and deployment |
| `docs/MRCD 03 Development Plan.md` | Phased task breakdown and milestones |
| `docs/MRCD_Content_Matrix.md` | Master narrative script, personas, and conversational flow |
| `public/config/framework.json` | The functional JSON schema containing the logic layer |

---

## Completed Sessions

### Phase 1 Session 1 — Project Planning & Architecture (2026-05-17)
- Completed `MRCD 00 Ideation and Brainstorming.md`
- Completed `MRCD 01 Project Brief.md` mapping out goals, scope, requirements.
- Completed `MRCD 02 Technical Specification.md` detailing frontend-only architecture and `framework.json` schema.
- Added CI/CD deployment strategy for GitHub-based updates.
- Scaffolded `CONTEXT.md`, `SETUP.md`, `GEMINI.md`, `README.md`, `.gitignore`.

### Phase 1 Session 2 — Content Matrix Finalization (2026-05-18)
- Developed deep research prompt for Gemini to map Rothgerber's framework.
- Finalized `docs/MRCD_Content_Matrix.md` establishing the 15-node flow, Persona Archetypes, and conversational tone.
- Generated the functional `public/config/framework.json` to act as the core logic layer.
- Officially closed Phase 1.

---

## Next Session
- **Phase 2, Task 2.1:** Scaffold React+TS+Vite and install Tailwind, Framer Motion, and Zustand.

---

*MRCD CONTEXT.md | Update at end of every session | Do not let this fall out of date*

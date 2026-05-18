# MRCD Interactive Web Experience — Development Plan

**Metacognitive Profiling Platform**

| Field | Value |
|---|---|
| Version | 1.0 |
| Date | May 2026 |
| Status | Phase 1 — Planning |
| Author | MRCD Project |
| Supersedes | Technical Specification v1.0 |

---

## 1. Purpose & Scope

This Development Plan covers the end-to-end build of the MRCD Interactive Web Experience across Phases 1–4. It defines phase milestones, task sequencing, definitions of done, the testing strategy, AI session workflow, and the risk/decision log.

---

## 2. Phased Overview

| Phase | Focus | Primary Deliverable | Gate Criterion |
|---|---|---|---|
| 1 | Foundations | Ideation, Project Brief, Tech Specs, Content Matrix, and repo setup. | All core documentation is approved and `framework.json` content is finalized. |
| 2 | Core Engine | React/Vite scaffolding, Tailwind setup, JSON parsing, State Management (Zustand), and the basic Questionnaire UI. | User can click through the entire questionnaire from start to finish based entirely on the JSON config. |
| 3 | Visualization | "Dark & Neural" SVG Schematic, Desktop Split-screen vs Mobile Scrollytelling layouts, and Framer Motion animations. | Node schematic accurately illuminates the user's path in real-time as they answer questions. |
| 4 | Export & Polish | PDF/Image export (`jsPDF`), Persona debrief, ambient audio controls, Web Share API, and live deployment. | User can complete the experience, view their persona, download their PDF report, and the app is live via CI/CD. |

---

## 3. Phase 1 — Foundations & Planning

### 3.1 Goal
Establish the project architecture, design language, documentation, and the complete psychological framework content.

### 3.2 Task Breakdown
| # | Task | Detail | Depends On |
|---|---|---|---|
| 1.1 | Ideation Document | Define core psychological framework and UX logic | - |
| 1.2 | Project Brief | Define goals, scope, and user stories | 1.1 |
| 1.3 | Technical Specification | Architecture, state shape, and JSON schema | 1.2 |
| 1.4 | Repository Setup | Boilerplate docs (README, SETUP, GEMINI, .gitignore) | 1.3 |
| 1.5 | Context Document | `CONTEXT.md` session state tracking | 1.4 |
| 1.6 | Development Plan | Phase milestones and task breakdown | 1.3 |
| 1.7 | Content Matrix | `framework.json` draft with all questions, triggers, and personas | 1.6 |
| 1.8 | Phase 1  | Review and approval of all planning artifacts | 1.7 |

### 3.3 Definition of Done
- All Phase 1 documents exist and are approved.
- `framework.json` contains a complete end-to-end path for at least one trigger.

---

## 4. Phase 2 — Core Engine & Logic

### 4.1 Goal
Scaffold the React application and build the logic layer. The app must dynamically load `framework.json` and allow a user to navigate through the questions.

### 4.2 Key Design Decisions
- **State Management:** Zustand to hold `currentNodeId`, `history` (for back navigation), and cumulative scores.
- **Styling:** Tailwind CSS with a strict "Dark & Neural" palette.

### 4.3 Task Breakdown
| # | Task | Detail | Depends On |
|---|---|---|---|
| 2.1 | Vite Scaffolding | Initialize React+TS+Vite, install Tailwind, Framer Motion, Zustand | Phase 1 |
| 2.2 | Asset Integration | Load `framework.json` into `public/config/` and media into `public/media/` | 2.1 |
| 2.3 | State Store | Build Zustand store tracking history, current node, and scores | 2.1 |
| 2.4 | Base Layouts | Scaffold Desktop (Split) and Mobile (Scrollytelling) main containers | 2.3 |
| 2.5 | Media Triggers | Build components to render initial video/image/text triggers | 2.4 |
| 2.6 | Questionnaire UI | Build interactive question cards that dispatch state updates | 2.4 |
| 2.7 | Persona Calculator | Logic to evaluate cumulative scores against persona conditions | 2.6 |
| 2.8 | Phase 2  | Verify end-to-end navigation logic (UI can be ugly, but logic must work) | 2.7 |

### 4.4 Definition of Done
- App runs locally.
- Questions map exactly to `framework.json`.
- "Back" button works.
- Reaching the end successfully calculates a final Persona.

---

## 5. Phase 3 — The Scientific Schematic

### 5.1 Goal
Bring the application to life visually. Implement the "Dark & Neural" interactive node map that tracks user progress.

### 5.2 Task Breakdown
| # | Task | Detail | Depends On |
|---|---|---|---|
| 3.1 | SVG Canvas | Build the base schematic component with hardcoded node coordinates | Phase 2 |
| 3.2 | Node States | Style unvisited (dark), active (glowing), and visited (lit) node states | 3.1 |
| 3.3 | Path Animations | Use SVG `stroke-dashoffset` to animate paths connecting nodes | 3.2 |
| 3.4 | State Sync | Connect the Schematic to Zustand so it reacts to the current node | 3.3 |
| 3.5 | Concept Tooltips | Add hoverable definition tooltips for complex psychological terms | 3.4 |
| 3.6 | Layout Polish | Ensure Schematic stays fixed on Desktop left-pane and background on Mobile | 3.4 |
| 3.7 | Phase 3  | Visual review of the complete responsive experience | 3.6 |

### 5.3 Definition of Done
- Schematic is fully interactive and visually polished.
- Mobile scrollytelling UX works flawlessly without overlapping issues.

---

## 6. Phase 4 — Export, Polish & Deployment

### 6.1 Goal
Finalize the user debrief, generate the downloadable PDF report, add ambient audio, and deploy to production.

### 6.2 Task Breakdown
| # | Task | Detail | Depends On |
|---|---|---|---|
| 4.1 | Debrief Screen | Build the final summary UI displaying the user's Persona and breakdown | Phase 3 |
| 4.2 | PDF Export Component | Build hidden `<ExportTemplate />` and integrate `jsPDF` + `html2canvas` | 4.1 |
| 4.3 | Social Share | Implement native Web Share API for mobile/desktop sharing | 4.1 |
| 4.4 | Ambient Audio | Add background audio loop with explicit opt-in and persistent mute toggle | 4.1 |
| 4.5 | CI/CD Setup | Connect GitHub repository to Vercel/Netlify for automated deployments | 4.4 |
| 4.6 | Phase 4  | Full production test of export, audio, and live site | 4.5 |

### 6.3 Definition of Done
- PDF successfully downloads with text and schematic image intact.
- Audio plays/mutes correctly.
- Site is accessible via a public URL.

---

## 7. Testing Strategy

| Level | When | What is tested | Tooling |
|---|---|---|---|
| Unit (Logic) | Phase 2 & 4 | Persona calculation logic, state history traversal (back button), JSON parsing | `Vitest` |
| Component | Phase 2 & 3 | UI components render correctly based on props | `React Testing Library` |
| End-to-end | Phase Gates | User can complete the full journey on Desktop and Mobile | Manual testing (Browser dev tools) |
| Visual / Export | Phase 4 | PDF generation renders correctly across browsers | Manual |

---

## 8. AI Assistant Workflow

### 8.1 Session Start Protocol
At the start of a session, the AI must read these files in order:
1. `GEMINI.md`
2. `CONTEXT.md`
3. `docs/MRCD 03 Development Plan.md` (specifically the current Phase and Tasks)

Then confirm to the user:
- What session we're on and which tasks it covers.
- Pre-conditions — are they met based on what is in `CONTEXT.md`?
- The Definition of Done for this session.
- Any open risks flagged for this session.

### 8.2 Session End Protocol
At the end of a session, the AI must update `CONTEXT.md`. Specifically:
- Mark completed tasks as `[x]` in the Phase Task Checklist.
- Add any new files to the File Map.
- Record any architecture decisions made this session.
- Update Open Questions & Risks if anything changed.
- Fill in the Completed Sessions log with today's date and a one-line summary.
- Set the Next Session block to the correct session number, tasks, and pre-conditions.
- Run `npm run lint` and `npm run format` (or equivalent) and fix anything that fails.
- Run the full test suite (`npm run test`) to confirm all tests pass.
- Commit all changes with a task-referenced message (e.g., `feat: Phase 2 Tasks 2.1 — React scaffolding`).
- **Show the final `CONTEXT.md` before closing** so the user can verify it.

### 8.3 Task Granularity
Sessions should target 1-3 tasks from the breakdown to keep PRs small and reviewable.

---

## 9. Risk & Decision Log

| # | Risk / Decision | Category | Detail | Status | Resolution |
|---|---|---|---|---|---|
| R1 | PDF Export Layout | Technical | `jsPDF` capturing complex SVGs or DOM elements can be flaky across different browsers. | Open | Test export early in Phase 4. Consider simplified hidden export templates if the main DOM fails to capture cleanly. |
| R2 | Mobile Scrollytelling | UX / Perf | Mobile browsers may struggle with heavy SVG animations fixed in the background while scrolling over them. | Open | Use CSS transforms for animations; avoid heavy repaints. Test on older mobile hardware. |
| R3 | Config Parsing | Design | Ensuring `framework.json` doesn't become too complex for researchers to edit without breaking the schema. | Open | Implement strict TypeScript interfaces and schema validation on app load. Provide a clear JSON template. |

---

## 10. Milestone Summary

| Phase | Gate | Gate Criterion |
|---|---|---|
| 1 | Foundations | All planning docs and Content Matrix approved. |
| 2 | Core Engine | App runs, JSON loads, state updates correctly from start to finish. |
| 3 | Visualization | Node schematic maps user path in real-time with polished animations. |
| 4 | Export & Polish | Debrief works, PDF downloads correctly, site deployed live. |

---
*MRCD Interactive Web Experience — Development Plan | Document Status: v1.0*

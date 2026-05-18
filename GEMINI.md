# GEMINI.md — MRCD Standing Brief

**Read this file at the start of every session before writing any code.**
**Then read CONTEXT.md to get the current session state.**

---

## 1. Project Summary

The MRCD Interactive Web Experience is a dynamic, highly personalized digital platform designed to automate the psychological profiling of Meat-Related Cognitive Dissonance.

The platform is designed as a decoupled, frontend-only Single Page Application (React/Vite). To ensure the platform is reusable for researchers without altering application code, the entire psychological framework (questions, triggers, scoring logic, personas) is driven by a static JSON configuration file (`public/config/framework.json`).

Full architecture, data models, and requirements are in:
- `docs/MRCD 01 Project Brief.md`
- `docs/MRCD 02 Technical Specification.md`

Current session state is tracked in `CONTEXT.md`.

---

## 2. Runtime Environment

| Item | Value |
|---|---|
| Framework | React (v18+) with Vite |
| Language | TypeScript |
| Styling | Tailwind CSS |
| Package manager | `npm` |

---

## 3. Directory Structure

```text
mrcd-app/
├── GEMINI.md                  ← this file
├── CONTEXT.md                 ← session state (read every session)
├── SETUP.md                   ← setup instructions
├── public/
│   ├── config/
│   │   └── framework.json     ← primary logic/content source of truth
│   └── media/                 ← trigger images/videos and audio
├── src/
│   ├── components/            ← React UI components
│   ├── context/               ← State management (Zustand/React Context)
│   ├── lib/                   ← Utilities and persona calculation logic
│   └── types/                 ← TypeScript definitions
├── docs/                      ← Project documentation
├── package.json
├── tailwind.config.js
└── vite.config.ts
```

---

## 4. Security & Data Rules

### 4.1 Data Privacy
- **Strictly Client-Side:** v1 must function entirely client-side. No user data, answers, or profiling results are transmitted to a server.
- Do not introduce backend requirements, database connections, or analytics telemetry into the v1 prototype.

### 4.2 Application Logic Boundary
- All content, questions, psychological terminology, and routing logic must remain in `public/config/framework.json`.
- **Do not hardcode** specific questions, answers, or trigger paths into React components. The UI must render dynamically based on the JSON configuration.

### 4.3 Git Operations
- Committing and pushing to GitHub does not require confirmation.
- The project is designed for seamless CI/CD. Updates to `framework.json` should trigger live deployments without rebuilding the frontend logic.

---

## 5. Code Conventions

### 5.1 Style & Framework
- Use **Tailwind CSS** for all styling.
- Ensure the UI follows the "Dark & Neural" aesthetic.
- Use **Framer Motion** for smooth, physics-based transitions, particularly in the Visualization layer.

### 5.2 TypeScript
- Use strict TypeScript typing for all state and component props.
- Ensure the JSON configuration matches a well-defined TypeScript interface in `src/types/framework.d.ts`.

### 5.3 Documentation
- Always update `docs/` when making architectural changes or creating new major documents.
- Keep `CONTEXT.md` up to date with session progress.

---

## 6. Testing & Validation

- Verify that the layout remains functional and adheres to the split-screen (Desktop) and scrollytelling (Mobile) paradigms.
- Ensure the `framework.json` schema remains strictly decoupled from UI logic.

---

## 7. When Uncertain

- **Stop and ask** rather than invent a design decision.
- If a task requires a decision not covered by the Technical Specification or this file, state the question explicitly and wait for an answer.
- Do not assume.

---

## 8. What Is Out of Scope for v1

Do not implement, design toward, or suggest the following unless explicitly asked:
- Backend databases (e.g., PostgreSQL)
- User authentication
- Centralized data analytics/tracking
- Dynamic force-directed node layout (use static coordinates for the schematic)

---

## 9. Phase Scope Reminder

Check `CONTEXT.md` for the current phase and task before writing any code. Do not implement features belonging to a future phase without explicit instruction.

---

## 10. AI Assistant Workflow (Session Protocol)

**At the start of a session:**
Please read these files in order:
1. `GEMINI.md`
2. `CONTEXT.md`
3. `docs/MRCD 03 Development Plan.md` (specifically the current Phase and Tasks)

Then confirm to the user:
- What session we're on and which tasks it covers.
- Pre-conditions — are they met based on what you see in `CONTEXT.md`?
- The Definition of Done for this session.
- Any open risks flagged for this session.

**At the end of a session:**
Update `CONTEXT.md`. Specifically:
- Mark completed tasks as `[x]` in the Phase Task Checklist.
- Add any new files to the File Map (if added).
- Record any architecture decisions made this session.
- Update Open Questions & Risks if anything changed.
- Fill in the Completed Sessions log with today's date and a one-line summary.
- Set the Next Session block to the correct session number, tasks, and pre-conditions.
- Run `npm run lint` and `npm run format` (or equivalent) and fix anything that fails.
- Run the full test suite (`npm run test`) to confirm all tests pass.
- Commit all changes with a task-referenced message, e.g.: `feat: Phase 1 Tasks 1.1, 1.2 — project scaffolding`.
- Show the final `CONTEXT.md` before closing so the user can verify it.

---

*MRCD GEMINI.md | Updated at project start | Refresh when conventions change*

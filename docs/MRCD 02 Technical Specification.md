# MRCD Interactive Web Experience — Technical Specification

**Metacognitive MRCD Profiling Platform**

| Field | Value |
|---|---|
| Version | 1.0 |
| Date | May 2026 |
| Status | Phase 1 — Frontend Prototype |
| Author | MRCD Project |
| Supersedes | Project Brief v1.0 |

---

## 1. Architecture

### 1.1 Layer Overview

The v1 MRCD platform is a decoupled, frontend-only Single Page Application (SPA). It uses static configuration files to drive logic, avoiding the need for a backend or database in the initial testing phase. This architecture ensures maximum portability and ease of initial testing.

| Layer | Technology | Responsibilities |
|---|---|---|
| **Web UI** | React / Vite / TypeScript | Renders the questionnaire, handles user inputs, manages audio, and provides the Scrollytelling/Split-screen layouts. |
| **State Engine** | Zustand (or React Context) | Maintains the user's progress through the framework, stores their answers, calculates the "leakage" or current Dissonance state, and determines the final Persona. |
| **Visualization Engine** | Custom SVG / React Flow | Renders the "Dark & Neural" schematic node map, animating active paths based on the State Engine. |
| **Configuration Layer** | Static JSON | Provides all textual content, trigger media paths, psychological definitions, and the logical routing map. |
| **Export Engine** | `html2canvas` + `jsPDF` | Captures the visualization layer and combines it with textual analysis to generate downloadable PNGs and PDFs. |

### 1.2 Component Communication

- **UI ↔ State Engine:** React components read from the global state to know which question to display. User interactions (clicks, choices) dispatch state updates.
- **State Engine ↔ Configuration Layer:** The State Engine loads the static `framework.json` file on initialization to construct the available graph of nodes and questions.
- **State Engine ↔ Visualization Engine:** The Visualization layer subscribes to state changes. As the user's "Active Node" updates in the state, the Visualization layer illuminates the corresponding SVG path and node.

---

## 2. Project & File System Structure

### 2.1 Root Layout

```
mrcd-app/
├── public/
│   ├── config/
│   │   └── framework.json        # The primary logic/content source of truth
│   ├── media/
│   │   ├── triggers/             # Images/videos used to trigger MRCD
│   │   └── audio/                # Ambient soundscapes
├── src/
│   ├── assets/
│   ├── components/
│   │   ├── ui/                   # Generic UI: Buttons, tooltips, modals
│   │   ├── schematic/            # SVG node visualization components
│   │   ├── questionnaire/        # Question cards, media players
│   │   └── export/               # Hidden components used for PDF generation templates
│   ├── context/
│   │   └── store.ts              # Zustand store / State management
│   ├── hooks/
│   ├── lib/
│   │   └── personaCalculator.ts  # Logic to map answers to final personas
│   ├── types/
│   │   └── framework.d.ts        # TypeScript definitions for JSON configs
│   ├── App.tsx
│   └── main.tsx
├── package.json
├── tailwind.config.js
├── tsconfig.json
└── vite.config.ts
```

---

## 3. Configuration Schema (`framework.json`)

To ensure the platform is reusable for research without altering application code, the MRCD logic is entirely driven by a JSON configuration file. 

### 3.1 JSON Structure Overview
```json
{
  "version": "1.0",
  "triggers": [
    {
      "id": "trigger_slaughterhouse",
      "type": "video",
      "src": "/media/triggers/video1.mp4",
      "prompt": "How does this footage make you feel?"
    }
  ],
  "nodes": [
    {
      "id": "node_willful_ignorance",
      "label": "Willful Ignorance",
      "stage": "prevention",
      "question": "Do you actively avoid thinking about where your meat comes from?",
      "options": [
        { "text": "Yes, I'd rather not know", "next_node": "node_dissonance_check", "value_weight": 1 },
        { "text": "No, I am fully aware", "next_node": "node_dissociation", "value_weight": 0 }
      ],
      "tooltip": "Willful ignorance is the act of intentionally avoiding information that might cause psychological discomfort."
    }
  ],
  "personas": [
    {
      "id": "persona_the_avoider",
      "title": "The Avoider",
      "description": "You heavily rely on prevention strategies, preferring to distance yourself from the reality of meat production.",
      "conditions": {
        "prevention_score_min": 3,
        "reduction_score_max": 2
      }
    }
  ]
}
```

### 3.2 Schema Field Reference

| Field | Type | Description |
|---|---|---|
| `triggers[].type` | string | `image`, `video`, `text`. Determines which media player component to render. |
| `nodes[].stage` | string | Maps to Rothgerber's framework: `trigger`, `prevention`, `dissonance`, `perceptual_reduction`, `behavioral_reduction`. |
| `nodes[].options[].next_node` | string | The ID of the node to route to if this option is selected. Allows branching paths. |
| `nodes[].options[].value_weight` | integer | A hidden score added to the user's profile to calculate their final Persona. |
| `personas[].conditions` | object | Logic rules to match a user's accumulated scores to a final Persona profile. |

---

## 4. State Management

The global state tracks the user's progress and allows for backward navigation. It is entirely client-side.

```typescript
interface MRCDState {
  // Configuration
  framework: FrameworkConfig | null;
  
  // User Session
  currentNodeId: string | null;
  history: string[]; // Array of previously visited node IDs to support "Back"
  answers: Record<string, string>; // Maps node_id -> selected_option_id
  scores: {
    prevention: number;
    dissonance: number;
    reduction: number;
  };
  
  // App State
  audioEnabled: boolean;
  finalPersona: Persona | null;
  
  // Actions
  selectOption: (nodeId: string, optionId: string, nextNodeId: string, weight: number) => void;
  goBack: () => void;
  toggleAudio: () => void;
  calculatePersona: () => void;
}
```

---

## 5. UI & Visualization Layer

### 5.1 Responsive Layouts
- **Desktop (Split Screen):** The screen is divided asymmetrically (e.g., 35/65). The left 35% is a fixed container holding the `VisualizationEngine`. The right 65% is a scrolling container holding the `QuestionnaireEngine`.
- **Mobile (Scrollytelling):** The `VisualizationEngine` is mounted as `fixed inset-0 -z-10`. The `QuestionnaireEngine` is transparent, allowing question cards to scroll over the schematic background.

### 5.2 The Scientific Schematic (Visualization Engine)
- Rendered using an SVG canvas (or a lightweight library like React Flow customized for strict UI constraints).
- Nodes are positioned using predefined coordinates to maintain the "Scientific Schematic" aesthetic, rather than an unpredictable force-directed graph.
- **State Mapping:** 
  - `unvisited`: Dark, low opacity, inactive styling.
  - `active` (current node): Glowing, pulsing animation (via Framer Motion or CSS).
  - `visited`: Lit, solid color, indicating the traversed path.
- Transitions between active nodes trigger an animated path drawing effect using SVG `stroke-dashoffset` animations.

---

## 6. Export & Report Generation

The final debrief requires generating a standalone image and a multi-page PDF report.

### 6.1 Tools
- `html2canvas` (or `dom-to-image`): Captures the React DOM (specifically the SVG Schematic) and converts it to a base64 PNG.
- `jsPDF`: Generates a PDF document purely in browser memory, inserting the captured PNG and rendering structured text.

### 6.2 Export Flow
1. User clicks "Download Full Report".
2. A hidden, specifically formatted React component (`<ExportTemplate />`) is populated with the user's assigned Persona and detailed Answers.
3. `html2canvas` captures the Schematic SVG.
4. `jsPDF` initializes a new document, places the captured image on the first page, and utilizes `.text()` methods to layout the psychological analysis, persona description, and glossary of terms used on subsequent pages.
5. The PDF is saved directly to the user's device using `doc.save('MRCD_Profile.pdf')`.

---

## 7. Deferred & Out of Scope (v1)

- **Backend / Database (`PostgreSQL`):** Not implemented in v1. All state is ephemeral in the browser session. No data is saved externally.
- **User Authentication:** No login system required.
- **Data Analytics:** No telemetry or tracking of user answers to a central server in the prototype.
- **Dynamic Node Positioning:** Node layout in the schematic is statically defined in the configuration to ensure a predictable, highly-polished "Dark & Neural" aesthetic, avoiding messy auto-layouts.

---

## 8. Deployment & CI/CD Strategy

The platform must support easy deployment and continuous updates directly from a GitHub repository.

- **Hosting Platform:** Vercel, Netlify, or GitHub Pages. These platforms natively support modern static site generators (Vite/React) and require zero backend infrastructure for v1.
- **Continuous Integration:** The GitHub repository will be linked to the hosting provider. Every push to the `main` branch will automatically trigger a build and deployment to the live site.
- **Content Updates via Git:** Because the application logic is completely decoupled and driven by `framework.json`, researchers can update triggers, questions, or personas simply by committing a change to the JSON file in GitHub. The CI/CD pipeline will automatically deploy the updated test to the live site without requiring any code changes or developer intervention.

---
*MRCD Interactive Web Experience — Technical Specification | Document Status: v1.0*

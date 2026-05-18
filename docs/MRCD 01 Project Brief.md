# MRCD Interactive Experience — Project Brief

**Metacognitive MRCD Profiling Platform**

| Field | Value |
|---|---|
| Version | 1.0 |
| Date | May 2026 |
| Status | Initial Draft |
| Author | MRCD Project |
| Supersedes | Ideation Summary v1.0 |

---

## 1. Executive Summary
The MRCD Interactive Web Experience is a dynamic, highly personalized digital platform designed to automate the psychological profiling of Meat-Related Cognitive Dissonance (MRCD). Based on Hank Rothgerber's (2020) conceptual framework, the platform forces users to confront their own psychological processing regarding the "meat paradox." Users navigate a scrolling questionnaire and media triggers, while a glowing, node-based "Scientific Schematic" dynamically maps their cognitive defenses in real-time.

The platform is designed primarily for meat-eaters to prompt metacognition and reflexivity. It is built as a highly responsive, desktop-first web application that allows users to explore key psychological concepts, review their mapped defenses, and export or share their final "MRCD Profile." Additionally, the platform is structured with a decoupled, modular architecture to serve as a future tool for formal psychological research.

---

## 2. Problem Statement
Meat-eaters often experience an underlying psychological conflict between caring for animals and eating them. This conflict is rarely addressed consciously:

| Problem | Impact |
|---|---|
| **Unconscious Processing** | Individuals deploy rapid cognitive defenses (e.g., willful ignorance, dissociation) automatically, preventing them from recognizing their own rationalizations. |
| **Lack of Metacognition** | Without a structured way to visualize these defenses, people cannot reflect on *how* they justify their actions. |
| **Ineffective Confrontation** | Traditional animal advocacy often triggers immediate defensiveness rather than genuine self-reflection. |
| **Abstract Frameworks** | Academic frameworks like MRCD are locked in papers (e.g., Rothgerber 2020) and are inaccessible to the general public for personal application. |

---

## 3. Vision & Goals

### 3.1 Vision
The MRCD platform translates dense psychological theory into a visceral, interactive digital experience. A user encounters a trigger, answers targeted questions, and watches as their personal web of cognitive dissonance is mapped out before them. By explicitly confronting them with their "MRCD Profile" and the objective reality of animal sentience, the platform leaves users in a state of productive, unresolved tension.

### 3.2 Goals

| # | Goal | Success Criterion |
|---|---|---|
| G1 | **Profile Completion** | >70% of users who start the experience complete the flow and generate their final MRCD Profile. |
| G2 | **Dynamic Schema Visualization** | The node-based schematic updates accurately in real-time based on user inputs without performance lag. |
| G3 | **Concept Comprehension** | Users actively engage with concept tooltips and end-point explorations (measured via interaction tracking). |
| G4 | **Profile Export & Sharing** | Users can download their final node profile as an image, or a detailed PDF report including their MRCD "persona", and share it externally. |
| G5 | **Research Modularity** | The application allows swapping of media triggers via simple configuration files for A/B testing. |
| G6 | **Responsive Accessibility** | The experience functions seamlessly on mobile devices, even while prioritizing the desktop split-screen layout. |

---

## 4. Target Users

| User Type | Profile | Primary Need |
|---|---|---|
| **The Meat-Eater (Primary)** | General public; consumes meat; experiences latent discomfort when confronted with the "meat paradox." | A structured, engaging way to visualize their own thought processes and prompt deep self-reflection. |
| **The Researcher (Secondary)** | Academic psychologist or behavioral scientist. | A modular, reliable platform to test the efficacy of different triggers on metacognitive arousal. |
| **The Advocate (Tertiary)** | Vegan/Vegetarian seeking to understand meat-eater psychology. | An educational tool to understand the specific psychological barriers preventing behavioral change. |

---

## 5. Scope

### 5.1 In Scope (v1)
- Interactive, responsive web application (Desktop prioritized, Mobile supported)
- Modular Trigger Engine (configurable "Sneak Attack" vs "Explicit Choice")
- Support for multimedia triggers (Images, Videos, Text)
- Optional ambient audio integration (starts silent, prompts user, always-visible mute toggle)
- Real-time "Scientific Schematic" node map visualization (SVG/Canvas)
- Back-navigation support allowing users to change answers
- Concept exploration (tooltips for rare words, deep-dives at end points)
- Final "MRCD Profile" generation and debrief, mapping users to specific MRCD "personas" based on their responses
- Export functionality (Download/Save profile as an image AND a detailed PDF report)
- Social sharing functionality
- Static JSON/YAML configuration for questions and logic

### 5.2 Out of Scope (v1)
- Full backend database and user account system (Deferred to Phase 4)
- Researcher dashboard and data analytics suite (Deferred to Phase 4)
- Explicit IRB consent forms and active data collection (Architecture ready, but hidden in v1)

---

## 6. Functional Requirements

### 6.1 Core UX & Navigation
| ID | Requirement | Notes |
|---|---|---|
| UX-01 | The system shall present a continuous or paginated flow mapping to the MRCD framework. | |
| UX-02 | The system shall allow the user to navigate backward to modify previous answers. | "Back" button always accessible. |
| UX-03 | The system shall support ambient audio playback with explicit opt-in and a persistent mute toggle. | Audio defaults to off. |
| UX-04 | The system shall provide tooltips or popovers for rare/unusual psychological terms. | e.g., "Dichotomization". |

### 6.2 The Scientific Schematic
| ID | Requirement | Notes |
|---|---|---|
| UI-01 | The system shall render a node-based diagram visually representing the MRCD framework. | "Dark & Neural" aesthetic. |
| UI-02 | The schematic shall dynamically illuminate and branch based on the user's specific answers. | |
| UI-03 | The schematic shall be explorable, allowing users to click past nodes to review their path. | |
| UI-04 | The layout shall be an asymmetric split-screen on Desktop and a scrollytelling background on Mobile. | |

### 6.3 Profile Generation & Export
| ID | Requirement | Notes |
|---|---|---|
| EX-01 | The system shall generate a final debrief screen displaying the user's complete MRCD Profile and assign them a specific MRCD "Persona". | Personas categorize common dissonance pathways. |
| EX-02 | The system shall allow users to explore deep-dive concepts at specific end points of their profile. | |
| EX-03 | The system shall provide a mechanism to download the visual profile as an image file (e.g., PNG). | |
| EX-04 | The system shall generate a detailed PDF report containing the image, persona description, and in-depth psychological analysis for offline reading. | |
| EX-05 | The system shall provide native or simulated social sharing options using the Web Share API. | Links or image sharing. |

### 6.4 Configuration & Modularity
| ID | Requirement | Notes |
|---|---|---|
| CF-01 | The application logic (questions, triggers, node mappings) shall be driven by external configuration files (JSON/YAML). | |
| CF-02 | The system shall support rendering image, video, or text-based triggers based on the configuration. | |

---

## 7. Non-Functional Requirements

| Attribute | Requirement |
|---|---|
| **Performance** | The schematic animation must render at 60fps on modern devices. Trigger media must lazy-load to prevent blocking the initial render. |
| **Responsiveness** | The UI must be fully usable on mobile devices (viewport width >= 320px) using the scrollytelling paradigm. |
| **Accessibility** | Interactive elements (buttons, tooltips) must be keyboard navigable. Text contrast must adhere to WCAG AA standards. |
| **Maintainability** | The content configuration must be strictly separated from the UI components to allow researchers to update questions without writing code. |
| **Privacy** | v1 must function entirely client-side. No user data is transmitted to a server unless explicitly configured for a future research phase. |

---

## 8. User Stories

### 8.1 The Journey
- As a user, I want to choose whether I am surprised by the trigger or explicitly opt-in, so I feel a sense of control.
- As a user, I want to navigate backward to change an answer if I realize I misunderstood a question.
- As a user, I want to hover over complex words to see definitions so I can understand the psychology being discussed.
- As a user, I want to be asked before audio plays, and have a clear mute button, so I am not startled in a public place.

### 8.2 The Schematic
- As a user, I want to see my choices visually mapped in real-time so I can understand how my cognitive defenses connect.
- As a user, I want to click on previous nodes in the diagram to remind myself of the path I took.
- As a user, I want to read detailed explanations of the endpoints I reached so I can reflect on my specific justifications.

### 8.3 The Aftermath
- As a user, I want to see which MRCD "persona" I fall into so I can understand my responses in a broader psychological context.
- As a user, I want to download a detailed PDF report of my profile so I can read a fuller text description of my cognitive defenses offline.
- As a user, I want to download my final node profile as a quick image to save it for personal reflection.
- As a user, I want to share my profile using the native Web Share API to easily spark conversation with others.

---

## 9. Architecture Overview

| Layer | Responsibilities |
|---|---|
| **Interactive UI Layer (React)** | Renders the questionnaire, media triggers, tooltips, and audio controls. Handles responsive layout shifting (Desktop Split vs Mobile Scrollytelling). |
| **Visualization Engine (SVG/Canvas)** | Renders the "Dark & Neural" schematic map. Handles node illumination, animations, and pan/zoom mechanics. |
| **State & Logic Engine** | Tracks user inputs, calculates Dissonance leakage, manages the "Back" history stack, and determines the final profile state. |
| **Configuration Layer (JSON)** | Provides the source of truth for all text, media paths, and node relationships. |

*Note: Data persistence and backend APIs are explicitly decoupled and excluded from the v1 prototype.*

---

## 10. Technology Stack

| Component | Technology | Rationale |
|---|---|---|
| **Framework** | React / Vite / TypeScript | Modern, type-safe component architecture necessary for complex state management. |
| **Styling** | Tailwind CSS | Rapid, responsive, utility-first layout management. |
| **Animations** | Framer Motion | Smooth, physics-based transitions for the scrollytelling and UI elements. |
| **Visualization** | React Flow or Custom SVG | Ideal for node-based, interactive, pannable schematic diagrams. |
| **Export Tooling** | html2canvas + jsPDF | Standard libraries for capturing DOM elements as images and generating the detailed PDF report. |
| **Content Config** | JSON | Native to JS ecosystem, easy for non-developers to edit. |

---

## 11. Constraints & Assumptions

### 11.1 Constraints
- The project will begin as a frontend-only prototype to validate the UX and psychological impact.
- Heavy SVGs or Canvas animations may degrade battery life or performance on very old mobile devices; optimizations will target modern smartphone browsers.

### 11.2 Assumptions
- Users have modern, Javascript-enabled web browsers.
- Social sharing relies on the user's OS native sharing capabilities (Web Share API) where applicable, or standard fallback links.
- The psychological framework outlined by Rothgerber (2020) is fixed and will map 1:1 to the application logic.

---

## 12. Success Metrics

| Metric | Target |
|---|---|
| Completion Rate | > 70% of started sessions reach the debrief screen. |
| Debrief Engagement | Average time spent on the final debrief screen > 60 seconds. |
| Export/Share Rate | > 15% of users who complete the flow download or share their profile. |
| Interaction Depth | > 40% of users interact with at least one tooltip or explorable node. |
| Performance | Time to Interactive (TTI) < 3.0 seconds on standard broadband. |

---

## 13. Next Steps

| # | Document | Contents |
|---|---|---|
| 1 | **Technical Specification** | Detailed architecture, component structure, state management shape, and JSON configuration schema. |
| 2 | **Development Plan** | Phase milestones, task breakdown, testing strategy, and definition of done. |
| 3 | **Repository Setup** | Creation of standard repository documents (CONTEXT.md, SETUP.md, GEMINI.md, README.md, .gitignore). |
| 4 | **Content Matrix** | Mapping the exact questions, triggers, and tooltip definitions to the node framework. |
| 5 | **Phase 1 Development** | Begin UI scaffolding and JSON configuration integration. |

---
*MRCD Interactive Web Experience — Project Brief | Document Status: v1.0*

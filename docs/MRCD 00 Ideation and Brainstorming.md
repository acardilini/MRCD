# MRCD Interactive Web Experience — Ideation Session Summary

| Field | Value |
|---|---|
| Version | 1.0 |
| Date | May 2026 |
| Status | Initial Draft |

---

## 1. Purpose of This Document
This document summarizes the ideation session for the Meat-Related Cognitive Dissonance (MRCD) interactive web experience. It captures the problem context, product vision, MRCD psychological framework mapping, key design decisions, architectural direction, and development strategy. It serves as the foundation for subsequent project documentation including the Product Requirements Document (PRD), Technical Specification, and Development Plan.

---

## 2. Problem Statement & Vision

### 2.1 Problem
Meat-eaters often experience an underlying psychological conflict—the "meat paradox"—between caring for animals and eating them. When confronted with this paradox, individuals typically deploy rapid, unconscious cognitive defenses to prevent or reduce negative arousal (dissonance) rather than changing their behavior. These automated defenses limit metacognition and prevent individuals from fully recognizing the psychological mechanisms they use to justify their actions.

### 2.2 Vision
The MRCD Interactive Web Experience is a dynamic, highly personalized digital platform that forces users to confront their own psychological processing. By walking users through Hank Rothgerber's (2020) MRCD framework, the platform dynamically maps their individual cognitive defenses. The vision is to prompt metacognition and reflexivity, intentionally leaving users with unresolved tension that encourages long-term contemplation about their meat consumption and animal autonomy. Furthermore, the platform is designed to serve as a modular tool for psychological research.

---

## 3. Target Users
- **Primary:** Meat-eaters (to induce self-reflection and metacognition).
- **Secondary:** Psychological and behavioral researchers (testing metacognition, triggers, and cognitive dissonance).
- **Tertiary:** Vegetarians/Vegans (seeking to understand the psychological barriers of meat-eaters).

---

## 4. Core Concepts & Design Decisions

### 4.1 The Scientific Schematic Metaphor
The central UI/UX element is a sleek, glowing, node-based schematic diagram. As the user answers questions, nodes light up, branch out, and lock in, constructing a literal visual "MRCD Profile." This creates a powerful contrast between the sterile, complex ways we rationalize choices and the grounded reality of animal lives.

### 4.2 Progressive Disclosure & Flow
The user journey closely mirrors the MRCD framework. Users are not given the entire map at once; it unfolds sequentially:
1.  **Baseline Demographics & Implicit Variables** (e.g., Masculinity, Social Dominance, Empathy)
2.  **The Trigger Event** (reminders of animal origins)
3.  **Prevention Assessment** (Avoidance, Willful Ignorance, Dissociation)
4.  **Dissonance Check** (Negative Arousal/Guilt leakage)
5.  **Reduction Strategies** (Perceptual and Behavioral)

### 4.3 Modular Trigger Engine
The platform supports testing different triggers. Users can be routed through a "Sneak Attack" (where the trigger is unexpected) or an "Explicit Choice" mode. This allows researchers to swap media types (videos, images, narratives) via static configuration to test efficacy.

### 4.4 The Provocative Debrief
The experience intentionally avoids a "feel-good" resolution. The debrief dismantles their chosen defenses by reinforcing the objective reality of animal sentience and autonomy. If statistical data is shown, it is framed critically (e.g., "This mechanism is used by X% of people... meaning it is socially reinforced to help you ignore reality").

---

## 5. The MRCD Conceptual Framework Mapping (Rothgerber, 2020)
*To build a robust PRD, the platform's logic must perfectly mirror the stages of Figure 1 from the Rothgerber paper.*

### 5.1 Step 1: The Meat Paradox & Triggers
The inherent conflict between caring for animals and eating them. Triggers make this paradox salient (e.g., reminders of animal origins, exposure to animal suffering).

### 5.2 Step 2: Prevention Strategies
Mechanisms used proactively to prevent the trigger from causing negative arousal:
*   *Avoidance:* Actively avoiding information.
*   *Willful Ignorance:* Choosing not to know.
*   *Dissociation:* Disconnecting meat from the living animal.
*   *Perceived Behavioral Change:* Falsely believing one eats less meat.
*   *Do-Gooder Derogation:* Putting down vegetarians.

### 5.3 Step 3: The Dissonance State (Negative Arousal)
If prevention fails, the user experiences psychological discomfort (guilt or negative arousal).

### 5.4 Step 4: Dissonance-Reducing Mechanisms (Perceptual)
Post-hoc rationalizations to alleviate guilt:
*   *Denying Animal Mind/Sentience*
*   *Pro-Meat Justifications (The 4Ns):* Natural, Normal, Necessary, Nice.
*   *Dichotomization:* "Pets" vs. "Food".
*   *Reducing Perceived Choice:* Believing meat is unavoidable.

### 5.5 Step 5: Dissonance-Reducing Mechanisms (Behavioral)
Changing actions to align with values (e.g., transition to vegetarianism).

---

## 6. Technology Stack Decisions

| Component | Decision | Rationale |
|---|---|---|
| Language / Framework | React / Vite / TypeScript | Modern, highly interactive component-based UI required for the dynamic node schematic and smooth transitions. |
| Styling | Tailwind CSS + Framer Motion | Tailwind for rapid, responsive layout; Framer Motion for complex SVG node animations and scrollytelling transitions. |
| Content Configuration | JSON / YAML (Static) | Allows researchers to swap questions, triggers, and pathways without touching core logic or needing a database initially. |
| Data Storage (v1) | LocalStorage / SessionStorage | Keeps the initial prototype simple, fast, and entirely client-side without backend overhead. |
| Architecture Strategy | Frontend-First (Decoupled) | Allows immediate UX testing and prototyping. State is managed to easily "bolt on" a backend later for data collection. |

---

## 7. High-Level Architecture

The system is structured for immediate prototyping with future scalability:
- **Interactive UI Layer:** Dual-layout system based on device.
  - *Desktop:* Asymmetric Split Screen (Schematic 30-40% fixed left, questionnaire scrolling right).
  - *Mobile:* Scrollytelling (Schematic as full-bleed background, zooming and panning to nodes as question cards float over).
- **State & Logic Engine:** Manages user progression through the MRCD framework, tracking implicit variables and calculating the final profile state.
- **Configuration Layer:** Static files defining the questions, triggers, and schematic node mappings.
- **Aesthetic Core:** "Dark & Neural" theme—moody dark tones with brightly colored, glowing neon nodes emphasizing internal cognitive processing.

---

## 8. Development Strategy

### 8.1 Approach
Frontend-first, lean development. Build a working interactive prototype focused on the UX flow and the visual node schematic. Test the psychological impact before layering in backend data collection and researcher dashboards.

### 8.2 Phased Roadmap

| Phase | Focus | Key Deliverables |
|---|---|---|
| Phase 1 | Foundation & Core UX | Basic React/Vite app setup; routing; static JSON configuration integration; implementation of the scrolling questionnaire interface. |
| Phase 2 | The Schematic Metaphor | Build the interactive node map (SVG/Canvas); map user responses to node states; implement animations (glowing, branching); responsive layout (Desktop Split vs. Mobile Scrollytelling). |
| Phase 3 | Logic & Profiling | Implement the implicit variable tracking; Dissonance leakage logic; final "MRCD Profile" generation; the Provocative Debrief presentation. |
| Phase 4 | Backend Integration (Future) | Database provisioning for research data collection; researcher dashboard; hidden IRB/Consent flows made active. |

---

## 9. Deferred & Out of Scope (v1)
- **Full Backend / Database:** Deferred to Phase 4. v1 focuses on the UX prototype.
- **Researcher Dashboard:** Not in scope for the initial build.
- **Explicit IRB / Privacy Flow Activation:** Designed into the architecture but hidden for initial user testing.
- **User Accounts / Login:** Not required; sessions are ephemeral or tied to a research participant ID.

---
*MRCD Interactive Web Experience — Ideation Summary | Document Status: v1.0*

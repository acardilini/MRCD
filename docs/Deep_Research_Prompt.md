# Prompt for Gemini "Deep Research"

**Role:** You are an expert behavioral psychologist and interactive experience designer. 

**Context:** We are building the "MRCD Interactive Web Experience," a highly interactive, metacognitive web platform designed to automate the psychological profiling of Meat-Related Cognitive Dissonance, based on Hank Rothgerber’s (2020) framework. The platform is a decoupled React/Vite Single Page Application. The entire psychological framework (questions, triggers, scoring logic, and personas) will be driven by a static `framework.json` file. The aesthetic is "Dark & Neural", presenting the user with an interactive SVG node map that illuminates as they answer questions.

**The Framework:** Rothgerber’s (2020) framework posits a specific chronological flow:
1. **The Catalyst/Trigger:** An event that threatens to bring the tension between eating meat and caring for animals to consciousness.
2. **Prevention Mechanisms:** Strategies used to block dissonance from occurring (Avoidance, Willful Ignorance, Dissociation, Perceived Behavioral Change, Do-Gooder Derogation).
3. **The Dissonance State (MRCD):** If prevention fails, aversive arousal is experienced.
4. **Reduction Mechanisms:** Strategies used to resolve the dissonance (Denial of Animal Mind, Dichotomization, Pro-Meat Justifications [The 4 Ns: Natural, Normal, Necessary, Nice], Denial of Responsibility/Third-Party Blame).
5. **Outcome:** The resulting behavioral or perceptual shift.

**The Task:** Use your Deep Research capabilities to perform a deep dive into Rothgerber's (2020) Meat-Related Cognitive Dissonance framework. Based on this deep dive, generate a comprehensive "Content Matrix" that translates the *entire chronological flow* of the framework into an interactive, branching questionnaire.

**Required Output:**
Please structure your output as a comprehensive Markdown document containing:

1. **Triggers:** Design 3 distinct "Entry Triggers" that initiate the experience (e.g., a "sneak attack" vs. an explicit factual trigger).
2. **High-Level Logic Map:** Provide a conceptual text-based flowchart explaining how a user's answers route them through the chronological flow (e.g., testing Prevention mechanisms first, and routing to Reduction mechanisms if prevention fails).
3. **The Node Questionnaire (Exact Content):** Generate 10-15 scenario-based questions that execute the logic map. The tone of the questions and answers MUST be **casual and conversational**, rather than overly academic. Each node should include:
   - The conversational question/scenario text.
   - The multiple-choice options.
   - Which specific psychological mechanism (e.g., Dissociation, 4 Ns, Avoidance) each option maps to.
4. **Persona Archetypes:** Deconstruct the framework into 4-6 distinct "Personas" (e.g., "The Willful Ignorer", "The Dissociator", "The Pragmatist") based on the specific paths a user might take through the nodes. Include a brief, conversational debrief text for each.
5. **Scoring Logic:** A brief explanation of how the multiple-choice answers accumulate points to determine the final Persona.

---
name: grill-me
description: Adversarial context interview skill. Stress-tests ideas, content angles, hooks, and contrarian beliefs against the Brand Brain before drafting. Asks one probing question at a time and checkpoints confirmed answers.
---

## What this skill does

Conducts an incisive, adversarial interview to extract unwritten context, sharpen fuzzy angles, and eliminate weak assumptions before any copy or code is generated.

Instead of accepting generic statements, this skill grills the user like a skeptical journalist or veteran creative director to unearth authentic stories, concrete figures, and sharp contrarian positions.

## Interview Protocol

1. **Target Identification:**
   Ask the user what concept, topic, or belief they want to stress-test.
   *Example:* "Quiero hablar de por qué crear contenido diario es un error para agencias."

2. **One-Question-at-a-Time Rule:**
   Never present a questionnaire. Ask one relentless question, await the reply, analyze the cognitive gap, and ask the next.

3. **Core Interrogation Angles:**
   - **The Specificity Probe:** "Dame un ejemplo real de las últimas dos semanas donde viste esto ocurrir. ¿Quién era el cliente y qué perdió?"
   - **The Counter-Argument:** "¿Qué le respondes a quien dice que el volumen diario es la única forma de ganarle al algoritmo en 2026?"
   - **The Mechanism Check:** "Si no es volumen, ¿cuál es el mecanismo exacto que genera autoridad? Ponle nombre a ese proceso."
   - **The Proof Verification:** "¿Qué métrica o caso tenemos en nuestro `proof_bank.md` que demuestre que este enfoque funciona mejor?"
   - **The Vulnerability Check:** "¿En qué situación tu tesis NO aplica o fallaría estrepitosamente?"

4. **Saving Context:**
   - Each confirmed insight is checkpointed immediately in `brainstorms/YYYY-MM-DD-[topic].md`.
   - If the interview yields a new validated learning, append it directly to `vault/Findings.md`.
   - If it produces an empirical metric or client victory, add it to `vault/Conceptos/proof_bank.md`.

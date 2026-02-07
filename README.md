# MindLoad
MindLoad is a no-code / low-code study support prototype that helps students organize academic schedules and study resources in one website. The system uses structured data inputs like calendars or study guides and simple automated workflows to generate relevant study tips and reminders. 
This project is an early-stage prototype focused on workflow design, data handling, and automation logic rather than custom backend development or advanced AI models.
## HOW TO RUN 
1) Open the project in the platform workspace (Emergent)
2) Navigate through the screens or workflow steps to see how schedules and study resources are organized.
3) Upload example data files, like a student schedule CSV or a study tips document, to test how the system displays relevant information.
4) Click on the buttons or interact with the workflow to see study reminders and suggested tips appear.
5) You can explore different paths in the workflow .
6) No coding is required—everything is visual and interactive in the platform.
MindLoad uses rule-based and prompt-driven logic to analyze user input about workload and stress, generating supportive burnout feedback.
## Day 3 – Building the Brain of MindLoad

### Core logic
MindLoad uses rule-based and prompt-driven logic to analyze user input about workload and stress, generating supportive burnout feedback.

### Data / API integration
Inputs come from Emergent AI. Workflow processes text input to give burnout insights. No-code integration is fully functional for demo purposes.

### Test questions / exam set
Examples include:
- "I feel exhausted even after sleeping"
- "I’m busy but managing okay"
- "I feel stressed all the time"
- "I don’t know how I feel"
- "Everything feels overwhelming lately"

### Baseline results
Initial testing shows the app can categorize burnout levels (low / moderate / high) and provide relevant feedback.

### Run instructions
Open the MindLoad Emergent AI demo link, enter your input, and check the burnout feedback.

## Day 4 – Optimizing Integration & Application Evaluation

### Evaluation
Test set is stored within Emergent AI logic. Metrics considered: relevance, clarity, consistency, coverage.

### Top failure modes
- Very short or vague inputs produce generic feedback
- Ambiguous workload descriptions cause unclear burnout categorization
- Empty submissions give incomplete results

### Fixes applied
- Input validation prevents empty submissions
- Prompt logic refined for vague inputs
- Output formatting improved to clearly explain burnout levels

### Decisions
- Chose qualitative metrics to focus on user experience
- Implemented validation and fallback messaging in low-code workflow

### Safety & guardrails
- No PII collected
- Outputs are supportive and non-diagnostic
- User input validated for safety

### Blockers
- Improving response nuance for complex inputs
- Deciding how much guidance to give without medical advice

## Day 5 – Integration of Model/API with Interface

### User flow
Input → Analyze → Feedback; all screens and outputs designed clearly in Glide AI.

### Backend connection
Low-code workflow connects the UI to the app logic (rule-based / prompt-driven).

### UX basics
- Loading indicators added
- Input validation & friendly fallback messages
- Reset/clear functionality implemented

### Logging
Safe logging enabled for internal test purposes (no PII)

### Demo link
[Emergent AI MindLoad demo link here](https://stress-pulse-1.emergent.host/)

### Screenshots
![Graph screen](https://raw.githubusercontent.com/Neriah-tech/MindLoad/4f22437e4bbb62a2d65f6da7bb38b6723c4db333/Screenshot%202026-02-07%20173747.png)
![chatbot interface](https://raw.githubusercontent.com/Neriah-tech/MindLoad/4f22437e4bbb62a2d65f6da7bb38b6723c4db333/Screenshot%202026-02-07%20174125.png)
![Input screen](https://github.com/Neriah-tech/MindLoad/blob/main/Screenshot%202026-02-07%20172855.png?raw=true)
![Study Tip screen](https://raw.githubusercontent.com/Neriah-tech/MindLoad/4f22437e4bbb62a2d65f6da7bb38b6723c4db333/Screenshot%202026-02-07%20174204.png)
![Output screen](https://raw.githubusercontent.com/Neriah-tech/MindLoad/4f22437e4bbb62a2d65f6da7bb38b6723c4db333/Screenshot%202026-02-07%20173342.png)

### Known UX issues
- Output can be generic for very short inputs
- Reset/clear flow could be more explicit
- Input/output distinction could be visually clearer

### Decisions
- Used Emergent AI for fast UI–logic integration
- Kept flow minimal for beginner-friendly demo

### Blockers
- Further personalizing responses
- Minor UX visual improvements
## Day 6 – Final Enhancements, Security & Debugging

### Input validation
Checked empty or vague inputs; prompts users for clarification.

### Secrets handling
No API keys or sensitive information in the repo; handled entirely in Emergent AI workflow.

### Rate limits / caching
Lightweight processing avoids latency or rate-limit issues.

### Bug fixes
- Empty input fallback added
- Short/ambiguous input clarified
- Reset/clear flow fixed

### README / architecture notes
Updated workflow, architecture description, and screenshots.

### Remaining risks
- Generic feedback for very short inputs
- Minor UX visual polish needed

### Decisions
- Focused on validation, fallback, and workflow clarity for judge-friendly app
- Used low-code solutions for debugging and security

### Blockers
- Refining responses for nuanced inputs
- Optional UX polish

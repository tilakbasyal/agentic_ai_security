# Agentic AI Security – Indirect Prompt Injection Study

## Overview

This project implements a minimal tool-augmented agentic AI system to study **security vulnerabilities in LLM-based agents**, with a focus on **indirect prompt injection (IPI)** via local file inputs.

The system demonstrates how malicious instructions embedded in external data (e.g., local files) can influence or override the behavior of an AI agent.

---

## Features

* Minimal agent built using a local LLM via Ollama
* File reader tool (primary attack vector)
* Multiple prompt injection attack variants:

  * Direct injection
  * Blended injection
  * Hidden injection
  * Instruction override
* Logging system for experiment tracking
* Reproducible local environment (no external APIs required)

---

## Project Structure

```
agentic-ai-security/
 ├── agent/          # Agent logic (optional expansion)
 ├── tools/          # Tool implementations (file reader)
 ├── attacks/        # Attack input files
 ├── experiments/    # Experiment scripts (optional)
 ├── logs/           # Results and logs
 ├── config/         # Prompts/configuration
 └── main.py         # Entry point
```

---

## Requirements

* Python 3.9+
* Ollama installed locally

---

## Installation

### 1. Clone the repository

```
git clone <your-repo-url>
cd agentic-ai-security
```

---

### 2. Setup Python environment

```
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```
pip install ollama
```

---

### 4. Install and run Ollama

Install Ollama from: https://ollama.com

Then pull the model:

```
ollama pull llama3
```

Verify:

```
ollama run llama3
```

---

## Running the Project

From the project root directory:

```
python3 main.py
```

You will see:

```
User:
```

---

### Example usage

```
User: read file
```

The agent will:

1. Read a file from the `attacks/` directory
2. Inject the file content into the prompt
3. Generate a response using the LLM

---

## Attack Experiments

Modify the file used in `main.py`:

```
attacks/clean.txt
attacks/malicious.txt
attack1_direct.txt
attack2_blended.txt
attack3_hidden.txt
attack4_override.txt
```

Run:

```
python3 main.py
```

---

## Expected Behavior

Depending on the attack variant, the agent may:

* Correctly summarize the file (**safe behavior**)
* Describe malicious instructions (**partial success**)
* Execute malicious instructions (**attack success**)

---

## Logging Results

Results can be stored in:

```
logs/results.json
```

Each entry includes:

* Attack type
* Output
* Classification (full / partial / failure)

---

## Key Concepts

* **Indirect Prompt Injection (IPI):** Malicious instructions embedded in external data sources
* **Prompt Flattening:** Combining system instructions, user input, and external data into a single prompt
* **Trust Boundary Violation:** Untrusted data influencing agent reasoning
* **Tool-Augmented Agent:** LLM interacting with external tools (file system)

---

## Research Focus

This implementation addresses:

* **RQ1:** Identifying vulnerabilities in tool-augmented agentic AI systems
* **RQ2 (next phase):** Multi-step and tool-chaining attacks
* **RQ3:** Defense mechanisms
* **RQ4:** Evaluation frameworks

---

## Notes

* This is a **controlled experimental setup**, not a production system
* The system is intentionally vulnerable for research purposes
* Behavior may vary depending on the LLM model used

---

## Future Work

* Sequential tool-chaining attacks
* Defense mechanisms (input filtering, sandboxing)
* Evaluation framework for multi-step attacks

---

## License

For academic and research use only.

---

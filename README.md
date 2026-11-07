# 🛡️ ZeroTrace — AI Incident Response Agent

ZeroTrace is an AI-powered incident response agent that learns from previous production incidents using **Hindsight memory**.

## 🚨 Problem

Production teams often face recurring incidents such as API failures, high CPU usage, service crashes, and outages. Troubleshooting can start from scratch each time because previous incident knowledge is difficult to reuse.

## 💡 Solution

ZeroTrace remembers previous incidents, their resolutions, and operational experience. When a new incident occurs, it searches its memory and reasons over previous experiences to recommend a practical response.

## 🧠 How Hindsight Is Used

ZeroTrace uses Hindsight as its long-term operational memory:

- **`retain()`** — Stores incidents and their resolutions.
- **`recall()`** — Finds relevant previous incidents.
- **`reflect()`** — Reasons over stored experiences and recommends a response.
- **`retain()` again** — Saves the new resolution as future experience.

### Learning Loop

Past Incident → Hindsight Memory → New Incident → Recall → Reflect → Recommendation → Resolution → New Memory

## 🛠️ Tech Stack

- Python
- Streamlit
- Hindsight Cloud
- hindsight-client
- python-dotenv

## 🚀 Run Locally

Create a virtual environment:

```bash
python3.14 -m venv .venv314
source .venv314/bin/activate

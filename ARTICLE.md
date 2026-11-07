# ZeroTrace — AI Incident Response Agent

## The Problem

Production teams regularly face incidents such as API failures, service crashes, high CPU usage, and outages. When similar incidents happen again, engineers often have to troubleshoot from the beginning because previous operational knowledge is difficult to reuse.

## Our Solution

ZeroTrace is an AI Incident Response Agent that uses Hindsight as long-term operational memory.

Instead of treating every incident as a new problem, ZeroTrace remembers previous incidents, their causes, resolutions, and operational experience.

When a new incident occurs, ZeroTrace:

1. Searches Hindsight for similar incidents.
2. Recalls relevant previous experience.
3. Uses Hindsight reflection to reason over that experience.
4. Generates a practical incident response recommendation.
5. Records the final resolution back into memory.

## How Hindsight Powers ZeroTrace

ZeroTrace uses three important Hindsight capabilities:

- `retain()` — stores incidents and their resolutions.
- `recall()` — finds relevant previous incidents.
- `reflect()` — reasons over stored experience and recommends a response.

After the incident is resolved, the new experience is stored again using `retain()`.

This creates a continuous learning loop:

**Past Incident → Hindsight Memory → New Incident → Recall → Reflect → Recommendation → Resolution → New Memory**

## Example

A production API starts returning 503 errors while CPU usage reaches 95%.

ZeroTrace searches its memory and finds a previous incident with the same symptoms. The previous incident was resolved by restarting the backend service and monitoring CPU usage.

ZeroTrace uses this experience to recommend a similar response and explains why the previous incident influenced its recommendation.

## Technology

- Python
- Streamlit
- Hindsight Cloud
- hindsight-client
- python-dotenv

## Impact

ZeroTrace helps teams reduce repeated troubleshooting effort by turning previous incident knowledge into reusable operational memory.

The goal is not just to generate an answer, but to make the incident response agent **learn from what happened before**.

## Project

GitHub: https://github.com/Shashau/ZeroTrace

Live Demo: https://zerotrace-tfeebzxplkhunphgbe4s6s.streamlit.app/

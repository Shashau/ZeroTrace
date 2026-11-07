import os
import streamlit as st
from dotenv import load_dotenv
from hindsight_client import Hindsight

load_dotenv()

HINDSIGHT_API_KEY = os.getenv("HINDSIGHT_API_KEY")
HINDSIGHT_BASE_URL = os.getenv("HINDSIGHT_BASE_URL")
BANK_ID = os.getenv("HINDSIGHT_BANK_ID")


def create_client():
    return Hindsight(
        base_url=HINDSIGHT_BASE_URL,
        api_key=HINDSIGHT_API_KEY,
    )


st.set_page_config(
    page_title="ZeroTrace",
    page_icon="🛡️",
    layout="centered",
)

st.title("🛡️ ZeroTrace")
st.subheader("AI Incident Response Agent")

st.write(
    "ZeroTrace remembers previous production incidents and learns "
    "from past resolutions to recommend faster responses."
)

st.divider()

incident = st.text_area(
    "🚨 Describe the incident",
    placeholder=(
        "Example: Production API is returning 503 errors "
        "and CPU usage is 95%."
    ),
    height=130,
)

if st.button("🔍 Analyze Incident", use_container_width=True):

    if not incident.strip():
        st.warning("Please describe an incident first.")
        st.stop()

    client = create_client()

    try:
        # --------------------------------
        # 1. Recall previous experiences
        # --------------------------------

        with st.spinner("🧠 Searching Hindsight memory..."):

            memory = client.recall(
                bank_id=BANK_ID,
                query=incident,
                max_tokens=3000,
            )

        memories = memory.results[:5]

        st.success("Memory search completed!")

        # --------------------------------
        # 2. Show previous experiences
        # --------------------------------

        st.subheader("🧠 Previous Experience")

        if memories:

            for item in memories:
                st.info(item.text)

        else:
            st.info(
                "No similar incidents found. "
                "This will become a new experience for ZeroTrace."
            )

        # --------------------------------
        # 3. Hindsight AI reasoning
        # --------------------------------

        st.subheader("🤖 ZeroTrace Recommendation")

        with st.spinner("🤖 Learning from previous incidents..."):

            response = client.reflect(
                bank_id=BANK_ID,
                query=f"""
You are ZeroTrace, an AI production incident response agent.

A new incident has occurred:

{incident}

Use the incident history stored in your memory to help respond.

Provide:

1. Severity: LOW, MEDIUM, HIGH, or CRITICAL
2. Likely root cause
3. Immediate actions to take
4. Verification steps
5. Explain how previous incidents influenced your recommendation

If there is no relevant previous experience, clearly say so.

Keep the response practical and concise.
""",
                budget="mid",
            )

        st.markdown(response.text)

        # --------------------------------
        # 4. Store the new incident
        # --------------------------------

        st.divider()

        st.subheader("💾 Record Resolution")

        resolution = st.text_area(
            "What happened after the recommended action?",
            placeholder=(
                "Example: Restarted the backend service. "
                "CPU dropped to 35% and the API recovered."
            ),
            height=100,
        )

        if st.button(
            "🧠 Save Experience to Hindsight",
            use_container_width=True,
        ):

            if not resolution.strip():
                st.warning("Enter the resolution first.")
            else:

                memory_content = f"""
Production Incident:
{incident}

Resolution:
{resolution}

This incident was analyzed by ZeroTrace and stored
as operational experience for future incidents.
"""

                client.retain(
                    bank_id=BANK_ID,
                    content=memory_content,
                    context="ZeroTrace incident response and post-mortem",
                )

                st.success(
                    "🧠 Experience saved! ZeroTrace can use this "
                    "incident when a similar problem happens again."
                )

    except Exception as e:

        st.error(f"ZeroTrace error: {e}")

    finally:

        client.close()


st.divider()

st.caption(
    "🧠 Memory powered by Hindsight • "
    "ZeroTrace Incident Response Agent"
)
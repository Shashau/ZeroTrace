import os
from dotenv import load_dotenv
from hindsight_client import Hindsight

load_dotenv()

client = Hindsight(
    base_url=os.getenv("HINDSIGHT_BASE_URL"),
    api_key=os.getenv("HINDSIGHT_API_KEY"),
)

bank_id = os.getenv("HINDSIGHT_BANK_ID")

print("🧠 Storing incident memory...")

client.retain(
    bank_id=bank_id,
    content="""
    Incident: Production API returned 503 errors.
    Root cause: Backend service crashed because of high CPU usage.
    Resolution: Restarted the backend service and monitored CPU usage.
    """
)

print("✅ Incident stored!")

print("\n🔎 Searching Hindsight memory...")

result = client.recall(
    bank_id=bank_id,
    query="Production API 503 error caused by high CPU usage"
)

print("\n🧠 Hindsight remembered:")

for memory in result.results:
    print("-", memory.text)

client.close()
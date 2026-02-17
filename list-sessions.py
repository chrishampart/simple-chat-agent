import os
import vertexai
from vertexai import agent_engines
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Vertex AI
vertexai.init(
    project=os.getenv("GOOGLE_CLOUD_PROJECT"),
    location=os.getenv("GOOGLE_CLOUD_LOCATION")
)

def list_sessions():
    print("Connecting to 'simple_chat_app'...")
    app_list = agent_engines.list(filter='display_name="simple_chat_app"')
    try:
        engine_resource = next(app_list)
        remote_app = agent_engines.get(engine_resource.resource_name)
    except StopIteration:
        print("Error: Agent 'simple_chat_app' not found.")
        return

    users = ["timing_test_user", "cli_user", "verification_test", "test_user"]
    total_found = 0

    print(f"Agent: {remote_app.resource_name}\n")
    
    for user_id in users:
        print(f"Checking sessions for user '{user_id}'...")
        try:
            sessions = list(remote_app.list_sessions(user_id=user_id))
            print(f"  Count: {len(sessions)}")
            total_found += len(sessions)
            for s in sessions[:3]:
                print(f"  - {s}")
        except Exception as e:
            print(f"  Error for {user_id}: {e}")
        print("-" * 20)

    print(f"\nTotal sessions found across test users: {total_found}")

if __name__ == "__main__":
    list_sessions()

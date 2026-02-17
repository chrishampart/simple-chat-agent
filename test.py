import os
import sys
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

def run_test():
    print("Connecting to 'simple_chat_app'...")
    # Dynamically find the latest deployment
    app_list = list(agent_engines.list(filter='display_name="simple_chat_app"'))
    if not app_list:
        print("Error: Agent 'simple_chat_app' not found.")
        sys.exit(1)
    
    # Sort by create_time (latest first)
    app_list.sort(key=lambda x: x.create_time, reverse=True)
    remote_app = app_list[0]
    print(f"Connected to agent: {remote_app.resource_name}")

    # Start a session and send a query
    user_id = "test_user"
    session = remote_app.create_session(user_id=user_id)
    print(f"Session created: {session['id']}")
    
    print("\nSending query: 'What are your capabilities?'")
    responses = remote_app.stream_query(
        user_id=user_id,
        session_id=session["id"],
        message="What are your capabilities?"
    )

    print("Response: ", end="", flush=True)
    for response in responses:
        content = response.get("content")
        if content:
            parts = content.get("parts")
            if parts:
                for part in parts:
                    if "text" in part:
                        print(part["text"], end="", flush=True)
    print("\n")

if __name__ == "__main__":
    run_test()


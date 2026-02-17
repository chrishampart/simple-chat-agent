import os
import vertexai
from vertexai import agent_engines
from dotenv import load_dotenv

load_dotenv()

vertexai.init(
    project=os.getenv("GOOGLE_CLOUD_PROJECT"),
    location=os.getenv("GOOGLE_CLOUD_LOCATION")
)

def verify():
    print("Finding the deployed agent...")
    app_list = agent_engines.list(filter='display_name="simple_chat_app"')
    try:
        engine_resource = next(app_list)
        print(f"Agent resource found: {engine_resource.resource_name}")
        
        # Use get() to ensure we have the full object
        remote_app = agent_engines.get(engine_resource.resource_name)
        print(f"Full app object retrieved. Methods: {[m for m in dir(remote_app) if not m.startswith('_')]}")
        
    except StopIteration:
        print("Agent 'simple_chat_app' not found.")
        return

    print("Sending a test query via stream_query...")
    try:
        user_id = "verification_test"
        session = remote_app.create_session(user_id=user_id)
        session_id = session["id"]
        
        responses = remote_app.stream_query(
            session_id=session_id,
            message="Hi there! Are you running?",
            user_id=user_id
        )
        print("Response received:")
        print(f"---")
        found_response = False
        for response in responses:
            found_response = True
            print(response, end="", flush=True)
        if not found_response:
            print("[Empty Response]")
        print(f"\n---")
        print("Agent is RUNNING and RESPONSIVE.")
    except Exception as e:
        print(f"Error querying agent: {e}")

if __name__ == "__main__":
    verify()

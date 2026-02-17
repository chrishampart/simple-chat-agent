import os
import time
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

def create_sessions():
    print("Connecting to 'simple_chat_app'...")
    app_list = agent_engines.list(filter='display_name="simple_chat_app"')
    try:
        remote_app = next(app_list)
        print(f"Connected to agent: {remote_app.resource_name}\n")
    except StopIteration:
        print("Error: Agent 'simple_chat_app' not found.")
        return

    user_id = "timing_test_user"
    
    for i in range(1, 10):
        print(f"Iteration {i}: Creating session...")
        start_time = time.perf_counter()
        
        try:
            session = remote_app.create_session(user_id=user_id)
            end_time = time.perf_counter()
            
            duration = end_time - start_time
            print(f"  Session ID: {session['id']}")
            print(f"  Time taken: {duration:.4f} seconds")
        except Exception as e:
            print(f"  Error creating session: {e}")
        
        print("-" * 30)

if __name__ == "__main__":
    create_sessions()

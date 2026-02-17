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

def chat():
    print("Connecting to the latest 'simple_chat_app'...")
    app_list = list(agent_engines.list(filter='display_name="simple_chat_app"'))
    if not app_list:
        print("Error: Agent 'simple_chat_app' not found.")
        sys.exit(1)
    
    # Sort by create_time (latest first)
    app_list.sort(key=lambda x: x.create_time, reverse=True)
    remote_app = app_list[0]
    print(f"Connected to agent: {remote_app.resource_name} (Created: {remote_app.create_time})")

    user_id = "cli_user"
    print("Creating session...")
    session = remote_app.create_session(user_id=user_id)
    session_id = session["id"]
    
    print("\n--- Interactive Chat Started ---")
    print("Type 'exit' or 'quit' to end the conversation.\n")

    while True:
        try:
            user_input = input("You: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["exit", "quit"]:
                print("Goodbye!")
                break

            print("Agent: ", end="", flush=True)
            responses = remote_app.stream_query(
                session_id=session_id,
                message=user_input,
                user_id=user_id
            )
            for response in responses:
                # responses are dictionaries in the newest SDK
                content = response.get("content")
                if content:
                    parts = content.get("parts")
                    if parts:
                        for part in parts:
                            if "text" in part:
                                print(part["text"], end="", flush=True)
            print("\n")

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {e}")

if __name__ == "__main__":
    chat()

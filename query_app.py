import os
import vertexai
from vertexai import agent_engines
from dotenv import load_dotenv

load_dotenv()

vertexai.init(
    project=os.getenv("GOOGLE_CLOUD_PROJECT"),
    location=os.getenv("GOOGLE_CLOUD_LOCATION")
)

# List or get your deployed app
app_list = agent_engines.list(filter='display_name="simple_chat_app"')
remote_app = next(app_list)

# Create a session and query
session = remote_app.create_session(user_id="test_user")
responses = remote_app.stream_query(
    session_id=session["id"],
    message="Hello, who are you?",
    user_id="test_user"
)

for response in responses:
    print(response, end="", flush=True)
print()


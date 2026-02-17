import os
import vertexai
from vertexai import agent_engines
from agent import root_agent
from dotenv import load_dotenv

load_dotenv()

# Initialize Vertex AI
vertexai.init(
    project=os.getenv("GOOGLE_CLOUD_PROJECT"),
    location=os.getenv("GOOGLE_CLOUD_LOCATION", "us-central1"),
    staging_bucket=os.getenv("STAGING_BUCKET")
)

# Deploy to Agent Engine
remote_app = agent_engines.create(
    display_name="simple_chat_app",
    agent_engine=root_agent,
    requirements=["google-adk"]
)

print(f"Deployed Agent Resource Name: {remote_app.resource_name}")


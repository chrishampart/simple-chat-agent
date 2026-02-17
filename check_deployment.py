import os
import vertexai
from vertexai import agent_engines
from dotenv import load_dotenv

load_dotenv()

vertexai.init(
    project=os.getenv("GOOGLE_CLOUD_PROJECT"),
    location=os.getenv("GOOGLE_CLOUD_LOCATION")
)

print(f"Checking for agents in project {os.getenv('GOOGLE_CLOUD_PROJECT')} and location {os.getenv('GOOGLE_CLOUD_LOCATION')}...")

try:
    app_list = agent_engines.list()
    apps = list(app_list)
    if not apps:
        print("No agents found.")
    for app in apps:
        print(f"Found Agent: {app.display_name} ({app.resource_name})")
except Exception as e:
    print(f"Error: {e}")

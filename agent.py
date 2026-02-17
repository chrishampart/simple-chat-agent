from google.adk.agents import Agent
from google.adk.models import Gemini
from dotenv import load_dotenv

load_dotenv()

# Define the model explicitly
gemini_model = Gemini(model="gemini-2.0-flash")

# Define the agent
root_agent = Agent(
    name="simple_chat_agent",
    model=gemini_model,
    description="A simple chat agent.",
    instruction="You are a helpful chatbot.",
)

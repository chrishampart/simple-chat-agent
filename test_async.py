import os
import sys
import asyncio
import vertexai
from vertexai import agent_engines
from dotenv import load_dotenv

load_dotenv()

async def test_async():
    vertexai.init(
        project=os.getenv("GOOGLE_CLOUD_PROJECT"),
        location=os.getenv("GOOGLE_CLOUD_LOCATION")
    )
    
    print("Finding the latest 'simple_chat_app'...")
    app_list = list(agent_engines.list(filter='display_name="simple_chat_app"'))
    if not app_list:
        print("Error: Agent 'simple_chat_app' not found.")
        return
    
    # Sort by create_time (latest first)
    app_list.sort(key=lambda x: x.create_time, reverse=True)
    remote_app = app_list[0]
    print(f"Connected to agent: {remote_app.resource_name}")
    
    user_id = "async_test"
    session = remote_app.create_session(user_id=user_id)
    session_id = session["id"]
    
    print(f"Querying with session {session_id}...")
    try:
        responses = remote_app.async_stream_query(
            session_id=session_id,
            message="Hello, async!",
            user_id=user_id
        )
        found = False
        async for response in responses:
            found = True
            # The structure depends on the ADK version, 
            # similar to the synchronous stream_query in chat.py
            content = response.get("content")
            if content:
                parts = content.get("parts")
                if parts:
                    for part in parts:
                        if "text" in part:
                            print(part["text"], end="", flush=True)
        
        if not found:
            print("No response chunks received from async_stream_query.")
        else:
            print("\nAsync query completed.")
    except Exception as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    asyncio.run(test_async())

# Simple Chat Agent

A basic interactive chatbot built using Google Cloud's Vertex AI Agent Engine and the Vertex AI Agent Development Kit (ADK).

## Features

- **Interactive CLI**: Chat with your agent in real-time.
- **Asynchronous Queries**: Support for async streaming queries.
- **Session Management**: Automated session creation and persistence tracking.
- **Easy Deployment**: Scripts for quick deployment to Vertex AI.

## Setup

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd simple-chat-agent
   ```

2. **Set up a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
   *(Note: Requirements currently include `google-adk`, `google-cloud-aiplatform`, and `python-dotenv`.)*

3. **Configure environment variables**:
   Copy `.env.example` to `.env` and fill in your details:
   ```bash
   cp .env.example .env
   ```
   Modify `.env`:
   - `GOOGLE_CLOUD_PROJECT`: Your GCP Project ID.
   - `GOOGLE_CLOUD_LOCATION`: The location (e.g., `us-central1` or `europe-west2`).

4. **Authentication**:
   Ensure you are authenticated with Google Cloud:
   ```bash
   gcloud auth application-default login
   ```

## Usage

> [!NOTE]
> Ensure your virtual environment is activated before running any scripts:
> `source venv/bin/activate`

### Deployment
To deploy your agent to Vertex AI:
```bash
python deploy.py
```

### Interactive Chat
Start a chat session with the latest deployed agent:
```bash
python chat.py
```

### Testing
Run synchronous or asynchronous tests:
```bash
python test.py
python test_async.py
```

## Project Structure

- `agent.py`: Definition of the agent logic and model configuration.
- `chat.py`: Main CLI interactive chat script.
- `deploy.py`: Deployment script for Vertex AI.
- `test.py` / `test_async.py`: Test scripts for verifying agent functionality.
- `verify_agent.py`: A comprehensive verification tool.

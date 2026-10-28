# AI Phishing Message Analyzer

A beginner-friendly prompt engineering project using Python, Flask, an LLM SDK, JSON, and validation.

## Flow
Message input → Prompt + LLM SDK → JSON → Python validation → Safety report

## Run on Windows
1. Extract the ZIP and open the folder in VS Code.
2. Open Terminal.
3. Create a virtual environment:
   `python -m venv venv`
4. Activate it:
   `venv\Scripts\activate`
5. Install dependencies:
   `pip install -r requirements.txt`
6. Run:
   `python app.py`
7. Open `http://127.0.0.1:5000`

## Test message
Your bank account is blocked. Click this link immediately to verify your password and claim your reward.

## Enable actual LLM analysis (optional)
1. Copy `.env.example` to `.env`.
2. Get a Groq API key from the official Groq developer console if available to you.
3. Set `GROQ_API_KEY=your_key_here` in `.env`.
4. Restart the app.

Keep API keys private. Do not upload `.env` to GitHub.

## Prompt engineering
The prompt gives the model a role, defines the analysis task, lists indicators to look for, treats the supplied message as untrusted data, and requires a fixed JSON schema.

## Limitations
Without a key, the application uses simple keyword rules, not an LLM. With an LLM, results can still be incorrect. Do not treat the assessment as a guarantee that a message is safe or fraudulent. Never paste real passwords, one-time codes, or financial details.

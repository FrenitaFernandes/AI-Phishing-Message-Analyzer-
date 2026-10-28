
from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("ERROR: API key not found.")
else:
    try:
        client = Groq(api_key=api_key)

        response = client.chat.completions.create(
            model="%pip install -U transformers langchain-huggingface langchain-core langchain-groqopenai/gpt-oss-120b",
            messages=[
                {
                    "role": "user",
                    "content": "Reply with exactly: Groq is working"
                }
            ],
            temperature=0
        )

        print("SUCCESS: Groq API is working!")
        print(response.choices[0].message.content)

    except Exception as e:
        print("Groq API request failed.")
        print("Error type:", type(e).__name__)
        print("Error details:", str(e).replace(api_key, "[HIDDEN]"))

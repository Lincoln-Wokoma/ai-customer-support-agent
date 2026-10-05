from src.memory.memory import format_history
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

def generate_response(sessionID, question, context):

    prompt = f"""
You are a helpful customer support agent.

Answer the customer's question using only the information provided
in the context below.

If the answer cannot be found in the context, say that you don't
have enough information and recommend contacting customer support.

History:
{format_history(sessionID)}

Context:
{context}

Customer question:
{question}
"""

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    interaction = client.interactions.create(
        model="gemini-3.5-flash",
        input=prompt
    )

    return interaction.output_text

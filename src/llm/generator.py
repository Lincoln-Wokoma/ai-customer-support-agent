from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client()

MODEL_NAME = "gemini-3.8-flash"


def generate_response(question, context):

    prompt = f"""
You are a helpful customer support agent.

Answer the customer's question using only the information provided
in the context below.

If the answer cannot be found in the context, say that you don't
have enough information and recommend contacting customer support.

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

question = "Can I return a laptop after 5 days?"

context = """
Customers can request a return within 7 days of receiving an item.
The item must be unused and in its original packaging.
Some products may not be eligible for return because of hygiene
or safety restrictions.
"""


response = generate_response(question, context)

print(response)
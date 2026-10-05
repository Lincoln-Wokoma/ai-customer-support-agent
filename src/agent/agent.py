from src.retrieval.search import search
from src.llm.generator import generate_response
from src.memory.memory import add_message


def answer_question(question, model, index, chunks):

    sessionID = "S001"

    add_message(sessionID,"customer", question)

    results = search(question, model, index, chunks)

    context = "\n\n".join(results)

    response = generate_response(sessionID, question, context)

    add_message(sessionID, "agent", response)
    
    return response
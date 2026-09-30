from src.retrieval.search import search
from src.llm.generator import generate_response


def answer_question(question, model, index, chunks):

    results = search(question, model, index, chunks)

    context = "\n\n".join(results)

    return generate_response(question, context)
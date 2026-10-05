from src.retrieval.loader import load_document
from src.retrieval.chunker import split_text
from src.retrieval.embedding import create_embeddings, model
from src.retrieval.vector_store import create_vector_store
from src.agent.agent import answer_question
from src.memory.memory import get_history


file_path = "data/knowledge_base/support_faq.txt"

document = load_document(file_path)

chunks = split_text(document)

embeddings = create_embeddings(chunks)

index = create_vector_store(embeddings)


question = input("Enter a question: ")

answer = answer_question(question, model, index, chunks)

print("\nCustomer:", question)
print("\nAgent:", answer)
print("\nHistory", get_history("S001"))
from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_text(document, chunk_size = 200, chunk_overlap = 10):
    splitter = RecursiveCharacterTextSplitter(chunk_size = chunk_size, chunk_overlap = chunk_overlap)
    return splitter.split_text(document)


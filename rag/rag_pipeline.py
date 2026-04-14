from rag.document_loader import load_sec_document
from rag.vector_store import create_vector_store


def query_sec_rag(cik, question):

    document = load_sec_document(cik)

    vector_db = create_vector_store(document)

    retriever = vector_db.as_retriever()

    docs = retriever.invoke(question)

    if not docs:
        return "No relevant SEC information found."

    context = "\n".join([doc.page_content for doc in docs])

    return context
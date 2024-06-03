from langchain.storage import InMemoryByteStore
from langchain.tools.retriever import create_retriever_tool
from langchain_qdrant import Qdrant

from ext.qdrant_client import embedding_function, qdrant_client

vectorstore_summaries = Qdrant(
    client=qdrant_client, collection_name="summaries-tgs", embeddings=embedding_function
)

vectorstore_questions = Qdrant(
    client=qdrant_client,
    collection_name="hypothetical-question-tgs",
    embeddings=embedding_function,
)

id_key = "doc_id"

store = InMemoryByteStore()


retriever_summaries = vectorstore_summaries.as_retriever()
retriever_questions = vectorstore_questions.as_retriever()

retriever_tool_summaries = create_retriever_tool(
    retriever_summaries,
    "therapeutic_guidelines_smoking_summaries",
    "This tool provides a concise summary of the 'Protocolo Clínico e Diretrizes Terapêuticas do Tabagismo' document. The summary includes key points, major guidelines, and critical information related to the diagnosis, treatment, and management of tobacco addiction as described in the clinical protocol.",
)

retriever_tool_questions = create_retriever_tool(
    retriever_questions,
    "therapeutic_guidelines_smoking_questions_and_answer",
    "This tool generates example questions based on the contents of the 'Protocolo Clínico e Diretrizes Terapêuticas do Tabagismo' document. These questions can be used for educational purposes, training, or to facilitate discussions around the guidelines and protocols described in the document.",
)


tools = [retriever_tool_summaries, retriever_tool_questions]

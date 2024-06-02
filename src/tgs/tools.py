from langchain.tools.retriever import create_retriever_tool
from langchain_qdrant import Qdrant

from ext.qdrant_client import embedding_function, qdrant_client

vectorstore = Qdrant(
    client=qdrant_client, collection_name="summaries-tgs", embeddings=embedding_function
)

id_key = "doc_id"

# The retriever (empty to start)
# retriever = MultiVectorRetriever(
#     vectorstore=vectorstore,
#     byte_store=store,
#     id_key=id_key,
# )

# retriever = vectorstore.as_retriever(
#     search_type="similarity_score_threshold", search_kwargs={"score_threshold": 0.5}
# )

retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 5, "lambda_mult": 0.25, "fetch_k": 50},
)

retriever_tool = create_retriever_tool(
    retriever,
    "therapeutic_guidelines_smoking",
    "The Ministry of Health, through the Secretariat of Specialized Health Care and the Secretariat of Science, Technology, Innovation, and Strategic Inputs in Health, has approved the Clinical Protocol and Therapeutic Guidelines for Smoking. This ordinance updates the national parameters for diagnosing, treating, and following up on smoking-related health issues in Brazil. The protocol, available on the Ministry of Health’s website, includes diagnostic criteria, treatment options, and guidelines for health professionals. It mandates the informed consent of patients regarding potential risks and side effects and requires SUS managers to structure and coordinate the healthcare network for effective treatment of smoking",
)

tools = [retriever_tool]

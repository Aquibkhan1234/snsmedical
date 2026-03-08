import os
from dotenv import load_dotenv
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

PINECONE_INDEX_NAME = "medicalindex"

def get_retriever():
    embeddings = GoogleGenerativeAIEmbeddings(
        model ="models/gemini-embedding-001"
    )

    pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
    index=pc.Index(PINECONE_INDEX_NAME)

    vectorstore = PineconeVectorStore(
        index=index,
        embedding=embeddings
    )
    retriever = vectorstore.as_retriever(
        search_kwargs={"k":4}
    )
    return retriever


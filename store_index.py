from dotenv import load_dotenv
import os
from src.helper import load_pdf_file, filter_to_minimal_docs, text_split, download_hugging_face_embeddings
from src.config import require_env
from pinecone import Pinecone
from pinecone import ServerlessSpec 
from langchain_pinecone import PineconeVectorStore

load_dotenv()

PINECONE_API_KEY = require_env("PINECONE_API_KEY")
MISTRAL_API_KEY = require_env("MISTRAL_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["MISTRAL_API_KEY"] = MISTRAL_API_KEY


extracted_data = load_pdf_file(data='data/')
print("Total documents:", len(extracted_data))

for i, doc in enumerate(extracted_data[:10]):
    print(i, "length:", len(doc.page_content))

print("Documents loaded:", len(extracted_data))
print("First document content length:", len(extracted_data[0].page_content))
print("First document preview:", extracted_data[0].page_content[:200])

filter_data = filter_to_minimal_docs(extracted_data)

print("Documents after filtering:", len(filter_data))

non_empty_docs = [
    doc for doc in extracted_data
    if doc.page_content and doc.page_content.strip()
]

print("Non-empty documents:", len(non_empty_docs))

if non_empty_docs:
    print("First non-empty content length:", len(non_empty_docs[0].page_content))
    print("First non-empty preview:", non_empty_docs[0].page_content[:200])

text_chunks = text_split(non_empty_docs)

print("Total chunks:", len(text_chunks))
embeddings = download_hugging_face_embeddings()

pc = Pinecone(api_key=PINECONE_API_KEY)

index_name = "medicalbot"

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings
)

print("Upload process completed")
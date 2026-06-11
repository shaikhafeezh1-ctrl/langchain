from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv


load_dotenv()

embedding=OpenAIEmbeddings(model="text-embedding-3-large",dimensions=32)

doc=[
    "Delhi is the captial of india",
    "Mumbai is the Financial captial of india",
    "Paris is the captial of France"
]

result=embedding.embed_documents(doc)

print(str(result))
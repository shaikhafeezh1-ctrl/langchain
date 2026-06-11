from langchain_community.document_loaders import WebBaseLoader

url="https://medium.com/@amandaberman09/when-museums-go-silent-erasure-speaks-louder-908326fa06b2"
loader= WebBaseLoader(url)

docs=loader.load()

print(docs)
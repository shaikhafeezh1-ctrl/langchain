from langchain_community.document_loaders import DirectoryLoader , PyPDFLoader


loader= DirectoryLoader(
    path="Books",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

docs=loader.load()

print(docs)
print(len(docs))

print(docs[355].page_content)
print(docs[355].metadata)
from langchain_community.chat_models import HuggingFaceHub

# Initialize the model
model = HuggingFaceHub(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0"
)

# Run a simple query
response = model.invoke("Hello TinyLlama, how are you?")
print(response)


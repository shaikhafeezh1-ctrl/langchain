from google import genai

client = genai.Client()
models = client.models.list()
for m in models:
    # Access supported methods safely — some Model objects may not have this attribute.
    supported = getattr(m, "supported_methods", None) or getattr(m, "supportedMethods", None)
    print(m.name, supported)

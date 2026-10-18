from groq import Groq

client = Groq(api_key="GRQO_API_KEY")

models = client.models.list()

for model in models.data:
    print(model.id)
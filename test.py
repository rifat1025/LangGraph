from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

print("API Key Found:", GROQ_API_KEY is not None)

client = Groq(api_key=GROQ_API_KEY)

models = client.models.list()

for model in models.data:
    print(model.id)
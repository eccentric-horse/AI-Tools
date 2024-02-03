import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
models = openai.models.list().data
for model in models:
    print(model.id)
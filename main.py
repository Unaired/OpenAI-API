import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = "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"

models = openai.Model.list()
print(models.data[0].id)
chat_completion = openai.ChatCompletion.create(model="gpt-4", messages=[
    {"role": "user", "content": "Hello worl"}
    
])




while True:
    print(chat_completion.choices[0].message.content)
    
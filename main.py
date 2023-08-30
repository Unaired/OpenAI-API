import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = "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"

models = openai.Model.list()
print(models.data[0].id)

messages=[

    {"role": "system", "content": "You are a helpful assistant"},
       
]
 
user_wants_to_continue = True

while user_wants_to_continue == True:

    user_input = input()

    if user_input != "":
        user_wants_to_continue = True

    else: user_wants_to_continue = False

    messages.append({"role": "user", "content": user_input})
    chat_completion = openai.ChatCompletion.create(model="gpt-4", messages = messages)
    assistant_response = chat_completion.choices[0].message.content
    messages.append({"role": "assistant", "content": assistant_response})
    print(assistant_response)



    




    
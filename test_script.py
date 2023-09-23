import os
import fakeopenai as openai

# Set API key
openai.api_key = "pk-this-is-a-real-free-pool-token-for-everyone"

# Usage
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a joke with 1000 words."},
    ]
)

assistant_reply = response['choices'][0]['message']
print("Assistant:", assistant_reply)

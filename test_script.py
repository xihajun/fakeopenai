import fakeopenai
import os

FAKEOPENAI_KEY = os.environ.get("FAKEOPENAI_KEY")

fakeopenai.set_api_key(FAKEOPENAI_KEY)

response = fakeopenai.ChatCompletion_create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a joke with 1000 words."},
    ]
)

assistant_reply = response['choices'][0]['message']['content']
print("Assistant:", assistant_reply)
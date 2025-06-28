#todo:ADD your API Key here

import openai
from config import apikey

client = openai.OpenAI(api_key=apikey)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",  # or "gpt-4"
    messages=[
        {"role": "user", "content": "Write an email to my boss for resignation"}
    ],
    temperature=0.7,
    max_tokens=256
)

print(response.choices[0].message.content)

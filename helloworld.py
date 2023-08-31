import openai
import json

with open('.env.json') as f:
    data = json.load(f)
    api_key = data['API_KEY']

# Load your API key from an environment variable or secret management service
openai.api_key = api_key

chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(chat_completion)
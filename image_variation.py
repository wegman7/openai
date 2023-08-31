import openai
import json
import webbrowser

with open('.env.json') as f:
    data = json.load(f)
    api_key = data['API_KEY']

# Load your API key from an environment variable or secret management service
openai.api_key = api_key

response = openai.Image.create_variation(
  image=open("/Users/jw085395/downloads/profile_pic.png", "rb"),
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']

webbrowser.open(image_url)
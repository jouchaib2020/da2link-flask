import openai
import os
from dotenv import load_dotenv

# Load variables from .env file into environment
load_dotenv()

# Set your API key
openai.api_key = os.environ.get('API_KEY')

# Define a function to get a response from ChatGPT
def get_response(prompt):
  messages = [
    {"role": "user", "content": "What is 1+1"},
    {"role": "user", "content": prompt}
    ]
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
    temperature=0.7,
  )
  return response.choices[0].message["content"]

# Get a response from ChatGPT
prompt = "what was my last question"
response = get_response(prompt)

# Print the response
print(response)

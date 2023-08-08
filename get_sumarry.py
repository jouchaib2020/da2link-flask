import openai
import os
from dotenv import load_dotenv

# Load variables from .env file into environment
load_dotenv()

# Set your API key
openai.api_key = os.environ.get('API_KEY')

# Define a function to get a response from ChatGPT
def get_response(prompt):
  messages = [{"role": "user", "content": prompt}]
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
    temperature=0.7,
  )
  return response.choices[0].message["content"]

# Get a response from ChatGPT
prompt = "What is 1+1"
response_1 = get_response(prompt)
response = get_response("what was my last question")

# Print the response
print(response)

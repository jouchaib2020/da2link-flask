import openai
import os
from dotenv import load_dotenv
from messages import messages

# Load variables from .env file into environment
load_dotenv()

# Set your API key
openai.api_key = os.environ.get('API_KEY')

# Define a function to get a response from ChatGPT

def get_response(prompt):
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages(prompt),
    temperature=0.7,
  )
  return response.choices[0].message["content"]

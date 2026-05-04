import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

MODEL_NAME = "gpt-4.1-mini"

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
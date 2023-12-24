"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Text-to-Speech
==============

"""
# Substitua sua chave de API OpenAI:
import openai
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key  = os.environ['OPENAI_API_KEY']

from transformers import pipeline
from datasets import load_dataset


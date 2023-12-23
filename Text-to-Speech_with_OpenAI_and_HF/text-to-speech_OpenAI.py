"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Text-to-Speech
==============
O speech endpoint recebe três entradas principais: o modelo,
o texto que deve ser transformado em áudio e a voz a ser usada
para a geração do áudio. Uma solicitação simples seria semelhante a este script.


Links de estudo:

* https://platform.openai.com/docs/guides/text-to-speech

* https://platform.openai.com/docs/models/tts
"""
# Substitua sua chave de API OpenAI:
import openai
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key  = os.environ['OPENAI_API_KEY']


from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv


client = OpenAI()

speech_file_path = Path(__file__).parent / "speech.mp3"

response = client.audio.speech.create(
    model="tts-1", # ou "tts-1-hd"
    voice="alloy",
    input="Olá, sou Eddy Giusepe e sou Cientista de Dados"
)

response.stream_to_file(speech_file_path)

import os
from dotenv import load_dotenv
load_dotenv()


from ast import Await
import discord
import random

TOKEN = os.getenv('api_key')


client = discord.Client()

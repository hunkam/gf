
import os
from dotenv import load_dotenv
load_dotenv()


from ast import Await
import discord
import random

TOKEN = os.getenv('api_key')


client = discord.Client()

#when bot is ready
@client.event
async def on_ready():
    print("we have logged in as {0.user}".format(client))



#triggers on discord message
@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')


    if message.author == client.user:
        return

#triggers by typing in discord chat when bot is in server
    if user_message.lower() == "hello":
        await message.channel.send(f'eyy boss {username}')
        return
    elif user_message.lower() == "waifu":
        await message.channel.send(f'consider touching grass {username}')
        return
    elif user_message.lower() == "bye":
        await message.channel.send(f'see you later {username}')
    elif user_message.lower() == "i love you":
        await message.channel.send(f'no bitches {username}?')
        return
    elif user_message.lower() == "hey":
        await message.channel.send(f'i love you {username}')
        return


client.run(TOKEN)



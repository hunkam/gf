"""hey & thanks for taking the time to look at this code, this is a script interacting with the discord.py
module to read discord messages and repsond accordingly. 
 oh also how can I hide my private token (i tried assigning it to a variable in a seperate file that id
 have git ignore but that would't work right...)"""

from ast import Await
import discord
import random

TOKEN = 'OTU0NDQ2NDMxOTEyMDk5OTIx.YjTPgg.2izuYFNEKoSpufW1TJI2H0XefFA'
# ^^DISCORD bot token^^pls not steal

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
        await message.channel.send(f'see you later{username}')
        return


client.run(TOKEN)



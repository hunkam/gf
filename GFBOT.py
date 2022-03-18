import discord
import random

TOKEN = 'OTU0NDQ2NDMxOTEyMDk5OTIx.YjTPgg.PhgLwZyTnyALEzUeqSTN3R914tg'
# ^^DISCORD bot token^^pls not steal

client = discord.Client()

@client.event
async def on_ready():
    print("we have logged in as {0.user}".format(client))

    client.run(TOKEN)
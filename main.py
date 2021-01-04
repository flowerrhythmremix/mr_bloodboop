import discord
import os
import random

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('!choose'):
      choices = message.content.split()[1:]

      result = random.choice(choices)
      await message.channel.send(result)

client.run(os.getenv('TOKEN'))
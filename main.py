import discord
import requests
import json
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

    if message.content.startswith('%'):
      ticker = message.content[1:].upper()
      url = "https://min-api.cryptocompare.com/data/price"
      headers = {
        'Content-type': 'application/json',
        'Authorization': os.getenv('CRYPTOCOMPARE_KEY')
      }
      payload = { 'fsym': ticker, 'tsyms': 'USD' }

      request = requests.get(url, params=payload, headers=headers)

      if ticker == 'DOGE':
        ticker = ':doge:'

      await message.channel.send("CRYPTO: " + ticker + " is currently trading at $" + str(request.json()['USD']))
      
client.run(os.getenv('TOKEN'))
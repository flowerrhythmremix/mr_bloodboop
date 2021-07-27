import discord
import requests
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
        ticker = '<:doge:804544921955467275>'

      await message.channel.send("CRYPTO: " + ticker + " is currently trading at $" + str(request.json()['USD']))

    if message.content.startswith('$'):
      ticker = message.content[1:].upper()

      url = "https://www.alphavantage.co/query"

      payload = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': ticker,
        'interval': '1min',
        'apikey': os.getenv('ALPHA_VANTAGE_KEY')
      }

      request = requests.get(url, params=payload)

      response = request.json()['Time Series (1min)']
      for key, value in response.items():
        price = value['4. close']
        break

      await message.channel.send("STONK: " + ticker + " is currently trading at $" + str(price))

    if 'twitter' in message.content()
      await message.content.replace('twitter', 'fxtwitter')
      
client.run(os.getenv('TOKEN'))
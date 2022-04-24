"""
Discord Bot that retrieves realtime price of whatever cryptocurrency you input.

"""

# Bot STUFF 
from ast import Global
from cmath import e
import requests
from requests import Request, Session 
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import os
import json
import pprint 
import discord 
intents = discord.Intents.all()
bot = discord.Client(intents = intents)
key=os.environ.get('COINMARKETCAP_API_KEY')


@bot.event
async def on_ready():
    print("Mr. Bot is online")
    
crypto = input("Please enter a cryptocurrency symbol: ")    
@bot.event
async def on_message(msg):
    username = msg.author.display_name
    if msg.author == bot.user:
        return
    else:
         if msg.content == "hello" or "hi" or "what's up":
                await msg.channel.send("hello " + username)
         
    if msg.content == "check price":
        

                price_now = get_price()
                await msg.channel.send(price_now)
        
         
                
 # API CALL STUFF              

parameters = {
'symbol': f"{crypto}" # Needs to be variable of input recieved from bot
} 

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'key',
  'aux': 'is_active',
}

url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

session = Session()
session.headers.update(headers)

def get_price():
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        return "This is the current price: " + str(data['data'][crypto.upper()]['quote']['USD']['price'])
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      return e 
      
     
bot.run('OTYxNzIxMTg5NjgyNzc4MTUy.Yk9Gpw.hP_XxTBke6hPwwpXFiCSCHAVmRc')
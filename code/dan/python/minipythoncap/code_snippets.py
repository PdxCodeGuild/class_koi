@bot.event
async def on_message(msg):
    if msg.content == "check price":
        await msg.channel.send(crypto = input("Please enter a cryptocurrency symbol"))
    
        price_now = check_price()
        await message.channel.send(price_now)
        
        
        
        
        parameters = {
'symbol': f"{cr}"
} 


headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'key',
  'aux': 'is_active',
}





url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

def get_price():
    session = Session()
    session.headers.update(headers)
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        pprint.pprint(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print (e)

   

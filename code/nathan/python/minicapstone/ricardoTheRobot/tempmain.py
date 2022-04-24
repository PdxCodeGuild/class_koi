import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('Log in successful {0.user}'.format(client))


@client.event
async def on_message(message):
    if(message.author == client.user):
        return
    
    if(message.content.startswith('!challenge')):
        await message.channel.send("A list")
    
# client.run('OTU2NzkyMzUxNjA5NzI0OTc4.Yj1YUA.ebWuq82CNkFWINz-YrHpxOud5cI')
client.logout()

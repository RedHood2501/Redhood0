import os

import discord

client = discord.Client()

@client.event

async def on_ready():

  print('nuke bot it ready to go!')

  

@client.event

async def on_message(message):

If (message.content.startswith('nuke')):

await message.guild_create_text_channel('nuked kid')



  client.run(os.getenv("TOKEN")

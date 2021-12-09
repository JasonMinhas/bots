import discord
import os

thotbot_token = os.getenv('thotbot_token')
guild_name = os.getenv('matts_guild')

client = discord.Client()

@client.event
async def on_ready():
  channel = client.get_channel(741478408575385704)
  await channel.send("Use the command '$[name]_fact' to get a fun fact about someone.")

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content


client.run(thotbot_token)
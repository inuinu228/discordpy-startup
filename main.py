import discord

client = discord.Client()

@client.event
async def on_ready():
  print("logged in as " + client.user.name)

@client.event
async def on_message(message):
  if message.author != client.user:
    msg = message.author.mention + " おう "
    await client.send_message(message.channel, msg)

client.run("NjA5MzEzODc1MTI0Mjg5NTM3.XU1umQ.LYxgttlsUlwIAGKosB0fzrCnuD8")

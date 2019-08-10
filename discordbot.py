from discord.ext import commands
import os
import traceback
import discord

client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_message(message):
    # 「やあ」というチャットが来た場合のメッセージ
    if message.content.startswith("やあ"):
        # 送り主がチャットボット以外なら返事を返す
        if client.user != message.author:
            message = "やあ、" + message.author.name
            await client.send_message(message.channel, message)

client.run(token) 

from discord.ext 
import discord
import commands
import os
import traceback

client = discord.Client()
bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
@client.event
async def on_message(message):
    # 「おはよう」で始まるか調べる
    if message.content.startswith("おはよう"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            m = "おはようございます" + message.author.name + "さん！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def na(ctx):
    await ctx.send('おう')
    
client.run(token)    
bot.run(token)

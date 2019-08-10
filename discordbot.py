from discord.ext import commands
import os
import traceback
import discord

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
    # 「やあ」というチャットが来た場合のメッセージ
    if message.content.startswith("やあ"):
        # 送り主がチャットボット以外なら返事を返す
        if client.user != message.author:
            message = "やあ、" + message.author.name
            await client.send_message(message.channel, message)
            
client.run(token)

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))
    
@bot.command()
async def na(ctx):
    await ctx.send('おう')
    
@bot.command()
async def ayamare(ctx):
    await ctx.send('全部俺がわり')
    
@bot.command()
async def edpi(ctx, a: float, b: float):
    await ctx.send('お前のEDPIは %d や \n わかったか？' % (round(a*b)))
    
@bot.command()
async def furimuki(ctx, c: float, d: float):
    await ctx.send('お前の振り向きは %.1f cmや \n わかったか？' % (round(2.54*180/(c*0.55550*d),1)))
         
bot.run(token)

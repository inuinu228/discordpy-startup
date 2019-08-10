from discord.ext import commands
import os
import traceback
import discord
import random

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))
    
@bot.command(name="なあ")
async def na(ctx):
    await ctx.send('おう')
    
@bot.command(name="謝れ")
async def ayamare(ctx):
    await ctx.send('全部俺がわり')
    
@bot.command()
async def edpi(ctx, a: float, b: float):
    await ctx.send('お前のEDPIは %d や \n わかったか？' % (round(a*b)))
    
@bot.command(name="振り向き")
async def furimuki(ctx, c: float, d: float):
    await ctx.send('お前の振り向きは %.1f cmや \n わかったか？' % (round(2.54*180/(c*0.55550*d),1)))
    
@bot.command()
async def list(ctx):
    await ctx.send('/na 俺が同意するぞ \n /ayamare 俺が謝るぞ \n /edpi DPIと感度を教えると俺がEDPIを計算するぞ \n /furimuki DPIと感度を教えると俺が振り向きを測るぞ')
            
bot.run(token)    
client.run(token) 

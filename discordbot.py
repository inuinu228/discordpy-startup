from discord.ext import commands
import os
import traceback
import discord

bot = commands.Bot(command_prefix='/')
bot = remove_command('help')
token = os.environ['DISCORD_BOT_TOKEN']

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
    
@bot.command()
async def help(ctx):
    await ctx.send('na 俺が同意するぞ \n ayamare 俺が謝るぞ \n edpi 俺がお前のEDPIを教えるぞ \n furimuki 俺がお前の振り向きを教えるぞ')
     
bot.run(token)

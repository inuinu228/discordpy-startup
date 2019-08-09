from discord.ext import commands
import os
import traceback
import discord

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))
    
@bot.command()
async def na(ctx):
    await ctx.send('おう')
    
@bot.command()
async def hey(ctx):
    await ctx.send('なんや！！！')
    
@bot.command()
async def oum(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def kakezan(ctx, a: float, b: float):
    await ctx.send(round(a*b))
    
@bot.command()
async def edpi(ctx, a: float, b: float):
    await ctx.send('お前のEDPIは %d や \n わかったか？' % (round(a*b)))
    
@bot.command()
async def 180(ctx, a: float, b: float):
    await ctx.send('お前の振り向きは %d cmや \n わかったか？' % ((round(2.54 * 360 / (a * 0.55550 * b)))/2)

bot.run(token)

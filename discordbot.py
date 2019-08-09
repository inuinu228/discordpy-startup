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
async def oum(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def kakezan(ctx, a: int, b: int):
    await ctx.send(a*b)
    
@bot.command()
async def edpi(ctx, a: float, b: float):
    await ctx.send('お前のEDPIはround(a*b)や')
    
bot.run(token)

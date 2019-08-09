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
async def edpi(ctx, a: float, b: float):
    await ctx.send('お前のEDPIは %d や \n わかったか？' % (round(a*b)))
    
@bot.command()
async def zenshu(ctx, a: float, b: float):
    await ctx.send('お前の全周は %d cmや \n わかったか？' % (2.54 * 360 / (a * 0.55550 * b))
    
bot.run(token)

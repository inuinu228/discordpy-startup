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
async def edpi(ctx, a: int, b: int):
    await ctx.send("お前のEDPIはa*bや")
    
bot.run(token)

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
async def hey(ctx):
    await ctx.send('なんや！！！')

bot.run(token)

from discord.ext import commands
import os
import traceback
import discord


bot = commands.Bot(command_prefix='/')
client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def na(ctx):
    await ctx.send('おう')

bot.run(token)

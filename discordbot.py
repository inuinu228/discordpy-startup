from discord.ext 
import discord
import commands
import os
import traceback

client = discord.Client()
bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def na(ctx):
    await ctx.send('おう')
    
client.run(token)    
bot.run(token)

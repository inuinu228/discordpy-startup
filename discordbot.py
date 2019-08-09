from discord.ext import commands
import os
import traceback
import discord


token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))
    
@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

bot.run(token)

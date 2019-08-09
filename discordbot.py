from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.event
async def on_message(message):
    if message.content.startswith("なあゆうどう"):
        if client.user != message.author:
            m = "おう"
            await message.channel.send(m)
    
bot.run(token)

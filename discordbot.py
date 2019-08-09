from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def なあゆうどう(ctx):
    await ctx.send('おう')
    
@bot.command()
async def おい(ctx):
    await ctx.send('なんや！！！')
    
@bot.command()
async def あやまれ(ctx):
    await ctx.send('ごめんな')
      await ctx.send('全部俺がわり')

bot.run(token)

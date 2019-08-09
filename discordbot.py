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
    # 「おはよう」で始まるか調べる
    if message.content.startswith("なあゆうどう"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            m = "おう"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)
    
bot.run(token)

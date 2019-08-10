from discord.ext import commands
import os
import traceback
import discord
import random

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
discord_voice_channel_id = 'チャンネル１'
youtube_url = 'https://www.youtube.com/watch?v=QBP8imm03Mo'
client = discord.Client()

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))
    
@bot.command()
async def na(ctx):
    await ctx.send('おう')
    
@bot.command()
async def hey(ctx):
    await ctx.send('なんや！！！')
    
@bot.command()
async def ayamare(ctx):
    await ctx.send('全部俺がわり')
    
@bot.command()
async def edpi(ctx, a: float, b: float):
    await ctx.send('お前のEDPIは %d や \n わかったか？' % (round(a*b)))
    
@bot.command()
async def furimuki(ctx, c: float, d: float):
    await ctx.send('お前の振り向きは %.1f cmや \n わかったか？' % (round(2.54*180/(c*0.55550*d),1)))
    
bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Yudo bot", description="上野裕道の脳みそを搭載したロボット", color=0xeee657)

    embed.add_field(name="/na", value="俺が同意してやるぞ", inline=False)
    embed.add_field(name="/hey",　value="俺が返事してやるぞ", inline=False)
    embed.add_field(name="/ayamare", value="俺が謝ってやるぞ", inline=False)
    embed.add_field(name="/edpi", value="DPIと感度を教えると俺がEDPIを計算してやるぞ", inline=False)
    embed.add_field(name="/furimuki", value="DPIと感度を教えると俺が振り向きを測ってやるぞ", inline=False)
    embed.add_field(name="/help", value="俺がどんなことするか教えてやるぞ", inline=False)

    await ctx.send(embed=embed)
            
bot.run(token)    
client.run(token) 

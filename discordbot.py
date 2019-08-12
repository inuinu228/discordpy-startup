from discord.ext import commands
import os
import traceback
import discord
import random

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
discord_voice_channel_id = 'チャンネル１'
youtube_url = 'https://www.youtube.com/watch?v=t9KON71nlqw'
saikoro = range(1,7)
client = discord.Client()

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))
    
@bot.command()
async def na(ctx):
    await ctx.send('おう')
    
@bot.command()
async def ayamare(ctx):
    await ctx.send('全部俺がわり')
    
@bot.command()
async def hey(ctx):
    await ctx.send('なんや！！！')
    
@bot.command()
async def youtube(ctx):
    await ctx.send(youtube_url)
    
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
    embed.add_field(name="/ayamare", value="俺が謝ってやるぞ", inline=False)
    embed.add_field(name="/hey", value="俺があいさつ返してやるぞ", inline=False)
    embed.add_field(name="/dice", value="サイコロを振ってやるぞ", inline=False)
    embed.add_field(name="/edpi", value="DPIと感度を教えると俺がEDPIを計算してやるぞ", inline=False)
    embed.add_field(name="/furimuki", value="DPIと感度を教えると俺が振り向きを測ってやるぞ", inline=False)
    embed.add_field(name="/takayama", value="高山の情報を教えるぞ", inline=False)
    embed.add_field(name="/help", value="俺がどんなことするか教えてやるぞ", inline=False)

    await ctx.send(embed=embed)
    
@bot.command()
async def takayama(ctx):
    embed = discord.Embed(title="高山", description="a.k.a 駆け出しチクニー少年", color=0xeee657)

    embed.add_field(name="MOUSE", value="LOGICOOL G502", inline=False)
    embed.add_field(name="DPI", value="1000", inline=False)
    embed.add_field(name="Mouse Sensitivity X", value="0.112", inline=False)
    embed.add_field(name="Mouse Sensitivity Y", value="0.112", inline=False)
    embed.add_field(name="Mouse Targeting Sensitivity", value="0.450", inline=False)
    embed.add_field(name="Mouse Scope Sensitivity", value="0.700", inline=False)
    embed.add_field(name="Monitor", value="Acer KG251QIbmiipx 24.5", inline=False)
    embed.add_field(name="GPU", value="GTX 1070", inline=False)
    embed.add_field(name="Mousepad", value="Steelseries Qck Heavy", inline=False)
    embed.add_field(name="Keyboard", value="HyperX Alloy FPS Pro", inline=False)
    embed.add_field(name="Headset", value="Steelseries Arctis5 2017", inline=False)
    
    await ctx.send(embed=embed)

            
bot.run(token)    
client.run(token) 

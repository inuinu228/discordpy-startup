from discord.ext import commands
import os
import traceback
import discord
import random

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
discord_voice_channel_id = 'チャンネル１'
youtube_url = 'https://www.youtube.com/watch?v=t9KON71nlqw'
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
    embed.add_field(name="/edpi", value="DPIと感度を教えると俺がEDPIを計算してやるぞ", inline=False)
    embed.add_field(name="/furimuki", value="DPIと感度を教えると俺が振り向きを測ってやるぞ", inline=False)
    embed.add_field(name="/takayama", value="高山の情報を教えるぞ", inline=False)
    embed.add_field(name="/tokimatsu", value="時松の情報を教えるぞ", inline=False)
    embed.add_field(name="/ushi", value="牛島の情報を教えるぞ", inline=False)
    embed.add_field(name="/haruki", value="はるきの情報を教えるぞ", inline=False)
    embed.add_field(name="/help", value="俺がどんなことするか教えてやるぞ", inline=False)

    await ctx.send(embed=embed)
    
@bot.command()
async def takayama(ctx):
    embed = discord.Embed(title="高山", description="a.k.a 駆け出しチクニー少年", color=0x00ff00)

    embed.add_field(name="MOUSE", value="Logicool G502h", inline=False)
    embed.add_field(name="DPI", value="1000", inline=False)
    embed.add_field(name="Mouse Sensitivity X", value="0.083", inline=False)
    embed.add_field(name="Mouse Sensitivity Y", value="0.083", inline=False)
    embed.add_field(name="Mouse Targeting Sensitivity", value="0.450", inline=False)
    embed.add_field(name="Mouse Scope Sensitivity", value="0.700", inline=False)
    embed.add_field(name="Monitor", value="Acer KG251QIbmiipx 24.5 240hz", inline=False)
    embed.add_field(name="GPU", value="GTX 1070", inline=False)
    embed.add_field(name="Mousepad", value="Steelseries Qck Heavy", inline=False)
    embed.add_field(name="Keyboard", value="HyperX Alloy FPS Pro", inline=False)
    embed.add_field(name="Headset", value="Steelseries Arctis5 2017", inline=False)
    
    await ctx.send(embed=embed)
    
@bot.command()
async def tokimatsu(ctx):
    embed = discord.Embed(title="時松", description="a.k.a 駆け出しアナニー少年 more...", color=0xFF00FF)

    embed.add_field(name="MOUSE", value="Logicool G402", inline=False)
    embed.add_field(name="DPI", value="1600", inline=False)
    embed.add_field(name="Mouse Sensitivity X", value="0.06", inline=False)
    embed.add_field(name="Mouse Sensitivity Y", value="0.06", inline=False)
    embed.add_field(name="Mouse Targeting Sensitivity", value="0.9", inline=False)
    embed.add_field(name="Mouse Scope Sensitivity", value="0.9", inline=False)
    embed.add_field(name="Monitor", value="I-O DATA GigaCrysta 24.5 240hz", inline=False)
    embed.add_field(name="GPU", value="RTX 2080", inline=False)
    embed.add_field(name="Mousepad", value="Artisan Shidenkai SnowWhite", inline=False)
    embed.add_field(name="Keyboard", value="Corsair K63 Red", inline=False)
    embed.add_field(name="Headset", value="Astro A40TR-MAP&Mix Amp 2019", inline=False)
    
    await ctx.send(embed=embed)
    
@bot.command()
async def ushi(ctx):
    embed = discord.Embed(title="牛島", description="880-0122 宮崎県宮崎市塩路1334−3", color=0x0000ee)

    embed.add_field(name="MOUSE", value="Logicool G403", inline=False)
    embed.add_field(name="DPI", value="1600", inline=False)
    embed.add_field(name="Mouse Sensitivity X", value="0.03", inline=False)
    embed.add_field(name="Mouse Sensitivity Y", value="0.03", inline=False)
    embed.add_field(name="Mouse Targeting Sensitivity", value="?", inline=False)
    embed.add_field(name="Mouse Scope Sensitivity", value="?", inline=False)
    embed.add_field(name="Monitor", value="BenQ Zowie XL2546 24.5 240hz", inline=False)
    embed.add_field(name="GPU", value="GTX 1660Ti", inline=False)
    embed.add_field(name="Mousepad", value="FANTECH M80 mouse pad", inline=False)
    embed.add_field(name="Keyboard", value="NPET K10", inline=False)
    embed.add_field(name="Headset", value="SADES Diablo", inline=False)
    
    await ctx.send(embed=embed)
    
@bot.command()
async def haruki(ctx):
    embed = discord.Embed(title="興梠", description="https://www.vill.nishimera.lg.jp/", color=0x800080)

    embed.add_field(name="MOUSE", value="Steelseries Rival", inline=False)
    embed.add_field(name="DPI", value="?", inline=False)
    embed.add_field(name="Mouse Sensitivity X", value="0.150", inline=False)
    embed.add_field(name="Mouse Sensitivity Y", value="0.150", inline=False)
    embed.add_field(name="Mouse Targeting Sensitivity", value="?", inline=False)
    embed.add_field(name="Mouse Scope Sensitivity", value="?", inline=False)
    embed.add_field(name="Monitor", value="ViewSonic VX3276-2K-MHD-7 60hz", inline=False)
    embed.add_field(name="GPU", value="GTX 1070", inline=False)
    embed.add_field(name="Mousepad", value="Learntech PUBG Big pro gaming mouse pad", inline=False)
    embed.add_field(name="Keyboard", value="Lantoo GamingKeyboard Lefthand", inline=False)
    embed.add_field(name="Headset", value="?", inline=False)
    
    await ctx.send(embed=embed)
            
bot.run(token)    
client.run(token) 

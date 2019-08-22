from discord.ext import commands
import os
import traceback
import discord
import math

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

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
async def shine(ctx):
    await ctx.send('しね')
    
@bot.command()
async def edpi(ctx, a: float, b: float):
    await ctx.send('お前のEDPIは %d や \n わかったか？' % (round(a*b)))
    
@bot.command()
async def furimuki(ctx, c: float, d: float):
    await ctx.send('お前の振り向きは %.1f cmや \n わかったか？' % (round(2.54*180/(c*0.55550*d),1)))
    
@bot.command()
async def zoomfurimuki(ctx, c: float, d: float, e: float):
    await ctx.send('お前の振り向きは %.1f cmや \n わかったか？' % (round(2.54*180/(c*0.55550*d*e),1)))

@bot.command()
async def convert2(ctx, a: float):
    await ctx.send('Apexにフォートの感度を持っていきたいときは %.1f cm にするといいぞ' % (round(a * math.tan(80 / 2 / 180 * 3.141592653589793) / math.tan(106 / 2 / 180 * 3.141592653589793),1)))
        
bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Yudo bot", description="上野裕道の脳みそを搭載したロボット", color=0xeee657)

    embed.add_field(name="/na", value="俺が同意してやるぞ", inline=False)
    embed.add_field(name="/ayamare", value="俺が謝ってやるぞ", inline=False)
    embed.add_field(name="/hey", value="俺があいさつ返してやるぞ", inline=False)
    embed.add_field(name="/shine", value="俺が殺してやるぞ", inline=False)
    embed.add_field(name="/edpi", value="DPIと感度を教えると俺がEDPIを計算してやるぞ", inline=False)
    embed.add_field(name="/furimuki", value="DPIと感度を教えると俺が振り向きを測ってやるぞ", inline=False)
    embed.add_field(name="/zoomfurimuki", value="DPIと感度とズーム感度を教えると俺がズーム時の振り向きを測ってやるぞ", inline=False)
    embed.add_field(name="/convert", value="振り向きを教えると俺がApexでの適正振り向きを教えるぞ", inline=False)
    embed.add_field(name="/takayama", value="高山の情報を教えるぞ", inline=False)
    embed.add_field(name="/tokimatsu", value="時松の情報を教えるぞ", inline=False)
    embed.add_field(name="/ushi", value="牛島の情報を教えるぞ", inline=False)
    embed.add_field(name="/haruki", value="はるきの情報を教えるぞ", inline=False)
    embed.add_field(name="/shibata", value="ごめんな", inline=False)
    embed.add_field(name="/help", value="俺がどんなことするか教えてやるぞ", inline=False)

    await ctx.send(embed=embed)
    
@bot.command()
async def takayama(ctx):
    embed = discord.Embed(title="高山", description="USE CODE HUDDLED IN THE ITEM SHOP", color=0x00ff00)

    embed.add_field(name="MOUSE", value="DHARMAPOINT DPTM37BK", inline=False)
    embed.add_field(name="DPI", value="1000", inline=False)
    embed.add_field(name="Mouse Sensitivity X", value="0.08", inline=False)
    embed.add_field(name="Mouse Sensitivity Y", value="0.08", inline=False)
    embed.add_field(name="Mouse Targeting Sensitivity", value="0.450", inline=False)
    embed.add_field(name="Mouse Scope Sensitivity", value="0.700", inline=False)
    embed.add_field(name="Monitor", value="Acer KG251QIbmiipx 24.5 240hz", inline=False)
    embed.add_field(name="GPU", value="ZOTAC GEFORCE GTX 1070 MINI", inline=False)
    embed.add_field(name="Mousepad", value="Steelseries Qck Heavy", inline=False)
    embed.add_field(name="Keyboard", value="HyperX Alloy FPS Pro", inline=False)
    embed.add_field(name="Headset", value="Steelseries Arctis5 2017", inline=False)
    
    await ctx.send(embed=embed)
    
@bot.command()
async def tokimatsu(ctx):
    embed = discord.Embed(title="時松", description="a.k.a 駆け出しアナニー少年 more...", color=0xFF00FF)

    embed.add_field(name="MOUSE", value="Logicool G402", inline=False)
    embed.add_field(name="DPI", value="1600", inline=False)
    embed.add_field(name="Mouse Sensitivity X", value="0.059", inline=False)
    embed.add_field(name="Mouse Sensitivity Y", value="0.059", inline=False)
    embed.add_field(name="Mouse Targeting Sensitivity", value="0.80", inline=False)
    embed.add_field(name="Mouse Scope Sensitivity", value="0.97", inline=False)
    embed.add_field(name="Monitor", value="I-O DATA GigaCrysta 24.5 240hz", inline=False)
    embed.add_field(name="GPU", value="GIGABITE RTX 2080", inline=False)
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
    embed.add_field(name="GPU", value="GIGABITE GTX 1660Ti", inline=False)
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
    embed.add_field(name="Headset", value="きこえる", inline=False)
    
    await ctx.send(embed=embed)
    
@bot.command()
async def shibata(ctx):
    embed = discord.Embed(title="柴田", description="0985-22-3302 宮崎市下北方町役田745-11", color=0xbc8f8f)

    embed.add_field(name="MOUSE", value="つよいやつ", inline=False)
    embed.add_field(name="DPI", value="たくさん", inline=False)
    embed.add_field(name="Mouse Sensitivity X", value="たかい", inline=False)
    embed.add_field(name="Mouse Sensitivity Y", value="たかい", inline=False)
    embed.add_field(name="Mouse Targeting Sensitivity", value="ひくい", inline=False)
    embed.add_field(name="Mouse Scope Sensitivity", value="ひくい", inline=False)
    embed.add_field(name="Monitor", value="すごいやつ", inline=False)
    embed.add_field(name="GPU", value="やばいやつ", inline=False)
    embed.add_field(name="Mousepad", value="すべるやつ", inline=False)
    embed.add_field(name="Keyboard", value="ひかるやつ", inline=False)
    embed.add_field(name="Headset", value="きこえる", inline=False)
    
    await ctx.send(embed=embed)
            
    

bot.run(token)    
client.run(token) 

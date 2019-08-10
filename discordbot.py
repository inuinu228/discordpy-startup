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
async def join(ctx):
        if message.author.voice_channel is None:
            await client.send_message(message.channel ,'ボイスチャンネルに参加してからコマンドを打て')
            return
        if voice == None:
            # ボイスチャンネルIDが未指定なら
            if discord_voice_channel_id == 'チャンネル１':
                voice = await client.join_voice_channel(message.author.voice_channel)
            # ボイスチャンネルIDが指定されていたら
            else:
                voice = await client.join_voice_channel(client.get_channel(discord_voice_channel_id))
        # 接続済みか確認
        elif(voice.is_connected() == True):
            # 再生中の場合は一度停止
            if(player.is_playing()):
                player.stop()
            # ボイスチャンネルIDが未指定なら
            if discord_voice_channel_id == '':
                await voice.move_to(message.author.voice_channel)
            # ボイスチャンネルIDが指定されていたら
            else:
                await voice.move_to(client.get_channel(discord_voice_channel_id))
        # youtubeからダウンロードし、再生
        player = await voice.create_ytdl_player(youtube_url)
        player.start()
        return
    
 @bot.command()
async def stop(ctx):
        if(player.is_playing()):
                player.stop()
                return
    
    
 @bot.command()
async def stop(ctx):
        if voice is not None:
            await voice.disconnect()
            voice = None
            return

    
@bot.command()
async def na(ctx):
    await ctx.send('おう')
    
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
    embed.add_field(name="/ayamare", value="俺が謝ってやるぞ", inline=False)
    embed.add_field(name="/edpi", value="DPIと感度を教えると俺がEDPIを計算してやるぞ", inline=False)
    embed.add_field(name="/furimuki", value="DPIと感度を教えると俺が振り向きを測ってやるぞ", inline=False)
    embed.add_field(name="/help", value="俺がどんなことするか教えてやるぞ", inline=False)

    await ctx.send(embed=embed)
            
bot.run(token)    
client.run(token) 

import discord
from discord.ext import commands

# 前綴
bot = commands.Bot(command_prefix="##")

# 登入訊息
@bot.event
async def on_ready():
    print(">> Bot is online <<")

# Log
@bot.event
async def on_voice_state_update(member,before,after):
    channel = bot.get_channel(807590258564268062)
    N = "None"
    if str(before.channel) in N:
        await channel.send(f"{member} 加入了{after.channel}")
    if str(after.channel) in N:
        await channel.send(f"{member} 離開了{before.channel}")
    if before.channel.id != after.channel.id:
        await channel.send(f"{member} 從{before.channel} 跳進了{after.channel}")

bot.run('ODA3NTg1NjQ1Mzk1NzA1ODU2.YB6Ivg.FOFheanXn_jroOlaXj1SXs49vw4')
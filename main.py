import discord
from discord.ext import commands
import requests ,json
import os

intents = discord.Intents().all()
bot = commands.Bot(command_prefix="d.",intents=intents)

cogs = ["clashroyale","troll","havadurumu","hayvanlar","pokemon","zar","ban_unban","on_member_join","on_member_remove","yardım","sil","nezaman","meme","incele","tahmin","pythonquiz","sunucu","valorant","music_cog","renk","film","döviz"]

for cog in cogs:
        bot.load_extension(cog) 
        print(f"{cog} succesfully loaded.")

@bot.event
async def on_ready():
    print(f"{bot.user} is ready.")
    activity1 = discord.Activity(type=discord.ActivityType.playing, name='d.yardım yaz!')
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=activity1)

#MUSIC
#LEVEL ,MEDIA


bot.run(os.environ['BOT_TOKEN'])

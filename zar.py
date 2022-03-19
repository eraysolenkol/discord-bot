from discord.ext import commands
import discord
import random

class zar(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def zar(self, ctx):
        zarlar = [i for i in range(1,7)]
        ne_cikti = [random.choice(zarlar),random.choice(zarlar)]
        zar_url = [f"https://thefiveplanets.org/b01/data/graphics/textures/dice/face{ne_cikti[0]}.jpg",f"https://thefiveplanets.org/b01/data/graphics/textures/dice/face{ne_cikti[1]}.jpg"]
        embed1 = discord.Embed(title=f"{ctx.author.name} zarı attı!",description=f"{ctx.author.mention} {ne_cikti[0]} geldi!",color=discord.Color.magenta())
        embed1.set_thumbnail(url=zar_url[0])
        embed2 = discord.Embed(title=f"{ctx.author.name} zarı attı!",description=f"{ctx.author.mention} {ne_cikti[1]} geldi!",color=discord.Color.magenta())
        embed2.set_thumbnail(url=zar_url[1])
        await ctx.send(embed=embed1)
        await ctx.send(embed=embed2)

        
def setup(bot):
    bot.add_cog(zar(bot))
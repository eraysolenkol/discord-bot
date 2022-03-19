from discord.ext import commands
import discord
import random

class renk(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def renk(self, ctx):
        renkler = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        renk_hex = "".join([random.choice(renkler) for i in range(6)])
        embed1 = discord.Embed(title=f"#{renk_hex.upper()}",color=(int(renk_hex,16)))
        embed1.set_image(url=f'https://singlecolorimage.com/get/{renk_hex}/400x100.png')
        await ctx.send(embed=embed1)
 
def setup(bot):
    bot.add_cog(renk(bot))
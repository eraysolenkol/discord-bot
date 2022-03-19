from discord.ext import commands
import discord
import random
import valorantrank
import replikler

val_agents = valorantrank.valorant_agent_images
replik_listesi = replikler.tum_replikler

class valorant(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def valorant(self, ctx):
        agent = random.choice(list(val_agents.keys()))
        replik = random.choice(replik_listesi[agent])
        embed = discord.Embed(title=f"{agent}",description=replik,color=discord.Color.magenta())
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.set_image(url=val_agents[agent])
        await ctx.send(embed=embed)

      
def setup(bot):
    bot.add_cog(valorant(bot))
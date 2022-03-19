from discord.ext import commands
import discord

class on_member_remove(commands.Cog):

    def __init__(self, bot):
        self.bot = bot 

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = discord.utils.get(member.guild.text_channels,name='gelen-giden')
        embed = discord.Embed(title=f"{member.name} sunucumuzdan ayrıldı :(",description="\n",color=discord.Color.red())
        embed.set_thumbnail(url=member.avatar_url)
        await channel.send(embed=embed)
        

def setup(bot):
    bot.add_cog(on_member_remove(bot))
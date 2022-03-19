from discord.ext import commands
import discord

class on_member_join(commands.Cog):

    def __init__(self, bot):
        self.bot = bot 

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.text_channels,name='gelen-giden')
        embed = discord.Embed(title=f"{member.guild.name} Sunucumuza hoşgeldin!!",description=f"{member.mention} bence içeride beraber çok fazla eğleneceğiz ve öğreneceğiz.\n\nd.yardım yazıp botun tüm komutları hakkında bilgi alabilirsin.",color=discord.Color.green())
        embed.set_thumbnail(url=member.avatar_url)
        await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(on_member_join(bot))
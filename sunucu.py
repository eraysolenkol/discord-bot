from discord.ext import commands
import discord

class sunucu(commands.Cog):

    def __init__(self, bot):
        self.bot = bot 

    @commands.command()
    async def sunucu(self, ctx):
        embed=discord.Embed(title=f"{ctx.guild.name} İstatistikleri",color=discord.Color.blue())
        embed.add_field(name="Kullanıcı Sayısı:", value=ctx.guild.member_count, inline=False)
        embed.add_field(name="Kanal Sayısı:", value=len(ctx.guild.channels), inline=False)
        if ctx.guild.icon_url != None:
            embed.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.send(embed=embed) 


def setup(bot):
    bot.add_cog(sunucu(bot))
from discord.ext import commands
import discord
from datetime import datetime

class ban_unban(commands.Cog):

    def __init__(self, bot):
        self.bot = bot 
        
    @commands.command()
    @discord.ext.commands.has_any_role("Yönetici","Yardımcı Yönetici","Geliştirici","BOT","Noob Brades")
    @discord.ext.commands.guild_only()

    async def ban(self,ctx, user:discord.Member,*args):
        reason = " ".join(args)
        await ctx.guild.ban(user)
        embed = discord.Embed(title=f"",description=f"**Kullanıcı Sunucumuzdan Banlanmıştır.**",color=discord.Color.red())
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="*",value=f"""**Banlanma Sebebi :** {reason}
**Banı Atan Yönetici :** {ctx.author.mention}
**Kullanıcı ID:** {user.id}
**Kullanıcı İsim ve Tag :** {user.mention}""")
        embed.set_author(name=user.name,icon_url=user.avatar_url)
        now = datetime.now()
        dt = now.strftime("%d/%m/%Y %H:%M:%S")
        embed.set_footer(text=f"{ctx.author.guild.name} • {dt}")
        channel = discord.utils.get(ctx.guild.channels, name='log')
        await channel.send(embed=embed)

    @commands.command()
    @discord.ext.commands.has_any_role("Yönetici","Yardımcı Yönetici","Geliştirici","BOT","Noob Brades")
    @discord.ext.commands.guild_only()
    async def unban(self,ctx, id: int,*args):
        reason = " ".join(args)
        user = await self.bot.fetch_user(id)
        await ctx.guild.unban(user)
        embed = discord.Embed(title=f"",description=f"**{user.mention}'ın yasağı kaldırıldı.**",color=discord.Color.green())
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="*",value=f"""**Banın Kaldırılma Sebebi:** {reason}
**Banı Kaldıran Yönetici :** {ctx.author.mention}
**Kullanıcı ID:** {id}
**Kullanıcı İsim ve Tag :** {user.mention}""")
        embed.set_author(name=user.name,icon_url=user.avatar_url)
        now = datetime.now()
        dt = now.strftime("%d/%m/%Y %H:%M:%S")
        embed.set_footer(text=f"{ctx.author.guild.name} • {dt}")
        channel = discord.utils.get(ctx.guild.channels, name='log')
        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(ban_unban(bot))
import discord
from discord.ext import commands
from datetime import datetime

class sil(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_any_role("Yönetici","Noob Brades")
    async def sil(self,ctx,amount = 1):
        await ctx.channel.purge(limit=amount+1)
        await ctx.send(f"İstediğiniz üzere {amount} mesaj silinmiştir {ctx.author.mention}", delete_after=5)

    # @sil.error 
    # async def sil_error(ctx, error):
    #     if isinstance(error, commands.MissingRole):
    #         await ctx.send("Bu komutu kullanabilmek için **Yönetici** yetkisine sahip olmanız gerekmektedir.")


def setup(bot):
    bot.add_cog(sil(bot))
from discord.ext import commands
import json,requests
import discord

class havadurumu(commands.Cog):

    def __init__(self, bot):
        self.bot = bot 
        
    @commands.command()
    async def havadurumu(self, ctx, şehir):
        r = requests.get(f'https://weatherdbi.herokuapp.com/data/weather/{şehir}')
        data = json.loads(r.text)
        region = data['region']
        current = data['currentConditions']
        saat = current['dayhour']
        hava = current['temp']['c']
        icon = current['iconURL']
        embed = discord.Embed(title=region,description=f"Hava : {hava}°C\nSaat : {saat}",color=discord.Color.green())
        embed.set_thumbnail(url=icon)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(havadurumu(bot))
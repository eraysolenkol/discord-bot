from discord.ext import commands
import json,requests

r = requests.get('http://www.floatrates.com/daily/try.json')

class döviz(commands.Cog):

    def __init__(self, bot):
        self.bot = bot 
        
    @commands.command()
    async def dolar(self, ctx): 
        data = json.loads(r.text)
        money = data['usd']['inverseRate']
        await ctx.send(f'Dolar = {round(money,2)}TL')

    @commands.command()
    async def euro(self, ctx): 
        data = json.loads(r.text)
        money = data['eur']['inverseRate']
        await ctx.send(f'Euro = {round(money,2)}TL')

    @commands.command()
    async def sterlin(self, ctx): 
        data = json.loads(r.text)
        money = data['gbp']['inverseRate']
        await ctx.send(f'Sterlin = {round(money,2)}TL')


def setup(bot):
    bot.add_cog(döviz(bot))
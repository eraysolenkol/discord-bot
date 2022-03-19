from discord.ext import commands
import json,requests

class hayvanlar(commands.Cog):

    def __init__(self, bot):
        self.bot = bot 
        
    @commands.command()
    async def köpek(self, ctx):
        r = requests.get('https://dog.ceo/api/breeds/image/random')
        data = json.loads(r.text)
        await ctx.send(data['message'])

    @commands.command()
    async def kedi(self, ctx):
        r = requests.get('https://api.thecatapi.com/v1/images/search')
        data = json.loads(r.text)
        await ctx.send(data[0]['url'])

    @commands.command()
    async def kuş(self, ctx):
        r = requests.get('https://some-random-api.ml/animal/birb')
        data = json.loads(r.text)
        await ctx.send(data['image'])

def setup(bot):
    bot.add_cog(hayvanlar(bot))
from discord.ext import commands
import json,requests
import random

class meme(commands.Cog):

    def __init__(self, bot):
        self.bot = bot 
        
    @commands.command()
    async def meme(self, ctx): 

        r = requests.get("https://programmermemes.herokuapp.com/")

        data = json.loads(r.text)
        num = random.randint(0,80)
        await ctx.send(data['memes'][num]['url'])
def setup(bot):
    bot.add_cog(meme(bot))
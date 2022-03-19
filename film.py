from discord.ext import commands
import json,requests
import discord
import random
import html2text
from urllib.parse import quote
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}
class film(commands.Cog):

    def __init__(self, bot):
        self.bot = bot 
        
    @commands.command()
    async def film(self, ctx): 
        r = requests.get("https://raw.githubusercontent.com/hjorturlarsen/IMDB-top-100/master/data/movies.json")
        data = json.loads(r.text)
        film = random.choice(data)['title']
        embed1 = discord.Embed(title=f"SANA BİR FİLM ÖNERİSİ {ctx.author.name}!",description=film,color=discord.Color.blurple())
        embed1.set_thumbnail(url=ctx.author.avatar_url)
        await ctx.send(embed=embed1)

    @commands.command()
    async def dizi(self, ctx , dizi_isim ,*args):
        dizi_isim += " "
        dizi_isim += " ".join(args)
        dizi_isim = quote(dizi_isim)
        r = requests.get(f'https://api.tvmaze.com/search/shows?q={dizi_isim}',headers=headers)
        data = json.loads(r.text)[0]
        name = data['show']['name']
        language = data['show']['language']
        genres = data['show']['genres']
        genres_str = " ,".join([genres[i] for i in range(len(genres))])
        image = data['show']['image']['original']
        summary = html2text.html2text(data['show']['summary'])
        embed1 = discord.Embed(title=name,description=f"""```yaml
Language: {language}```
```yaml
Genres: {genres_str}``` \n**Summary:** {summary}""",color=discord.Color.blurple())
        embed1.set_image(url=image)
        embed1.set_thumbnail(url=self.bot.user.avatar_url)
        await ctx.send(embed=embed1)

def setup(bot):
    bot.add_cog(film(bot))
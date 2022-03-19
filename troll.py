from discord.ext import commands
import json,requests
import discord
from urllib.parse import quote

class troll(commands.Cog):

    def __init__(self, bot):
        self.bot = bot 
        
    @commands.command()
    async def trigger(self, ctx, user:discord.Member):
        link = user.avatar_url
        link = str(link).replace(".webp",".png")
        await ctx.send(f'https://some-random-api.ml/canvas/triggered?avatar={link}')

    @commands.command()
    async def sarıl(self, ctx, user:discord.Member):
        if ctx.author.id == user.id:
            await ctx.send("O kadar yalnız mısın :(")
        else:
            r = requests.get('https://some-random-api.ml/animu/hug')
            link = json.loads(r.text)['link']
            await ctx.send(f"{ctx.author.mention} {user.mention}'a sarılıyor.\n {link}")

    @commands.command()
    async def sev(self, ctx, user:discord.Member):
        if ctx.author.id == user.id:
            await ctx.send("O kadar yalnız mısın :(")
        else:
            r = requests.get('https://some-random-api.ml/animu/pat')
            link = json.loads(r.text)['link']
            await ctx.send(f"{ctx.author.mention} {user.mention}'ı seviyor.\n {link}")

    @commands.command()
    async def gözkırp(self, ctx, user:discord.Member):
        if ctx.author.id == user.id:
            await ctx.send("O kadar yalnız mısın :(")
        else:
            r = requests.get('https://some-random-api.ml/animu/wink')
            link = json.loads(r.text)['link']
            await ctx.send(f"{ctx.author.mention} {user.mention}'a göz kırptı.\n {link}")

    @commands.command()
    async def youtubeyorum(self, ctx ,*args):
        comment = " ".join(args)
        comment = quote(comment)
        avatar = ctx.author.avatar_url
        avatar = str(avatar).replace(".webp",".png")
        image = f'https://some-random-api.ml/canvas/youtube-comment?avatar={avatar}&username={ctx.author.name}&comment={comment}'
        await ctx.send(image)

    @commands.command()
    async def twitteryorum(self, ctx ,*args):
        comment = " ".join(args)
        comment = quote(comment)
        avatar = ctx.author.avatar_url
        avatar = str(avatar).replace(".webp",".png")
        image = f'https://some-random-api.ml/canvas/tweet?avatar={avatar}&username={ctx.author.name}&comment={comment}&displayname={ctx.author.name}'
        await ctx.send(image)

def setup(bot):
    bot.add_cog(troll(bot))
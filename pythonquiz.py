#https://i.imgur.com/pQ0X6Re.png
from discord.ext import commands
import discord
import random
import asyncio

class pythonquiz(commands.Cog):

    def __init__(self, bot):
        self.bot = bot 

    @commands.command()
 
    async def pythonquiz(self, message):
        # we do not want the bot to reply to itself

        if message.author.id == self.bot.user.id:
            return

        quiz = {"https://i.imgur.com/pQ0X6Re.png":"30",
        "https://i.imgur.com/G7lH1A0.png":"b",
        "https://i.imgur.com/8gNlI4T.png":"doC",
        "https://i.imgur.com/YtK0cra.png":"182.0",
        "https://i.imgur.com/4EQPg0B.png":"a"}

        quiz_at = {"https://i.imgur.com/pQ0X6Re.png":"",
        "https://i.imgur.com/G7lH1A0.png":"""```yaml
a) True\n   True``` ```yaml
b) True\n   False``````yaml
c) False\n   True``` ```yaml
d) False\n   False```""",
        "https://i.imgur.com/8gNlI4T.png":"",
        "https://i.imgur.com/YtK0cra.png":"",
        "https://i.imgur.com/4EQPg0B.png":"""```yaml
a) TypeError``` ```yaml
b) ["Python","Php","C","Java"]``````yaml
c) ["Python","C","Php","Java"]``` ```yaml
d) ["Python","C","Java","Php"]```"""}

        soru = random.choice(list(quiz.keys()))
        embed=discord.Embed(title="Python Quiz",description="Bu kodun çıktısı nedir?",color=discord.Color.gold())   
        embed.set_image(url=soru)
        if quiz_at[soru] != "":
            embed.add_field(name="Şıklar:",value=f"Örnek cevap şekli: c\n{quiz_at[soru]}")
        await message.channel.send(embed=embed)

        def is_correct(m):
            return m.author == message.author

        cevap = quiz[soru]

        try:
            guess = await self.bot.wait_for('message', check=is_correct, timeout=60.0)
        except asyncio.TimeoutError:
            return await message.channel.send(f'Üzgünüm, 60 saniyeyi geçtin , cevap ise {cevap}.')

        if guess.content == cevap:
            await message.channel.send('Doğru Cevap!!')
        else:
            await message.channel.send(f'Yaklaştın gibi ya ama cevap {cevap} :(')


def setup(bot):
    bot.add_cog(pythonquiz(bot))
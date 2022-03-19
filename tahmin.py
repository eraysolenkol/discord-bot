from discord.ext import commands
import discord
import random
import asyncio

class tahmin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot 
        
    @commands.command()
 
    async def tahmin(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.bot.user.id:
            return


        await message.channel.send(f'{message.author.mention} 1 ile 10 arasında bir sayı tahmin et!')

        def is_correct(m):
            return m.author == message.author and m.content.isdigit()

        cevap = random.randint(1, 10)

        try:
            guess = await self.bot.wait_for('message', check=is_correct, timeout=15.0)
        except asyncio.TimeoutError:
            return await message.channel.send(f'Üzgünüm, 15 saniyeyi geçtin , cevap ise {cevap}.')

        if int(guess.content) == cevap:
            await message.channel.send('Müneccin gibiyim diyorsun!')
        else:
            await message.channel.send(f'Yaklaştın gibi ya ama cevap {cevap} :(')


def setup(bot):
    bot.add_cog(tahmin(bot))
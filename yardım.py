from discord.ext import commands
import discord

class yardım(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def yardım(self, ctx):

        text_eglence = """
```yaml
d.zar -> Rastgele 2 adet zar atar.      

d.meme -> Rastgele bir programlama meme'i gönderir.

d.renk -> Rastgele bir renk verir.

d.tahmin -> Sayı tahmin etme oyunu başlatır.

d.pythonquiz -> Basit bir python sorusu sorar. (60 saniye cevaplama süresi)

d.film -> IMDB TOP 100'den bir film önerir.

d.dizi <isim> -> Dizi hakkındaki basit bilgileri verir (İngilizce)

d.randompoke -> Rastgele bir pokemon gönderir.

d.köpek -> Rastgele bir köpek fotoğrafı gönderir.

d.kedi -> Rastgele bir kedi fotoğrafı gönderir.

d.kuş -> Rastgele bir kuş fotoğrafı gönderir.

d.youtubeyorum -> Youtube yorumu şeklinde mesaj gönderir.

d.twitteryorum -> Twitter yorumu şeklinde mesaj gönderir.

d.trigger @discord.Member -> İstediğin kişiyi triggerla.```
**1**/6
"""
        text_anime = """```yaml
d.sarıl @discord.Member -> İstediğin kişiye sarılabilirsin.```
```yaml
d.sev @discord.Member -> İstediğin kişiyi sevebilirsin.```
```yaml
d.gözkırp @discord.Member -> İstediğin kişiye göz kırpabilirsin.```
**2**/6"""
        text_muzik = """```yaml
d.oynat <url veya şarkı ismi> -> Bulunduğun kanalda şarkı çalar.```
```yaml
d.sıra -> Şarkı sırasını gösterir.```
```yaml
d.atla -> Sonraki şarkıya geçer.```
```yaml
d.çıkış -> Sesli sohbetten çıkar.```
```yaml
d.neçalıyor -> Çalan şarkıyı gösterir.```
**3**/6"""

        text_valorant = """```yaml
d.incele nickname#tag -> Kişinin valorant hesabının istatistiklerini gösterir.```
```yaml
d.valorant -> Rastgele bir valorant ajanı ve repliği gönderir.```
**5**/6"""

        text_sunucu = """```yaml
d.sil <miktar> -> Girilen miktar kadar mesajı kullanıldığı kanaldan siler.```
```yaml
d.nezaman @discord.Member -> Etiketlenen kişinin hesabının ne zaman yaratıldığını ve sunucuya ne zaman katıldığını gösterir.```
```yaml
d.sunucu -> Sunucu hakkında basit istatistikleri gösterir.```
```yaml
d.ban @discord.Member -> Kullanıcıyı sunucudan yasaklar.```
```yaml
d.unban <id> -> Kullanıcının sunucu yasaklamasını kaldırır.```
**4**/6"""
        text_haber = """```yaml
d.dolar -> Dolar kurunu gösterir.```
```yaml
d.euro -> Euro kurunu gösterir.```
```yaml
d.sterlin -> Sterlin kurunu gösterir.```
```yaml
d.havadurumu <şehir> -> Anlık hava durumunu gösterir.```
**6**/6"""

        embed = discord.Embed(title=f"Merhaba {ctx.author.name} , Botumuzun Tüm Eğlence Komutları: ",description=text_eglence,color=discord.Color.orange())
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed2 = discord.Embed(title=f"Merhaba {ctx.author.name} , Botumuzun Tüm Müzik Komutları: ",description=text_muzik,color=discord.Color.orange())
        embed2.set_thumbnail(url=self.bot.user.avatar_url)
        embed3 = discord.Embed(title=f"Merhaba {ctx.author.name} , Botumuzun Tüm Yönetim Komutları: ",description=text_sunucu,color=discord.Color.orange())
        embed3.set_thumbnail(url=self.bot.user.avatar_url)
        embed4 = discord.Embed(title=f"Merhaba {ctx.author.name} , Botumuzun Tüm Valorant Komutları: ",description=text_valorant,color=discord.Color.orange())
        embed4.set_thumbnail(url=self.bot.user.avatar_url)
        embed5 = discord.Embed(title=f"Merhaba {ctx.author.name} , Botumuzun Tüm Haber Komutları: ",description=text_haber,color=discord.Color.orange())
        embed5.set_thumbnail(url=self.bot.user.avatar_url)
        embed6 = discord.Embed(title=f"Merhaba {ctx.author.name} , Botumuzun Tüm Anime Komutları: ",description=text_anime,color=discord.Color.orange())
        embed6.set_thumbnail(url=self.bot.user.avatar_url)

        pages = [embed,embed6,embed2,embed3,embed4,embed5]
        message = await ctx.send(embed = embed)

        await message.add_reaction('◀')
        await message.add_reaction('▶')
        def check(reaction, user):
            return user == ctx.author

        i = 0
        reaction = None

        while True:
            if str(reaction) == '◀':
                if i > 0:
                    i -= 1
                    await message.edit(embed = pages[i])
            elif str(reaction) == '▶':
                if i < 5:
                    i += 1
                    await message.edit(embed = pages[i])      
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout = 30.0, check = check)
                await message.remove_reaction(reaction, user)
            except:
                break

        await message.clear_reactions()
        
def setup(bot):
    bot.add_cog(yardım(bot))
import discord
from discord.ext import commands

from youtube_dl import YoutubeDL

class music_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
        #all the music related stuff
        self.is_playing = False
        self.music_titles = []
        # 2d array containing [song, channel]
        self.music_queue = []
        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

        self.vc = ""

     #searching the item on youtube
    def search_yt(self, item):
        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            try: 
                info = ydl.extract_info("ytsearch:%s" % item, download=False)['entries'][0]
            except Exception: 
                return False

        return {'source': info['formats'][0]['url'], 'title': info['title'],'thumbnail':info['thumbnail']}

    def play_next(self):
        if len(self.music_queue) > 0:
            self.is_playing = True

            #get the first url
            m_url = self.music_queue[0][0]['source']

            #remove the first element as you are currently playing it
            self.music_queue.pop(0)

            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
        else:
            self.is_playing = False

    # infinite loop checking 
    async def play_music(self):
        if len(self.music_queue) > 0:
            self.is_playing = True

            m_url = self.music_queue[0][0]['source']
            m_title = self.music_queue[0][0]['title']
            m_thumbnail = self.music_queue[0][0]['thumbnail']
            self.music_titles.append((m_title,m_thumbnail))


            #try to connect to voice channel if you are not already connected

            if self.vc == "" or not self.vc.is_connected() or self.vc == None:
                self.vc = await self.music_queue[0][1].connect()
            else:
                await self.vc.move_to(self.music_queue[0][1])
                self.music_titles.pop(0)
            
            print(self.music_queue)
            #remove the first element as you are currently playing it
            self.music_queue.pop(0)

            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())

            channel = discord.utils.get(self.bot.get_all_channels(), name='müzik')
            embed = discord.Embed(title=m_title,color=discord.Color.green())
            embed.set_thumbnail(url=self.bot.user.avatar_url) 
            embed.set_image(url=m_thumbnail)
            await channel.send(embed=embed)
        else:
            self.is_playing = False

    @commands.command()
    async def oynat(self, ctx, *args):
        query = " ".join(args)
        
        voice_channel = ctx.author.voice.channel
        if voice_channel is None:
            #you need to be connected so that the bot knows where to go
            await ctx.send("Lütfen önce bir ses kanalına bağlan.")
        else:
            song = self.search_yt(query)
            if type(song) == type(True):
                await ctx.send("Şarkı alınamadı.Farklı bir sözcük deneyiniz , bu linkin playlist veya canlı yayın kaydı olmasından kaynaklanabilir.")
            else:
                embed = discord.Embed(title=f"Şarkı Listeye Eklendi!",description=song['title'],color=discord.Color.green())
                embed.set_thumbnail(url=self.bot.user.avatar_url) 
                embed.set_image(url=song['thumbnail'])
                await ctx.send(embed=embed)
                self.music_queue.append([song, voice_channel])
                
                if self.is_playing == False:
                    await self.play_music()
                    

    @commands.command()
    async def sıra(self, ctx):
        retval = ""
        for i in range(0, len(self.music_queue)):
            retval += self.music_queue[i][0]['title'] + "\n"

        print(retval)
        if retval != "":
            embed = discord.Embed(title=f"ŞARKI SIRASI",description=retval,color=discord.Color.dark_blue())
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            await ctx.send(embed=embed)
        else:
            await ctx.send("Sırada şarkı bulunmamaktadır.")

    @commands.command()
    async def atla(self, ctx):
        if self.vc != "" and self.vc:
            self.vc.stop()
            #try to play next in the queue if it exists
            
            await self.play_music()

            
    @commands.command()
    async def çıkış(self, ctx):
        await self.vc.disconnect()

    @commands.command()
    async def neçalıyor(self,ctx):
        embed = discord.Embed(title=f"ÇALAN ŞARKI",description=self.music_titles[0][0],color=discord.Color.dark_blue())
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.set_image(url=self.music_titles[0][1])
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(music_cog(bot))
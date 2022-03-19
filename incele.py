import discord
from discord.ext import commands
import valorantrank
import requests,json
from urllib.parse import quote

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}


class incele(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def incele(self,ctx,nickname,*args):
        for arg in args:
            nickname += " "+arg
        nick = nickname.split("#")
        nickname = quote(nick[0]) 
        nickname += "#"+nick[1]
        name = nickname.split("#")
        stats = valorantrank.getSTATS(name,"competitive")
 
        hs_percentage = 0
        agents = []
        x = 0
        while x < 5:
            hs_percentage += stats[0][x][3]
            agents.append(stats[0][x][2])
            x = x + 1

        hs_percentage /= 5
        agent_count = []
        for agent in agents:
            agent_count.append(agents.count(agent))
        index = agent_count.index(max(agent_count))
        most_played_agent = agents[index]
        kd_ratio_stat = 0
        for x in stats[1]:
            kd_ratio_stat += x
        kd_ratio_stat /=5

        r2 = requests.get(f"https://api.henrikdev.xyz/valorant/v1/account/{name[0]}/{name[1]}",headers=headers)
        player_stats2 = json.loads(r2.text)
        region = player_stats2['data']['region']
        r = requests.get(f"https://api.henrikdev.xyz/valorant/v1/mmr/{region}/{name[0]}/{name[1]}",headers=headers)
        player_stats = json.loads(r.text)
        rank = player_stats['data']["currenttierpatched"]
        level = player_stats2['data']["account_level"]
        card_url = player_stats2['data']['card']['small']
        card_url2 = player_stats2['data']['card']['wide']
        elo = player_stats['data']['elo']
        puan = player_stats['data']["ranking_in_tier"]
        mmr_change = player_stats['data']['mmr_change_to_last_game']
        last_update = player_stats2['data']['last_update']
        last_update_tr = "Son Güncelleme Zamanı: " +  last_update 
        if mmr_change > 0:
            mmr_change = "+"+str(mmr_change)
        embed=discord.Embed(title=f"Oyuncu Profili İncelemesi: ", description="Son 5 maç istatistikleri göz önüne alınarak verilere ulaşılmıştır.5 maçlık veriler aşşağıda gösterildiği gibidir.", color=discord.Color.blue())
        embed.set_thumbnail(url=card_url)
        embed.add_field(name="Oyuncu İsmi",value=f"""```yaml
{nickname}```""")
        embed.add_field(name="Level",value=f"""```yaml
{level}```""")
        embed.add_field(name="%HS",value=f"""```yaml
%{round(hs_percentage,2)}```""")
        embed.add_field(name=f"En İyi Ajanı ",value=f"""```yaml
{most_played_agent}```""")
        embed.add_field(name= f'Rank ', value=f"""```yaml
{rank}```""")
        embed.add_field(name= 'Puan', value=f"""```yaml
{puan}```""")
        embed.add_field(name= 'Elo', value=f"""```yaml
{elo}```""")
        embed.add_field(name= 'Bölge', value=f"""```yaml
{region.upper()}```""")
        embed.add_field(name= 'Son Maç', value=f"""```yaml
{mmr_change}```""")
        embed.add_field(name= 'K/D Oranı', value=f"""```yaml
{round(kd_ratio_stat,2)}```""")
        embed.set_image(url=card_url2)
        embed.set_footer(text=last_update_tr)
        await ctx.send(embed=embed)

#     @incele.error 
#     async def incele_error(ctx,error,user=None):
#         if isinstance(error,commands.CommandInvokeError):
#             await ctx.send("Hatalı isim veya yetersiz bilgi")

def setup(bot):
    bot.add_cog(incele(bot))
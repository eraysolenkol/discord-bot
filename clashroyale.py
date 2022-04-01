from discord.ext import commands
import discord
import requests,json
from urllib.parse import quote
import os
import datetime
import time

my_token = os.environ['CR_API_TOKEN']

class clashroyale(commands.Cog):

    def __init__(self, bot):
        self.bot = bot 
        
    @commands.command()
    async def bilgi(self, ctx ,tag:str):
        headers = {'Authorization': f'Bearer {my_token}'}
        tag = tag.replace("#","%23")
        r = requests.get(f"https://proxy.royaleapi.dev/v1/players/{tag}",headers=headers)
        data = json.loads(r.text)

        name = data['name']
        tag = data['tag']
        level = data['expLevel']
        trophy = data['trophies']
        win = data['wins']
        loss = data['losses']
        threeCrownWins = data['threeCrownWins']
        arenaId = data['arena']['id']
        arenaName = data['arena']['name']
        badges = data['badges']
        currentDeck = data['currentDeck']
        winRate = (win*100) / (win+loss)
        deck =""
        for i in currentDeck:
            deck += i['name'] +"/"
        deck = deck.rstrip("/")
        currentFavouriteCard = data['currentFavouriteCard']['name']
        favCardImage = data['currentFavouriteCard']['iconUrls']['medium']
        try:
            clan = data['clan']['name']
            clanTag = data['clan']['tag']
        except:
            clan = ""
            clanTag = ""

        embed = discord.Embed(title=f"{name}",description=f"""**Tag:** {tag}\n**Level:** {level}\n**Kupa:** {trophy}
**Kazanma Oranı:** %{winRate}\n**Deste:** {deck}\n**Clan:** {clan}\n**Clan Tag:** {clanTag}\n\n**En Sevdiği Kart:** {currentFavouriteCard}""",color=discord.Color.blurple())
        embed.set_thumbnail(url=f'https://raw.githubusercontent.com/weeco/clash-royale-assets/master/images/arenas/{arenaId}.png')
        embed.set_image(url=favCardImage)
        await ctx.send(embed=embed)


    @commands.command()
    async def clan(self, ctx ,tag:str,*args):
        headers = {'Authorization': f'Bearer {my_token}'}

        if "#" in tag:
            tag = tag.replace("#","%23")
        else:
            tag = tag + " " + " ".join(args)
            tag = quote(tag) 
            r2 = requests.get(f"https://proxy.royaleapi.dev/v1/clans?name={tag}&limit=1",headers=headers)
            data2 = json.loads(r2.text)
            tag = data2['items'][0]['tag']
            tag = tag.replace("#","%23")

        r = requests.get(f"https://proxy.royaleapi.dev/v1/clans/{tag}",headers=headers)
        data = json.loads(r.text)
        
        name = data['name']
        tag = data['tag']
        desc = data['description']
        badgeId = data['badgeId']
        clanScore = data['clanScore']
        locationId = data['location']['id']
        locationName = data['location']['name']
        members = data['members']
        memberList = data['memberList']
        memberListString= ""
        i = 0
        while i < members:
            member = memberList[i]
            i_str = f"{i+1}."
            memberListString+= f"{i_str:<3}{member['name']:<17} {member['expLevel']:<6}{member['trophies']}  ({member['tag']})\n"
            i+=1

        embed = discord.Embed(title=f"{name}",description=f"""**Tag:** {tag}\n**Açıklama:** {desc}\n**Clan Skoru:** {clanScore}\n**Clan Lokasyonu:** {locationName}\n**Toplam Üye:** {members}
```yaml
{memberListString}
```""",color=discord.Color.blurple())
        embed.set_thumbnail(url=f'https://raw.githubusercontent.com/weeco/clash-royale-assets/master/images/badges/{badgeId}.png')
        await ctx.send(embed=embed)


    @commands.command()
    async def sandık(self, ctx ,tag:str):
        headers = {'Authorization': f'Bearer {my_token}'}
        tag = tag.replace("#","%23")
        r = requests.get(f"https://proxy.royaleapi.dev/v1/players/{tag}/upcomingchests",headers=headers)
        data = json.loads(r.text)

        items = data['items']
        i = 0
        firstChest :str= items[0]['name']
        firstChestLink = firstChest.lower()
        firstChestLink = firstChestLink.replace(" ","-")
        firstChestLink += "-closed"
        chests = ""
        specialChests=""
        while i < 9:
            chests += items[i]['name'] + "/"
            i+=1
        chests = chests.rstrip("/")
        while i < len(items):
            specialChests += items[i]['name'] + " => " +str(items[i]['index'] +1 )+ "\n"
            i+=1


        embed = discord.Embed(title=f"SIRADAKİ SANDIKLAR",description=f"""{chests}
```yaml
{specialChests}```""",color=discord.Color.blurple())
        embed.set_thumbnail(url=f'https://raw.githubusercontent.com/weeco/clash-royale-assets/master/images/chests/{firstChestLink}.png')
        await ctx.send(embed=embed)
        
    @commands.command()
    async def maçlar(self, ctx ,tag:str):
        
        headers = {'Authorization': f'Bearer {my_token}'}
        tag = tag.replace("#","%23")
        r = requests.get(f"https://proxy.royaleapi.dev/v1/players/{tag}/battlelog",headers=headers)
        data = json.loads(r.text)
        i = 0
        fieldNames = []
        fieldValues = []
        flagArena = 0
        arenaId = ""
        while i < 12:
            gameData = data[i]
            gameType = gameData['type']
            if "PvP" in gameType and flagArena == 0:
                arenaId = gameData['arena']['id']
                flagArena = 1
            battleTime = gameData['battleTime']
            teamName = gameData['team'][0]['name']
            teamTag = gameData['team'][0]['tag']
            teamTrophy = gameData['team'][0]['startingTrophies']
            teamCrowns = gameData['team'][0]['crowns']
            opponentName = gameData['opponent'][0]['name']
            opponentTag = gameData['opponent'][0]['tag']
            opponentTrophy = gameData['opponent'][0]['startingTrophies']
            opponentCrowns = gameData['opponent'][0]['crowns']
            whoWinName = teamName if teamCrowns > opponentCrowns else opponentName
            totalCrowns = teamCrowns if teamCrowns > opponentCrowns else opponentCrowns
            date_format = "%Y%m%dT%H%M%S.%fZ" 
            mytime = time.mktime(datetime.datetime.strptime(battleTime, date_format).timetuple())
            discordTime = f"<t:{int(mytime)}:R>"
            k = 0
            crownString = ""
            while k < totalCrowns:
                crownString += "👑"
                k +=1
            embedName = f"{teamName} ({teamTrophy}) VS {opponentName} ({opponentTrophy}) [{gameType} game]"
            embedValue = f"""```yaml
Kazanan: {whoWinName}```
{crownString}
({teamTag} VS {opponentTag})
{discordTime}"""
            fieldNames.append(embedValue)
            fieldValues.append(embedName)
            i+= 1

        embed = discord.Embed(title=f"GEÇMİŞ MAÇLAR",description="",color=discord.Color.blurple())
        j = 0
        while j < 12:
            embed.add_field(name=fieldValues[j],value=fieldNames[j])
            j += 1
        embed.set_thumbnail(url=f'https://raw.githubusercontent.com/weeco/clash-royale-assets/master/images/arenas/{arenaId}.png')
        await ctx.send(embed=embed)


def setup(bot):        
    bot.add_cog(clashroyale(bot))

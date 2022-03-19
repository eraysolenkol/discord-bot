import discord
from discord.ext import commands
from datetime import datetime

class nezaman(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def nezaman(self,ctx, member: discord.Member):
        ay = {"01":"Ocak","02":"Şubat","03":"Mart","04":"Nisan","05":"Mayıs","06":"Haziran","07":"Temmuz","08":"Ağustos","09":"Eylül","10":"Ekim","11":"Kasım","12":"Aralık"}
        joined_at = member.joined_at
        created_at = member.created_at
        year = joined_at.strftime("%Y")
        month = joined_at.strftime("%m")
        day = joined_at.strftime("%d")
        time = joined_at.strftime("%H:%M:%S")
        year2 = created_at.strftime("%Y")
        month2 = created_at.strftime("%m")
        day2 = created_at.strftime("%d")
        time2 = created_at.strftime("%H:%M:%S")
        roles_of_member = member.roles
        roles =[]
        for i in roles_of_member:
            if str(i) != "@everyone":
                roles.append(str(i))
        embed=discord.Embed(title=f"", description="", color=discord.Color.blue())
        roles_string = ", ".join(roles)
        embed.add_field(name="Profil Detayı",value=f"\n\n\n**Kullanıcı:** {member.mention}\n **ID Numarası:** {member.id}\n**Sunucumuzdaki Permleri:** {roles_string}",inline=False)
        embed.add_field(name="**Sunucuya katılma tarihi:**",value=f"""Gün: {day}
Ay: {ay[month]}
Yıl: {year}
Saat: {time}""")
        embed.add_field(name="**Hesap Oluşturulma tarihi:**",value=f"""Gün: {day2}
Ay: {ay[month2]}
Yıl: {year2}
Saat: {time2}""")
        embed.set_thumbnail(url=member.avatar_url)
    
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(nezaman(bot))
from termios import VLNEXT
from discord.ext import commands
import random , requests , json
import discord

class pokemon(commands.Cog):

    def __init__(self, bot):
        self.bot = bot 
        
    @commands.command()
    async def randompoke(self, ctx):
        num = random.randint(1,898)
        r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{num}')
        data = json.loads(r.text)
        name = data['forms'][0]['name'].upper()
        types = data['types']
        type_t = "/".join(types[i]['type']['name'] for i in range(len(types)))
        base_stats = "/".join(str(data['stats'][i]['base_stat']) for i in range(6))
        abilities = "/".join(data['abilities'][i]['ability']['name'] for i in range(len(data['abilities'])))
        embed = discord.Embed(title=name,description=f"""**Pokedex Numarası:** {num}\n**Tipi:** {type_t}\n**Yetenekleri:** {abilities}\n**Base Statları:** {base_stats}\n""",color=discord.Color.blurple())
        embed.set_thumbnail(url=f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{num}.png')
        try:
            r2= requests.get(f'https://some-random-api.ml/pokedex?pokemon={name}')
            data2 = json.loads(r2.text)
            ev = list(data2['family']['evolutionLine'])
            if name.capitalize() in ev:
                index = ev.index(name.capitalize())
                try:
                    next_ev = ev[index+1]
                except:
                    next_ev = ""
                r3 = requests.get(f'https://some-random-api.ml/pokedex?pokemon={next_ev}')
                data = json.loads(r3.text)
                pokeid = int(data['id'])
                img = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokeid}.png'
                embed.add_field(name='Sonraki Evrimi',value=next_ev)
                embed.set_image(url=img)
                
        except:
            None
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(pokemon(bot))
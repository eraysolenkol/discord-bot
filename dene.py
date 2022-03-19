from email.quoprimime import header_decode
import json , requests , random 

next_ev='Ivysaur'
r3 = f'https://some-random-api.ml/pokedex?pokemon={next_ev}'
data = json.loads(r3.text)
pokeid = int(data['id'])
img = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokeid}.png'
print(pokeid)
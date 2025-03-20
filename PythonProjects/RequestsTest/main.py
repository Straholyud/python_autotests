import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'c98935736dfcdd449935492d593f98c0'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}


body_pokemon = {
    "name": "generate",
    "photo_id": 347
}

response = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_pokemon)
print(response.text)

pokemon_id = response.json()["id"]
print(pokemon_id)

body_pokemon_name = {
    "pokemon_id": pokemon_id,
    "name": "generate"
}

pokemon_name = requests.patch(url=f'{URL}/pokemons', headers=HEADER, json=body_pokemon_name)
print(pokemon_name.text)

body_pokeball = {
    "pokemon_id": pokemon_id,
}

pokeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_pokeball)
print(pokeball.text)
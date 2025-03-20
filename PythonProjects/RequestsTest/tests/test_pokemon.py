import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'c98935736dfcdd449935492d593f98c0'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '24867'

def test_status_200():
    responce = requests.get(url=f'{URL}/pokemons', params={'trainer_id':TRAINER_ID})
    assert responce.status_code== 200

def test_name_trainer():
    response_get = requests.get(url=f'{URL}/pokemons', params={'trainer_id':TRAINER_ID})
    assert response.json()['data'][0]['trainer_name'] == 'Flin'
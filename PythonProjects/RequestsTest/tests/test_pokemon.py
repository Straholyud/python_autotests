import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'c98935736dfcdd449935492d593f98c0'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '24867'

def test_status_200():
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id':TRAINER_ID})
    assert response.status_code== 200

def test_name_trainer():
    response_get = requests.get(url=f'{URL}/trainers', params={'trainer_id':TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'Flin'
    print(response_get.text)

@pytest.mark.parametrize('key, value',[('name', 'Flin'), ('trainer_id', TRAINER_ID)], ('trainer_id', '24867'))
def test_parametrize(key,value):
    responce_parametrize = requests.get(url=f'{URL}/trainers', params={'trainer_id':TRAINER_ID})
    assert responce_parametrize.json()["data"][0][key] == value

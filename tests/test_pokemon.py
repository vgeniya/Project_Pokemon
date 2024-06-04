import requests
import pytest

host = 'https://api.pokemonbattle.ru'


def test_status_code():
    response = requests.get(url=f'{host}/v2/trainers', params={'trainer_id': 4349}, timeout=5)
    assert response.status_code == 200
    print(response)


def test_name():
    response = requests.get(url=f'{host}/v2/trainers', params={'trainer_id': 4349}, timeout=5)
    assert response.json()['data'][0]['trainer_name'] == 'Evgenia'
    print(response)



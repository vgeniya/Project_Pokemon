import requests
import pytest

host = 'https://api.pokemonbattle.ru'


def test_create_pokemon():
    response = requests.post(url=f'{host}/v2/pokemons',
                            json={"name": "Pikachu",
                                  "photo": "https://dolnikov.ru/pokemons/albums/001.png"},
                         headers={'Content-Type':  'application/json',
                                  'trainer_token':  '832b1a05601a0a4249f5a6bb387b20d6'}, timeout=5)
    print(response)


def test_update_name_pokemon():
    response = requests.put(url=f'{host}/v2/pokemons',
                            json={"pokemon_id": "27402",
                                  "name": "Pikach",
                                  "photo": "https://dolnikov.ru/pokemons/albums/011.png"},
                         headers={'Content-Type':  'application/json',
                                  'trainer_token':  '832b1a05601a0a4249f5a6bb387b20d6'}, timeout=5)
    print(response)


def test_catch_in_a_pokeball():
    response = requests.post(url=f'{host}/v2/trainers/add_pokeball',
                            json={"pokemon_id": "27402"},
                         headers={'Content-Type':  'application/json',
                                  'trainer_token':  '832b1a05601a0a4249f5a6bb387b20d6'}, timeout=5)
    print(response)


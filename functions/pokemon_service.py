import requests


def get_saludo():
    return "Hola Mundo variable"


def pokemon_request(url: str):
    h = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
    response = requests.get(url, headers=h)
    return response.json()


def get_pokemon_list(url: str):
    response_pokemon_json = pokemon_request(url)
    pokemon_list = []
    for pokemon in response_pokemon_json["results"]:
        pokemon_list.append(pokemon["name"])
    return pokemon_list


def get_pokemon(url: str) -> dict:
    response_pokemon_json = pokemon_request(url)
    dicc_pokemon = {
        'name': response_pokemon_json["name"],
        'number': response_pokemon_json["id"],
        'sprites': response_pokemon_json['sprites']['front_default'],
        'sprite_shiny': response_pokemon_json['sprites']['front_shiny'],
        'types': get_types_pokemon(response_pokemon_json['types']),
        'stats': get_stats_pokemon(response_pokemon_json['stats']),
        'abilities': get_abilities_pokemon(response_pokemon_json['abilities'])
    }
    return dicc_pokemon


def get_types_pokemon(types: list) -> list:
    types_pokemon = []
    for tipo in types:
        types_pokemon.append(tipo['type']['name'])
    return types_pokemon


def get_stats_pokemon(stats: list) -> list:
    stats_pokemons = []
    for stat in stats:
        current_stat = {
            'name': stat['stat']['name'],
            'value': stat['base_stat']
        }
        stats_pokemons.append(current_stat)
    return stats_pokemons


def get_abilities_pokemon(abilities: list) -> list:
    abilities_pokemon = []
    for ability in abilities:
        abilities_pokemon.append(ability["ability"]["name"])
    return abilities_pokemon

# print(get_pokemon("https://pokeapi.co/api/v2/pokemon/palkia"))

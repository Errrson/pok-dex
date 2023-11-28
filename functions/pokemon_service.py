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


def get_pokemon(url: str):
    response_pokemon_json = pokemon_request(url)
    dicc_pokemon = {
        'name': response_pokemon_json["name"],
        'number': response_pokemon_json["id"],
        'sprites': response_pokemon_json['sprites']['front_default']
    }
    return dicc_pokemon


print(get_pokemon("https://pokeapi.co/api/v2/pokemon/ditto"))

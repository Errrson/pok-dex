import requests


class PokemonListClass:

    def __init__(self):
        self.url = "https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0"
        self.h = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
        self.response = self.get_response()

    def get_response(self):
        response = requests.get(self.url, headers=self.h)
        return response.json()

    def get_pokemonlist(self):
        pokemonlist = []
        for pokemon in self.response['results']:
            temp_dict = {
                'name': pokemon['name'],
                'url': f"/pokemon/{pokemon['name']}"
            }
            pokemonlist.append(temp_dict)
        return pokemonlist

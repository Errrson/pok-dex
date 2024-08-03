import requests
class PokemonListClass:

    #https://pokeapi.co/api/v2/pokemon-species usar este endpoint
    def __init__(self):
        self.url = "https://pokeapi.co/api/v2/pokemon-species?limit=19999"
        self.h = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
        self.response = requests.get(self.url, headers=self.h)

    def get_pokemonlist(self):        
        pokemonlist = []
        data_poke = self.response.json()
        for pokemon in data_poke['results']:            
            temp_dict = {
                'name': pokemon['name'],
                'url': f"/pokemon/{pokemon['name']}"
            }

            pokemonlist.append(temp_dict)

        return pokemonlist
    
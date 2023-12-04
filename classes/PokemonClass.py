# Resumen: Crear una clase Python llamada Pokemon para interactuar con la PokeAPI.

# Importar la biblioteca requests para realizar consultas HTTP

# Definir la clase Pokemon

# Crear el método constructor con un parámetro obligatorio (nombre o id)
# Completar la ruta del endpoint usando el parámetro
# Realizar la consulta y guardar la respuesta como atributo si es exitosa
# Manejar errores si la respuesta no es exitosa

# Crear el método para obtener el nombre del Pokemon

# Crear el método para obtener el número de la Pokedex del Pokemon

# Crear el método para obtener la URL de la imagen del Pokemon

# Obtener altura, peso, lista de tipos y lista de stats

# Ejemplo de uso:
# mi_pokemon = Pokemon("charizard")
# print(mi_pokemon.get_name())
# print(mi_pokemon.get_pokedex_number())
# print(mi_pokemon.get_image_url())

import requests


class PokemonClass:

    def __init__(self, name):
        url_base = "https://pokeapi.co/api/v2/pokemon/"
        self.main_endpoint = url_base + name
        self.h = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
        self.response = self.get_response(self.main_endpoint)

    def get_response(self, url):
        response = requests.get(url, headers=self.h)
        return response.json()

    def get_name(self):
        return self.response['name']

    def get_num_pokedex(self):
        return self.response['id']

    def get_url_sprite(self):
        return self.response['sprites']['front_default']

    def get_url_sprite_shiny(self):
        return self.response['sprites']['front_shiny']

    def get_weight(self):
        return self.response['weight']

    def get_height(self):
        return self.response['height']

    def get_types(self):
        list_types = []
        for type_poke in self.response['types']:
            list_types.append(type_poke['type']['name'])
        return list_types

    def get_stats(self):
        list_stats = []
        for stat_poke in self.response['stats']:
            stat = {'name': stat_poke['stat']['name'],
                    'value': stat_poke['base_stat']}
            list_stats.append(stat)
        return list_stats

    def get_evolution_chain(self):
        list_evolutions = []
        species_json = self.get_response(self.response['species']['url'])
        evolution_json = self.get_response(
            species_json['evolution_chain']['url'])

        evolution_step_json = self.get_response(
            evolution_json['chain']['species']['url'])
        evolutions = {'name': evolution_json['chain']['species']['name'],
                      'id': evolution_step_json['id']}
        list_evolutions.append(evolutions)

        evolution_first = evolution_json['chain']['evolves_to']
        if evolution_first:
            evolution_step_json = self.get_response(
                evolution_first[0]['species']['url'])
            evolutions = {'name': evolution_first[0]['species']['name'],
                          'id': evolution_step_json['id']}
            list_evolutions.append(evolutions)

            evolution_second = evolution_first[0]['evolves_to']
            if evolution_second:
                evolution_step_json = self.get_response(
                    evolution_second[0]['species']['url'])
                evolutions = {'name': evolution_second[0]['species']['name'],
                              'id': evolution_step_json['id']}
            list_evolutions.append(evolutions)

        return list_evolutions

    def get_description(self):
        species_json = self.get_response(self.response['species']['url'])
        description_original = species_json['flavor_text_entries'][1]['flavor_text']
        description = description_original.replace(
            "\n", " ").replace("\f", "")
        return description

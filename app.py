from flask import Flask, render_template
from classes.PokemonClass import PokemonClass
import requests

app = Flask(__name__)


@app.route("/")
def hello_world():
    url = "https://pokeapi.co/api/v2/pokemon/?offset=0&limit=1500"
    h = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
    response = requests.get(url, headers=h)
    pokedex = response.json()
    name_pokemons = pokedex['results']
    return render_template("index.html", pokemon=name_pokemons)


@app.route("/pokemon/<string:nombre_pokemon>")
def page_pokemon(nombre_pokemon):
    Pokemon = PokemonClass(nombre_pokemon)
    pokemon_details = {
        'name': Pokemon.get_name(),
        'order': Pokemon.get_num_pokedex(),
        'sprite': Pokemon.get_url_sprite(),
        'sprite_shiny': Pokemon.get_url_sprite_shiny(),
        'weight': Pokemon.get_weight(),
        'height': Pokemon.get_height(),
        'types': Pokemon.get_types(),
        'stats': Pokemon.get_stats(),
        'evs': Pokemon.get_evolution_chain(),
        'description': Pokemon.get_description()
    }

    return render_template("details_pokemon.html", pokemon=pokemon_details)


if __name__ == "__main__":
    app.run(debug=True)

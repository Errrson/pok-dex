from flask import Flask, render_template
from classes.PokemonClass import PokemonClass

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


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
        'types': Pokemon.get_stats(),
        'stats': Pokemon.get_stats(),
        'evs': Pokemon.get_evolution_chain(),
        'description': Pokemon.get_description()
    }

    return render_template("details_pokemon.html", pokemon=pokemon_details)


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template
from classes.PokemonClass import PokemonClass

app = Flask(__name__)


# @app.route("/")
# def hello_world():
#     Pokemon_list = PokemonClass.get_response(
#         "https://pokeapi.co/api/v2/pokemon?limit=1000")
#     return render_template("index.html", pokemon_list=Pokemon_list)


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

    return render_template("pokemon_page.html", details=pokemon_details)


if __name__ == "__main__":
    app.run(debug=True)

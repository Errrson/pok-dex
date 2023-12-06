from flask import Flask, render_template, request, redirect, url_for
from classes.PokemonClass import PokemonClass
from classes.PokemonListClass import PokemonListClass


app = Flask(__name__)


@app.route("/")
def index():
    PokeList = PokemonListClass()
    pokemonlist = PokeList.get_pokemonlist()
    return render_template("index.html", pokemonlist=pokemonlist)


@app.route("/search", methods=['POST'])
def search_pokemon():
    if request.method == 'POST':
        current_search = request.form.get("search")

    return redirect(url_for("page_pokemon", nombre_pokemon=current_search))


@app.route("/pokemon/<string:nombre_pokemon>")
def page_pokemon(nombre_pokemon):
    Pokemon = PokemonClass(nombre_pokemon)
    if Pokemon.response == False:
        return render_template("not_found.html")

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
        'description': Pokemon.get_description(),
        'next_pokemon': Pokemon.get_next_pokemon(),
        'previous_pokemon': Pokemon.get_previous_pokemon()
    }

    return render_template("details_pokemon.html", pokemon=pokemon_details)


if __name__ == "__main__":
    app.run(debug=True)

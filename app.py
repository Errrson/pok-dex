from flask import Flask, render_template
from functions.pokemon_service import get_saludo, get_pokemon_list, get_pokemon

app = Flask(__name__)


@app.route("/")
def hello_world():
    pokemon_list = get_pokemon_list(
        "https://pokeapi.co/api/v2/pokemon?limit=1000")
    return render_template("index.html", pokemon_list=pokemon_list)


@app.route("/pokemon/<string:nombre_pokemon>")
def page_pokemon(nombre_pokemon):
    pokemon_details = get_pokemon(
        "https://pokeapi.co/api/v2/pokemon/" + nombre_pokemon)

    return render_template("pokemon_page.html", details=pokemon_details)


if __name__ == "__main__":
    app.run(debug=True)

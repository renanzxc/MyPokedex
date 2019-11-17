from flask import Flask, render_template, jsonify
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search_pokemon/<string:pokemonName>')
def search_pokemon(pokemonName):
    pokemons = pd.read_csv(os.getcwd()+"/pokemon.csv")
    pokemonName = pokemonName.capitalize()
    result = pokemons[pokemons["name"].str.match(pokemonName)][["name","type1","hp","attack","defense","sp_attack","sp_defense","speed",
"abilities"]]
    if(result.empty):
        return jsonify({'status':'2'})
    else:
        num = result.index.tolist()
        result = result.to_json()
        return jsonify({'status':'1', "pokemons": result, "numPokes": num})

if __name__ == "__main__":
    app.run(debug=True)
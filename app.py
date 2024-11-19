from flask import Flask, request, render_template
import requests

app = Flask(__name__)

SWAPI_URL = 'https://swapi.py4e.com/api/'

@app.route('/')
def homepage():
    return render_template('results.html', context = None)

@app.route('/results', methods = ['GET', 'POST'])
def search():

    character_id = request.form.get('character_index')
    response_character = requests.get(f'{SWAPI_URL}people/{character_id}')

    if response_character.status_code == 200:
            character_data = response_character.json()

            context = {

                'name': character_data.get('name', 'N/A'),
                'height': character_data.get('height', 'N/A'),
                'mass': character_data.get('mass', 'N/A'),
                'hair_color': character_data.get('hair_color', 'N/A'),
                'eye_color': character_data.get('eye_color', 'N/A'),

            }

    else: 

            context = {'error': 'Invalid character ID. Please try again.'}

    return render_template('results.html', context = context)

if __name__ == '__main__':
    app.run(debug = True)
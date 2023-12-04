# app.py

from flask import Flask, jsonify, request
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# In-memory storage for the number to guess
game_data = {
    'number_to_guess': None
}

@app.route('/start', methods=['GET'])
def start_game():
    game_data['number_to_guess'] = random.randint(1, 100)
    return jsonify({'message': 'New game started'}), 200

@app.route('/guess', methods=['POST'])
def guess():
    guess = request.json.get('guess')
    number_to_guess = game_data['number_to_guess']

    if not number_to_guess:
        return jsonify({'message': 'Start a new game first'}), 400

    if guess < number_to_guess:
        return jsonify({'message': 'Too low'}), 200
    elif guess > number_to_guess:
        return jsonify({'message': 'Too high'}), 200
    else:
        return jsonify({'message': 'Correct!'}), 200

if __name__ == '__main__':
    app.run(debug=True)

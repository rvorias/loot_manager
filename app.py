# app.py
from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth
from dotenv import load_dotenv
import os

from loot_manager import utils

app = Flask(__name__)

load_dotenv()

app.config['BASIC_AUTH_USERNAME'] = os.getenv('BASIC_AUTH_USERNAME')
app.config['BASIC_AUTH_PASSWORD'] = os.getenv('BASIC_AUTH_PASSWORD')
app.config['BASIC_AUTH_FORCE'] = True
basic_auth = BasicAuth(app)


@app.route('/pop_prompt/', methods=['GET'])
def pop_prompt():
    # Retrieve the name from url parameter
    item_class = request.args.get("class", None)
    prompt, n_prompts = utils.pop_prompt(item_class)

    response = {}

    response["prompt"] = prompt[0]
    response["template"] = prompt[1]
    response["remaining_prompts"] = n_prompts

    # Return the response in json format
    return jsonify(response)


@app.route('/clear_cache/', methods=['GET'])
def clear_cache():
    utils.clear_cache()
    return jsonify({"msg": "cleared cache"})


# A welcome message to test our server
@app.route('/')
def index():
    return """
    <h1>APIS</h1>
    - /pop_prompt/?class=None  [GET] : pops prompt from cache <br>
    - /clear_cache/ [GET] : clears cache backend
    
    """


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
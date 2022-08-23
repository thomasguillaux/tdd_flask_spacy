import json

import spacy
from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin

from ner_client import NamedEntityClient

app = Flask(__name__)
CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

ner = spacy.load("en_core_web_sm")
ner = NamedEntityClient(ner)

@app.route('/')
@cross_origin()
def index():
    return render_template('index.html')

@app.route('/ner', methods=['POST'], strict_slashes=False)
@cross_origin()
def get_named_ents():
    data = request.get_json()
    result = ner.get_ents(data['sentence'])
    response = { "entities" : result.get('ents'), "html" : result.get('html')}
    return json.dumps(response)

if __name__ == "__main__":
    app.run(debug=True)

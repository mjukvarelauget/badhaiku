from flask import Flask, jsonify, request
from haiku import haiku_as_list
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def get_root():
    return "hjelp!"

@app.route('/bad/haiku', methods=["GET"])
def get_haiku():
    return jsonify({'haiku': haiku_as_list()})

if __name__ == '__main__':
    app.run(debug=True)
    
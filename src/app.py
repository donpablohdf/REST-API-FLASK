import os
import sys
import flask
import json
from flask import Flask
from flask import request
app = Flask(__name__)

todos = [{"label": "Sample", "done": False}]


@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = flask.jsonify(todos)
    return json_text


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    print("Incoming request with the following body", request_body)
    decoded_object = json.loads(request_body)
    todos.append(decoded_object)
    return flask.jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    todos.pop(position)
    return flask.jsonify(todos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)

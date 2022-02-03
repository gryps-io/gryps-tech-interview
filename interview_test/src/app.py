from distutils.log import debug
import json
from flask import Flask, request, jsonify, make_response
from left_join import left_join

app = Flask(__name__)


# Test CURL 
# curl -X POST http://localhost:5000/ -H "Content-Type: application/json" --data '{"left_dict": {}, "right_dict": {}}'

@app.route("/", methods=['POST'])
def make_request():
    json_data = request.json
    left_dict = json_data.get("left_dict", {})
    right_dict = json_data.get("right_dict", {})
    left_key_to_match = json_data.get("left_key_to_match", "")
    right_key_to_match = json_data.get("right_key_to_match", "")
    keys_to_include = json_data.get("keys_to_include", [])
    result = left_join(left_dict,
                        right_dict,
                        left_key_to_match,
                        right_key_to_match,
                        keys_to_include)
    return make_response(jsonify(result), 200)

app.run(debug=True)
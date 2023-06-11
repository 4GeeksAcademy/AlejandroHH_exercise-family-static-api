"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def get_members():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "hello": "world",
        "family": members
    }


    return jsonify(response_body), 200

@app.route('/members/<int:id>', methods=['GET'])
def get_member(id):
    member = jackson_family.get_member(id)
    return jsonify(member), 200
    

    
    return jsonify({"message": "member not found"})

@app.route('/members', methods=['POST'])
def add_member():
    data = request.json

    jackson_family.add_member(data)

    return jsonify({"message": "new member added successfully"})







# @app.route('/members', methods=['POST'])
# def add_member():
#     data = request.json

#     id = data.get('id')
#     full_name = data.get('full_name')
#     last_name = data.get('last_name')
#     age = data.get('age')
#     lucky_numbers = data.get('lucky_numbers')

#     new_member = {
#         "id": id,
#         "first_name": full_name,
#         "last_name": last_name,
#         "age": age,
#         "lucky_numbers": lucky_numbers
#     }

#     jackson_family.add_member(new_member)

#     return jsonify("New member added successfully")


    
#     jackson_family.add_member(new_member)

#     return jsonify("New member added successfully")

# @app.route('/members/<int:id>', methods=['PUT'])
# def update_member():

#     pass

@app.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):
    member = jackson_family.get_member(id)
    print(member)

    return jsonify({"message": f"the member {id} has been successfully deleted"}), 200



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)

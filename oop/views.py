from flask import Flask,jsonify,json,request
from hello import GuestList
import re

event=Flask(__name__)
users = GuestList()
@event.route('/api/users',methods=['GET'])
def get_all_users():
    return jsonify({'Users':users.get_all_users()}),200

@event.route('/api/users',methods=['POST'])
def add_user():
    firstName = request.json['first_name']
    lastName = request.json['last_name']
    email = request.json['email']
    pin = request.json['password']

    if not isinstance(request.json['first_name'], str):
        return jsonify({'message' : "incorrect input"}), 400
    if firstName.strip() == "":
        return jsonify({'error': 'please enter your first_name'}), 400
    
    if lastName.strip() == "":
        return jsonify({'error': 'please enter your last_name'}), 400
    if not isinstance(request.json['last_name'], str):
        return jsonify({'message' : "incorrect input"}), 400
    if email.strip() == "":
        return jsonify({'error': 'please input your email'}), 400

    email_match=re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
    if email_match == None:
	    return "wrong email format"

     
    if not isinstance(request.json['password'], int):
        return jsonify({'error': 'please input numbers only'}), 400 

    
    users.add_user(firstName, lastName, email, pin)
    return jsonify({'message':'succussfully added a user'}),201

@event.route('/api/users/<int:user_id>',methods=['DELETE'])
def remove_user(user_id):
    users.remove_user(user_id)
    return jsonify({'message':' user removed succussfully'}),200


if __name__ == ('__main__'):
    event.run(debug=True)


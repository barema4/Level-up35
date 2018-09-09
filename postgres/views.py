import re
from flask import jsonify, request
from flask.views import MethodView
from data import DatabaseConnection


class AddUser(MethodView):
    
    def post(self):
        
        keys = ("first_name","last_name", "email", "password","sex")
        if not set(keys).issubset(set(request.json)):
            return jsonify({'Blank space': 'Your request has Empty feilds'}), 400

        if request.json['frist_name'] == "":
            return jsonify({'frist_name': 'enter user_name'}), 400

        if (' ' in request.json['frist_name']) == True:
            return jsonify({'message': 'frist_name should not contain any spaces'}), 400
        if request.json['last_name'] == "":
            return jsonify({'last_name': 'enter last_name'}), 400

        if (' ' in request.json['last_name']) == True:
            return jsonify({'message': 'last_name should not contain any spaces'}), 400

        if request.json['email'] == "":
            return jsonify({'email': 'enter email'}), 400

        if (' ' in request.json['email']) == True:
            return jsonify({'message': 'email should not contain any spaces'}), 400

        if request.json['password'] == "":
            return jsonify({'message': 'password should not contain any spaces'}), 400

        if (' ' in request.json['password']) == True:
            return jsonify({'Password': 'Password should not contain any spaces'}), 400

        pattern = r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$"
        if not re.match(pattern, request.json['email']):
            return jsonify({'email': 'Enter way of your email'}), 400

        if request.json['sex'] == "":
            return jsonify({'sex': 'enter male or female'}), 400

        

        user = DatabaseConnection()
        user_details = user.insert(request.json['first_name'],request.json['last_name'], request.json['email'], request.json['password'], request.json['sex'])
        if user_details == "email already exists":
            return jsonify({'message': user_details}), 401

        return jsonify({'message': user_details}), 201



class UserDetails(MethodView):
    
    def get(self, user_id):
        
        if user_id is None:
            user = DatabaseConnection()
            user_list = user.all_users()
            if user_list == "No one ":
                return jsonify({"user": user_list}), 404
            return jsonify({"user": user_list})

        user = DatabaseConnection()
        user_list = user_id.get_single_user(user_id)
        if user_list == "Not one":
            return jsonify({"user":user_list}), 404
        return jsonify({"user": user_list})







class RmoveUser(MethodView):
    
    def delete(self, user_id):
        
        
        user = DatabaseConnection()
        user_data = user.delete_user(user_id)
        return jsonify({
            'user data deleted': user_data
            })



       
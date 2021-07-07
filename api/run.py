from flask import Flask, jsonify, json, request


app = Flask(__name__)
user_list = [{'name': 'sam', 'sex': 'male','email':'samrubarema6@gmail.com','user_id':1},
             {'name': 'jacob', 'sex': 'male','email':'jacob@gmail.com','user_id':2},
             {'name': 'Susan', 'sex': 'female','email':'susanw@gmail.com','user_id':3}]

@app.route('/api/users', methods=['GET','POST'])
def get_users():


    
    if request.method == 'GET':

        return jsonify({'user_list': user_list})
    else:
        xl = [user for user in user_list]

        user_id = len(xl)+1
        users = {'name':request.json['name'], 'sex': request.json['sex'],'email': request.json['email'],'user_id':user_id}
        for user in user_list:
             if user == users:

                 return "user already exist"
        user_list.append(users)

        return jsonify({'user_list' : user_list})
    
        

@app.route('/api/delete_user/<int:user_id>', methods=['DELETE'])
def removeOne(user_id):
    user1 = [user for user in user_list if user['user_id'] == user_id]
    user_list.remove(user1[0])
    return jsonify({'user_list' : user_list})



if __name__ == '__main__':
    app.run(debug=True)
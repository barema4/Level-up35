from flask import Flask, Request, jsonify, json, request


app = Flask(__name__)
user_list = [{'name': 'sam', 'sex': 'male'}, {'name': 'jacob', 'sex': 'male'}, {'name': 'Susan', 'sex': 'female'}]


@app.route('/api/', methods=['GET','POST'])
def get_users():
    if request.method == 'GET':

        return jsonify({'user_list': user_list})
    else:
        users = {'name':request.json['name'], 'sex': request.json['sex']}
        user_list.append(users)
        return jsonify({'user_list' : user_list})

@app.route('/api/<string:name>', methods=['DELETE'])
def removeOne(name):
    user1 = [user for user in user_list if user['name'] == name]
    user_list.remove(user1[0])
    return jsonify({'user_list' : user_list})



if __name__ == '__main__':
    app.run(debug=True)
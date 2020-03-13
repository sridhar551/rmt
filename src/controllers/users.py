
from flask import Flask, request, jsonify, Blueprint
# from models import db, Users
from src.models.users import Users, UserSchema
from src.models import db

# app = Flask(__name__)
# app.config['DEBUG'] = True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://sridhar:5551@localhost/resource_management'
# db.init_app(app)

user_api = Blueprint('user_api', __name__)
user_schema = UserSchema()

# @app.route("/")
# def main():
#     return 'Hello World !'

@user_api.route('/', methods=['POST', 'GET'])
def data():
    
    # POST a data to database
    if request.method == 'POST':
        body = request.json
        print(body)
        name = body['name']
        email = body['email']
        password = body['password']

        data = Users(name, email, password)
        db.session.add(data)
        db.session.commit()

        return jsonify({
            'status': 'Data is posted to PostgreSQL!'})
    
    # GET all data from database & sort by id
    if request.method == 'GET':
        # data = User.query.all()
        data = Users.query.order_by(Users.id).all()
        # results = []
        # for i in data:
        #     dataDict = {
        #         "id" : i.id,
        #         "name" : i.name,
        #         "email" : i.email,
        #         "password" : i.password
        #     }
        #     results.append(dataDict)
        results = [
            {
                "id" : i.id,
                "name" : i.name,
                "email" : i.email,
                "password" : i.password,
                "created_at" : i.created_at,
                "modified_at" : i.modified_at
            } for i in data]
        return jsonify(results)

@user_api.route('/<string:id>', methods=['GET', 'DELETE', 'PUT'])
def onedata(id):

    # GET a specific data by id
    if request.method == 'GET':
        data = Users.query.get(id)
        print(data)
        dataDict = {
            'id': data.id,
            'name': data.name,
            'email' : data.email,
            'password': data.password,
            'created_at' : data.created_at,
            'modified_at' : data.modified_at
        }
        return jsonify(dataDict)
        
    # DELETE a data
    if request.method == 'DELETE':
        delData = Users.query.filter_by(id=id).first()
        db.session.delete(delData)
        db.session.commit()
        return jsonify({'status': 'Data '+id+' is deleted from PostgreSQL!'})

    # UPDATE a data by id
    if request.method == 'PUT':
        body = request.json
        newName = body['name']
        newEmail = body['email']
        newPassword = body['password']
        editData = Users.query.filter_by(id=id).first()
        editData.name = newName
        editData.email = newEmail
        editData.password = newPassword
        db.session.commit()
        return jsonify({'status': 'Data '+id+' is updated from PostgreSQL!'})


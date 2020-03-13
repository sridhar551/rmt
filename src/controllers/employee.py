from flask import Flask, request, jsonify, Blueprint
# from models import db, Users
from src.models.employee import Employee, EmployeeSchema
from src.models import db

# app = Flask(__name__)
# app.config['DEBUG'] = True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://sridhar:5551@localhost/resource_management'
# db.init_app(app)

employee_api = Blueprint('employee_api', __name__)
employee_schema = EmployeeSchema()


# @app.route("/")
# def main():
#     return 'Hello World !'

@employee_api.route('/', methods=['POST', 'GET'])
def data():
    # POST a data to database
    if request.method == 'POST':
        body = request.json
        print(body)
        firstname = body['firstname']
        lastname = body['lastname']
        designation = body['designation']
        phone_number = body['phone_number']

        data = Employee(firstname, lastname, designation, phone_number)
        db.session.add(data)
        db.session.commit()

        return jsonify({
            'status': 'Data is posted to PostgreSQL!'})

    # GET all data from database & sort by id
    if request.method == 'GET':
        # data = User.query.all()
        data = Employee.query.order_by(Employee.id).all()
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
                "id": i.id,
                "firstname": i.firstname,
                "lastname": i.lastname,
                "phone_number": i.phone_number,
                "designation" : i.designation,
                "created_at" : i.created_at,
                "modified_at" : i.modified_at
            } for i in data]
        return jsonify(results)


"""@user_api.route('/<string:id>', methods=['GET', 'DELETE', 'PUT'])
def onedata(id):
    # GET a specific data by id
    if request.method == 'GET':
        data = Users.query.get(id)
        print(data)
        dataDict = {
            'id': data.id,
            'name': data.name,
            'email': data.email,
            'password': data.password,
            'created_at': data.created_at,
            'modified_at': data.modified_at
        }
        return jsonify(dataDict)

    # DELETE a data
    if request.method == 'DELETE':
        delData = Users.query.filter_by(id=id).first()
        db.session.delete(delData)
        db.session.commit()
        return jsonify({'status': 'Data ' + id + ' is deleted from PostgreSQL!'})

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
        return jsonify({'status': 'Data ' + id + ' is updated from PostgreSQL!'})
"""

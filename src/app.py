# from flask import Flask, request, jsonify
# # from models import db, Users
# # from src.models.users import db, Users
#
# app = Flask(__name__)
# app.config['DEBUG'] = True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://sridhar:5551@localhost/resource_management'
# db.init_app(app)

# src/app.py

from flask import Flask

from .config import app_config
from .models import db

# import user_api blueprint
# from .views.UserView import user_api as user_blueprint
# from .views.BlogpostView import blogpost_api as blogpost_blueprint
from src.controllers.users import user_api as user_blueprint
from src.controllers.employee import employee_api as employee_blueprint


def create_app(env_name):
    """
    Create app
    """

    # app initiliazation
    app = Flask(__name__)

    app.config.from_object(app_config[env_name])

    # initializing bcrypt and db
    # bcrypt.init_app(app)
    db.init_app(app)

    app.register_blueprint(user_blueprint, url_prefix='/api/v1/users')
    app.register_blueprint(employee_blueprint, url_prefix='/api/v1/employee')

    @app.route('/', methods=['GET'])
    def index():
        """
        example endpoint
        """
        return 'Congratulations!'

    return app
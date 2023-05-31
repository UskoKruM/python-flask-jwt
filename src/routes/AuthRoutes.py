from flask import Blueprint, request, jsonify

# Models
from src.services.models.User import User
# Security
from src.utils.Security import Security
# Services
from src.services.AuthService import AuthService

main = Blueprint('auth_blueprint', __name__)


@main.route('/', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']

    _user = User(0, username, password, None)
    authenticated_user = AuthService.login_user(_user)

    if (authenticated_user != None):
        encoded_token = Security.generate_token(authenticated_user)
        return jsonify({'success': True, 'token': encoded_token})
    else:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401

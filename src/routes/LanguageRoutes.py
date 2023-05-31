from flask import Blueprint, request, jsonify

# Errors
from src.utils.errors.CustomException import CustomException
# Security
from src.utils.Security import Security
# Services
from src.services.LanguageService import LanguageService

main = Blueprint('language_blueprint', __name__)


@main.route('/')
def get_languages():
    has_access = Security.verify_token(request.headers)

    if has_access:
        try:
            languages = LanguageService.get_languages()
            if (len(languages) > 0):
                return jsonify({'languages': languages, 'message': "SUCCESS", 'success': True})
            else:
                return jsonify({'message': "NOTFOUND", 'success': True})
        except CustomException:
            return jsonify({'message': "ERROR", 'success': False})
    else:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401

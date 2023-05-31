# Database
from src.database.db import get_connection
# Errors
from src.utils.errors.CustomException import CustomException
# Models
from .models.Language import Language


class LanguageService():

    @classmethod
    def get_languages(cls):
        try:
            connection = get_connection()
            languages = []
            with connection.cursor() as cursor:
                cursor.execute('call sp_listLanguages()')
                resultset = cursor.fetchall()
                for row in resultset:
                    language = Language(int(row[0]), row[1])
                    languages.append(language.to_json())
            connection.close()
            return languages
        except CustomException as ex:
            raise CustomException(ex)

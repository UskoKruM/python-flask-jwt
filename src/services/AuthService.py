# Database
from src.database.db import get_connection
# Errors
from src.utils.errors.CustomException import CustomException
# Models
from .models.User import User


class AuthService():

    @classmethod
    def login_user(cls, user):
        try:
            connection = get_connection()
            authenticated_user = None
            with connection.cursor() as cursor:
                cursor.execute('call sp_verifyIdentity(%s, %s)', (user.username, user.password))
                row = cursor.fetchone()
                if row != None:
                    authenticated_user = User(int(row[0]), row[1], None, row[2])
            connection.close()
            return authenticated_user
        except CustomException as ex:
            raise CustomException(ex)

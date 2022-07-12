from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Emails:
    db_name = 'email_validation_db'
    def __init__( self, data ):
        self.id = data['id']
        self.email = data['email']


    @classmethod
    def save( cls, data ):
        query = "INSERT INTO emails ( email ) VALUE ( %(email)s )"
        return connectToMySQL( cls.db_name ).query_db( query, data )

    @classmethod
    def delete( cls, data ):
        query = "DELETE FROM emails WHERE id = ( %(id)s )"
        return connectToMySQL( cls.db_name ).query_db( query, data )

    @classmethod
    def view_all_emails( cls ):
        query = "SELECT * FROM emails"
        return connectToMySQL( cls.db_name ).query_db( query )


    @staticmethod
    def email_validation_regex( data ):
        is_valid = True
        if not EMAIL_REGEX.match(data['email']):
            flash('Invalid email address!')
            is_valid = False
        return is_valid

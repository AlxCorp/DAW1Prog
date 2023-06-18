import mysql.connector


class SqlDAO:
    def __init__(self):
        self.__database = None

    def create_database(self, user):

# Database Connection (Singleton Pattern)

from sqlalchemy import create_engine

class DatabaseConnection:
    __instance = None

    @staticmethod
    def get_instance():
        if DatabaseConnection.__instance is None:
            DatabaseConnection()
        return DatabaseConnection.__instance

    def __init__(self):
        if DatabaseConnection.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.connection = self.create_connection()
            DatabaseConnection.__instance = self

    def create_connection(self):
        return create_engine('sqlite:///food_ordering.db')
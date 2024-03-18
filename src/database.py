import mysql.connector


# Creating connection object
class DatabaseConfig:

    def database(self):
        my_db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            db='smart_parking',
        )

        return my_db


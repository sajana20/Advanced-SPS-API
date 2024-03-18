from src.database import DatabaseConfig
import json


class UserRepository():

    def get_user_details(self, email, password):
        print("yooo")
        database_config = DatabaseConfig()
        db = database_config.database()

        try:
            with db.cursor() as cursor:
                print("yo1")
                print(email, password)
                sql = f"SELECT id FROM user WHERE email ='{email}' AND password = '{password}'"
                print(sql)
                cursor.execute(sql)

                # Fetch all rows
                data = cursor.fetchone()
                print("gg1")
                print(data)
                if data == None:

                    return json.dumps({"error": "Invalid email"}), 401


                json_data = json.dumps({'id': data[0]})
                db.close()
                return json_data

        finally:
            db.close()

    def set_user_details(self, user_name, email, password):

        database_config = DatabaseConfig()
        db = database_config.database()

        try:
            with db.cursor() as cursor:
                print("yo1")
                print(email, password)
                sql = f"INSERT INTO user (user_name, email, password) VALUES ('{user_name}', '{email}', '{password}')"
                print(sql)
                cursor.execute(sql)
                db.commit()
                return "User Added Successfully"

        finally:
            db.close()


    # def delete_user(self, id):
    #     database_config = DatabaseConfig()
    #     db = database_config.database()
    #
    #     try:
    #         with db.cursor() as cursor:
    #             sql = f"DELETE FROM user WHERE id = {id}"
    #             print(sql)
    #             cursor.execute(sql)
    #             db.commit()
    #             return "User Deleted"
    #
    #     finally:
    #         db.close()


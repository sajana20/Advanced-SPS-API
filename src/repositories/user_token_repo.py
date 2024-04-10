from src.database import DatabaseConfig

database_config = DatabaseConfig()

class UserTokenRepository():
    def get_user_token(self, slot_id):
        db = database_config.database()
        try:
            with db.cursor() as cursor:
                sql = f"SELECT ut.token FROM parking_area pa JOIN user_token ut ON pa.user_id = ut.user_id WHERE pa.slot_id = {slot_id}"
                cursor.execute(sql)

                # Fetch all rows
                rows = cursor.fetchall()
                data = []
                for row in rows:
                    data.append(row[0]
                    )

                db.close()
                return data
        finally:
            db.close()

    def set_user_token(self, user_id, token):
        db = database_config.database()
        try:
            with db.cursor() as cursor:
                sql = f"INSERT INTO user_token (user_id, token) VALUES ('{user_id}', '{token}')"
                cursor.execute(sql)
                db.commit()
                return "Successfully Set Token"
        except Exception as err:
            print("Failed to save token." + str(err))
            return "Failed to save token"
        finally:
            db.close()

    def delete_user_token(self, user_id):
        db = database_config.database()
        try:
            with db.cursor() as cursor:
                sql = f"DELETE FROM user_token WHERE user_id = {user_id}"
                cursor.execute(sql)
                db.commit()
                return "Token deleted successfully"
        finally:
            db.close()
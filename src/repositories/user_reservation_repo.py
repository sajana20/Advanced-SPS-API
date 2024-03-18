from src.database import DatabaseConfig
import json


class UserReservationRepository():
    def update_user_reservation(self, user_id, slot_id):
        database_config = DatabaseConfig()
        db = database_config.database()

        try:
            with db.cursor() as cursor:
                print("yo1")
                print(user_id, slot_id)
                sql = f"INSERT INTO parking_reservation (user_id, slot_id, video_data) VALUES ('{user_id}', '{slot_id}')"
                print(sql)
                cursor.execute(sql)
                db.commit()
                return "User Reservation Added Successfully"

        finally:
            db.close()

    def get_user_reservation(self, user_id):
        database_config = DatabaseConfig()
        db = database_config.database()

        try:
            with db.cursor() as cursor:
                print("yo1")
                print(user_id)
                sql = f"SELECT * FROM parking_reservation WHERE user_id = {user_id}"
                print(sql)
                cursor.execute(sql)
                # Fetch all rows
                rows = cursor.fetchall()
                print("rowas")
                print(rows)
                data = []
                for row in rows:
                    data.append(
                        {
                            'id': row[0],
                            'userId': row[1],
                            'slotId': row[2],
                            'reservedDate': row[3].isoformat(),
                            'active': row[4],

                        }
                    )
                json_data = json.dumps(data)
                print(json_data)
                db.close()
                return json_data

        finally:
            db.close()
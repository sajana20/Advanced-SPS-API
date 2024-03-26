from src.database import DatabaseConfig
import json
from datetime import datetime



class UserReservationRepository():
    def update_user_reservation(self, user_id, slot_id, active):
        database_config = DatabaseConfig()
        db = database_config.database()
        now = datetime.now()

        try:
            with db.cursor() as cursor:
                sql = f"INSERT INTO parking_reservation (user_id, slot_id, reserved_date, active) VALUES ({user_id}, {slot_id},'{now}', {active})"
                cursor.execute(sql)
                db.commit()
                return "User Reservation Added Successfully"

        finally:
            db.close()

    def update_activie_status(self, active, slot_id):
        database_config = DatabaseConfig()
        db = database_config.database()

        try:
            with db.cursor() as cursor:
                sql = f"UPDATE parking_reservation SET active = {active} WHERE slot_id= {slot_id} AND active = 1"
                cursor.execute(sql)
                db.commit()
                return "User Reservation deactivated"

        finally:
            db.close()


    def get_user_reservation(self, user_id):
        database_config = DatabaseConfig()
        db = database_config.database()

        try:
            with db.cursor() as cursor:
                sql = f"SELECT * FROM parking_reservation WHERE user_id = {user_id} ORDER BY reserved_date DESC"
                cursor.execute(sql)
                # Fetch all rows
                rows = cursor.fetchall()

                data = []
                for row in rows:
                    data.append(
                        {
                            'id': row[0],
                            'userId': row[1],
                            'slotId': row[2],
                            'reservedDate': row[3].strftime('%Y-%m-%d %X'),
                            'active': row[4],

                        }
                    )
                json_data = json.dumps(data)
                db.close()
                return json_data

        finally:
            db.close()
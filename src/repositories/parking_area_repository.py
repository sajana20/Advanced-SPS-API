from src.database import DatabaseConfig
import json

database_config = DatabaseConfig()


class ParkingAreaRepository():

    def get_parking_availability(self):
        db = database_config.database()
        try:
            with db.cursor() as cursor:
                sql = f"SELECT slot_id, user_id, availability, poi FROM parking_area"
                cursor.execute(sql)

                # Fetch all rows
                rows = cursor.fetchall()
                data = []
                for row in rows:
                    data.append(
                        {
                            'slotId': row[0],
                            'userId': row[1],
                            'availability': row[2],
                            'poi': row[3]
                        }
                    )
                json_data = json.dumps(data)
                db.close()
                return json_data
        finally:
            db.close()

    def update_parking_availability(self, user_id, slot_id, availability):
        db = database_config.database()
        try:
            with db.cursor() as cursor:
                if user_id == '0':
                    user_id == None

                # Read data from database
                sql = f"UPDATE parking_area SET user_id = {user_id},availability = {availability} WHERE slot_id = {slot_id}";
                cursor.execute(sql)
                db.commit()
                db.close()

        finally:
            db.close()

    def checkAvailability(self, slot_id):
        db = database_config.database()
        try:
            with db.cursor() as cursor:
                sql = f"SELECT 1 FROM parking_area WHERE slot_id = {slot_id} AND user_id <> 0"
                cursor.execute(sql)
                data = cursor.fetchone()
                json_data = json.dumps({'availability': 1 if data is None else 0})
                db.close()
                return json_data
        finally:
            db.close()

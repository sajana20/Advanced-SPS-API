from src.database import DatabaseConfig
import mysql.connector
import json

database_config = DatabaseConfig()


class ParkingAreaRepository():

    def get_parking_availability(self):
        db = database_config.database()
        try:
            with db.cursor() as cursor:
                # Read data from database
                sql = f"SELECT slot_id, availability FROM parking_area"
                cursor.execute(sql)

                # Fetch all rows
                rows = cursor.fetchall()
                print("rowas")
                print(rows)
                data = []
                for row in rows:
                    data.append(
                        {
                            'slotId': row[0],
                            'availability': row[1]
                        }
                    )
                json_data = json.dumps(data)
                print(json_data)
                db.close()
                return json_data
        finally:
            db.close()


    def update_parking_availability(self,user_id, slot_id, availability):
        db = database_config.database()
        try:
            with db.cursor() as cursor:
                print("user_id")
                print(user_id)
                print("slot_id")
                print(slot_id)
                print("availability")
                print(availability)

                # Read data from database
                sql = f"UPDATE parking_area SET user_id = {user_id},availability = {availability} WHERE slot_id = {slot_id}";
                print(sql)
                cursor.execute(sql)
                db.commit()
                db.close()

        finally:
            db.close()

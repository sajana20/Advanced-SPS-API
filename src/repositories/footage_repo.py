from src.database import DatabaseConfig
import json


class FootageRepository():

    def set_footage(self, slot_id, file_name):

        database_config = DatabaseConfig()
        db = database_config.database()

        try:
            with db.cursor() as cursor:
                reservation_sql = f"SELECT id FROM parking_reservation WHERE (slot_id = {slot_id} AND active = 1)"

                cursor.execute(reservation_sql)
                data = cursor.fetchone()
                if (data[0] != None):
                    reservation_id = data[0]

                    sql = f"INSERT INTO footage (reservation_id, file_name) VALUES ({reservation_id}, '{file_name}')"
                    cursor.execute(sql)
                    db.commit()
                    return "Footage SET Successfully"

        finally:
            db.close()

    def get_footage_file_name(self, reservation_id):
        database_config = DatabaseConfig()
        db = database_config.database()

        try:
            with db.cursor() as cursor:

                sql = f"SELECT file_name FROM footage WHERE reservation_id ={reservation_id}"
                cursor.execute(sql)

                # Fetch all rows
                rows = cursor.fetchall()

                data = []
                if rows == None:
                    return "No footage for the reservation"
                for row in rows:
                    data.append(
                        {
                            'fileName': row[0]
                        }
                    )

                json_data = json.dumps(data)
                db.close()
                return json_data

        finally:
            db.close()

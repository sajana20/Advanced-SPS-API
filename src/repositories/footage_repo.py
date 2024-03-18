from src.database import DatabaseConfig
import json


class FootageRepository():

    def set_footage(self, slot_id, file_name):
        print("called set footage")
        print(slot_id,file_name)


        database_config = DatabaseConfig()
        db = database_config.database()

        try:
            with db.cursor() as cursor:
                reservation_sql = f"SELECT id FROM parking_reservation WHERE (slot_id = {slot_id} AND active = 1)"
                print("fefe")
                print(reservation_sql)

                cursor.execute(reservation_sql)
                data = cursor.fetchone()
                print("data[0]")
                print(data[0])
                if(data[0] != None):
                    reservation_id = data[0]
                    print("reservation_sql")
                    print(reservation_sql)
                    print("reservation_id")
                    print(reservation_id)

                    sql = f"INSERT INTO footage (reservation_id, file_name) VALUES ({reservation_id}, '{file_name}')"
                    print("sql3")
                    print(sql)

                    cursor.execute(sql)
                    db.commit()
                    print("reserrrrr success")
                    return

        finally:
            db.close()

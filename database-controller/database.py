#! /usr/bin/env python3

import os
import psycopg2
import psycopg2.extras
import json

from dotenv import load_dotenv
load_dotenv()

db_name = os.getenv("POSTGRES_DB")
db_user = os.getenv("POSTGRES_USER")
db_pw = os.getenv("POSTGRES_PASSWORD")
meta_table = 'sensor_metadata'
data_table = 'sensor_data'
settings_table = 'user_settings'


class Database:
    def __init__(self):
        self.conn = psycopg2.connect(host="localhost",
                                     dbname=db_name,
                                     user=db_user,
                                     password=db_pw)

    def close_connection(self):
        self.conn.close()

    def get_sensor_list(self):
        c = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        c.execute(f"SELECT id, type, location FROM {meta_table};")

        sensor_list = []
        for sensor in c:
            sensor_list.append({
                "sensor_id": sensor[0],
                "type": sensor[1],
                "location": sensor[2],
            })

        return sensor_list

    def insert_data(self, sensor_id, location, value):
        try:
            c = self.conn.cursor()
            values = (sensor_id, location, value)
            c.execute(
                f"INSERT INTO {data_table} (sensor_id, location, value) VALUES (%s,%s,%s);",
                values)
            self.conn.commit()
            return True
        except (Exception):
            return False

    def get_data(self, sensor_id):
        try:
            c = self.conn.cursor()
            values = (sensor_id, )
            c.execute(f"SELECT * FROM {data_table} WHERE sensor_id=%s;",
                      values)
            data = c.fetchall()
            return data
        except Exception as err:
            self.conn.rollback()
            print(err)
            return False

    def add_sensor(self, sensor_id, sensor_type, location):
        try:
            c = self.conn.cursor()
            values = (sensor_id, sensor_type, location)
            c.execute(
                f"INSERT INTO {meta_table} (id, type, location) VALUES (%s,%s,%s);",
                values)
            self.conn.commit()
            return True
        except Exception as err:
            self.conn.rollback()
            print(err)
            return False

    def delete_sensor(self, sensor_id):
        try:
            self.deactivate_sensor(sensor_id)
            c = self.conn.cursor()
            c.execute(f"DELETE FROM {meta_table} WHERE id=%s;", (sensor_id, ))
            self.conn.commit()
            return True
        except Exception as err:
            self.conn.rollback()
            print(err)
            return False

    def get_active_sensors(self):
        c = self.conn.cursor()
        c.execute(
            f"SELECT value FROM {settings_table} WHERE name='active_sensors';")

        sensor_list = list(c.fetchone())[0]
        return sensor_list

    def activate_sensor(self, sensor_id):
        try:
            active_sensors = self.get_active_sensors()
            all_sensors = []

            for sensor in self.get_sensor_list():
                all_sensors.append(sensor['sensor_id'])

            if (not sensor_id in active_sensors and sensor_id in all_sensors):
                active_sensors.append(sensor_id)
                c = self.conn.cursor()
                sensors = json.dumps(active_sensors)

                values = (sensors, )
                c.execute(
                    f"""INSERT INTO {settings_table} (name, value) VALUES ('active_sensors',%s) 
                    ON CONFLICT (name) DO UPDATE SET value = excluded.value;""",
                    values)
                self.conn.commit()
                return True
            return False

        except Exception as err:
            self.conn.rollback()
            print(err)
            return False

    def deactivate_sensor(self, sensor_id):
        try:
            active_sensors = self.get_active_sensors()
            all_sensors = []

            for sensor in self.get_sensor_list():
                all_sensors.append(sensor['sensor_id'])

            if (sensor_id in active_sensors and sensor_id in all_sensors):
                active_sensors.remove(sensor_id)
                c = self.conn.cursor()
                sensors = json.dumps(active_sensors)

                values = (sensors, )
                c.execute(
                    f"""INSERT INTO {settings_table} (name, value) VALUES ('active_sensors',%s) 
                    ON CONFLICT (name) DO UPDATE SET value = excluded.value;""",
                    values)
                self.conn.commit()
                return True
            return False

        except Exception as err:
            self.conn.rollback()
            print(err)
            return False

    def get_setting(self, name):
        c = self.conn.cursor()
        c.execute(f"SELECT * FROM {settings_table} WHERE name=%s", (name, ))
        data = c.fetchone()
        return {"name": data[0], "value": data[1]}

    def update_setting(self, name, value):
        values = (value, name)
        c = self.conn.cursor()
        c.execute(f"UPDATE {settings_table} SET value=%s WHERE name=%s",
                  values)
        self.conn.commit()
        return {'name': name, 'value': value}


if __name__ == "__main__":
    db = Database()

    # db.delete_sensor("123sensor")
    # sensors = db.get_sensor_list()
    # print(sensors)

    db.add_sensor("1sensor", "humidity", "ceiling")
    db.activate_sensor('1sensor')
    # print(db.get_active_sensors())

    # s0 = sensors[0]

    # x = 1
    # target = 25
    # while x < target:
    #     progress = float((x / target)) * 100.0
    #     db.insert_data({
    #         "sensor_id": s0['sensor_id'],
    #         "location": s0['location'],
    #         "value": progress,
    #     })
    #     print(progress)
    #     x += 1

    db.close_connection()

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

    def insert_data(self, data):
        sensor_id = data['sensor_id']
        location = data['location']
        value = data['value']
        try:
            c = self.conn.cursor()
            values = (sensor_id, location, value)
            c.execute(
                f"INSERT INTO {data_table} (sensor_id, location, value) VALUES (%s,%s,%s);",
                values)
            self.conn.commit()
            return data
        except (Exception):
            return False


if __name__ == "__main__":
    db = Database()

    sensors = db.get_sensor_list()
    # print(sensors)
    s0 = sensors[0]

    x = 1
    target = 25
    while x < target:
        progress = float((x / target)) * 100.0
        db.insert_data({
            "sensor_id": s0['sensor_id'],
            "location": s0['location'],
            "value": progress,
        })
        print(progress)
        x += 1

    db.close_connection()

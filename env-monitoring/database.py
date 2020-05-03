#! /usr/bin/env python3

import sqlite3
import time


db_name = '../data/env_data.db'
table_name = 'sensor_data'
table_fields = """
    sensor_id TEXT NOT NULL,
    type TEXT,
    location TEXT,
    value REAL,
    created_at INTEGER
    """


class Database:
    def __init__(self):
        self.conn = sqlite3.connect(db_name)
        self.check_existing_db()

    def check_existing_db(self):
        c = self.conn.cursor()
        c.execute(
            f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")

        if(not c.fetchall()):
            x = self.conn.cursor()
            x.execute(
                f"CREATE TABLE '{table_name}' ({table_fields})")
            print(f"No table found, created table '{table_name}'.")

    def close_connection(self):
        self.conn.close()

    def insert_data(self, data):
        sensor_id = data['sensor_id']
        env_type = data['type']
        location = data['location']
        value = data['value']
        created = int(time.time())
        c = self.conn.cursor()
        values = (sensor_id, env_type, location, value, created, )
        c.execute(
            f"INSERT INTO '{table_name}' VALUES (?,?,?,?,?)", values)
        self.conn.commit()


if __name__ == "__main__":
    db = Database()
    x = 1
    target = 100
    while x < target:
        db.insert_data({
            "sensor_id": "23jj2",
            "type": "°C",
            "location": "room",
            "value": x,
        })
        print(float((x / target)) * 100.0)
        x += 1
    db.close_connection()

#! /usr/bin/env python3

import sqlite3
import time
import json

db_name = '../database/user_settings.db'
table_name = 'user_settings'
table_fields = """
    name TEXT NOT NULL UNIQUE,
    setting TEXT,
    created_at INTEGER
    """


class UserDB:
    def __init__(self):
        self.conn = sqlite3.connect(db_name)
        self.check_existing_db()

    def check_existing_db(self):
        c = self.conn.cursor()
        c.execute(
            f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'"
        )

        if (not c.fetchall()):
            x = self.conn.cursor()
            x.execute(f"CREATE TABLE '{table_name}' ({table_fields})")

            setting = json.dumps([{
                "date": "start",
                "on": [14, 12],
                "off": [14, 14]
            }])
            self.insert_data({'name': 'light_cycle', 'setting': setting})

            print(f"No table found, created table '{table_name}'.")

    def close_connection(self):
        self.conn.close()

    def insert_data(self, data):
        values = (data['name'], data['setting'], int(time.time()))
        c = self.conn.cursor()
        c.execute(f"INSERT INTO '{table_name}' VALUES (?,?,?)", values)
        self.conn.commit()

    def get_setting(self, name):
        c = self.conn.cursor()
        c.execute(f"SELECT * FROM '{table_name}' WHERE name='{name}'")
        data = c.fetchone()
        return {"name": data[0], "setting": data[1], "created": data[2]}

    def update_setting(self, data):
        name = data['name']
        values = (name, data['setting'], int(time.time()))
        c = self.conn.cursor()
        c.execute(
            f"INSERT INTO '{table_name}' VALUES (?,?,?) ON DUPLICATE KEY UPDATE 'name' = '{name}'",
            values)
        self.conn.commit()
        return c.fetchall()


if __name__ == "__main__":
    db = UserDB()
    db.get_setting('light_cycle')
    # db.insert_data({
    #     "name": "light_cycle",
    #     "setting": "room",
    # })
    data = {
        "name":
        "light_cycle",
        "setting":
        json.dumps([{
            "date": "start",
            "on": [6, 0],
            "off": [22, 0]
        }, {
            "date": "2020-05-09",
            "on": [6, 0],
            "off": [22, 0]
        }, {
            "date": "2020-05-11",
            "on": [6, 0],
            "off": [22, 0]
        }, {
            "date": "2020-05-13",
            "on": [6, 0],
            "off": [22, 0]
        }])
    }
    db.update_setting(data)
    db.close_connection()

    input("Enter to delete db")
    import os
    os.remove(db_name)

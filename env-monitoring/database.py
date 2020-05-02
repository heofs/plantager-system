import sqlite3


db_name = '../data/env-data.db'
table_name = 'sensor-data'
table_fields = 'id INTEGER PRIMARY KEY, sensor_id TEXT, location TEXT, value REAL'


class Process:
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

    def insert_data(self):
        pass


if __name__ == "__main__":
    process = Process()
    process.close_connection()

import json
import sqlite3

class DataSource:
    def load(self):
        raise NotImplementedError


class JSONDataSource(DataSource):
    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):
        with open(self.file_path, "r") as file:
            return json.load(file)


class SQLiteDataSource(DataSource):
    def __init__(self, db_path, query):
        self.db_path = db_path
        self.query = query

    def load(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(self.query)
        data = cursor.fetchall()
        conn.close()
        return data

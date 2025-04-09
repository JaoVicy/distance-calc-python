import sqlite3

class DatabaseManager:
    def __init__(self, db_name="geo_points.db"):
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.connection:
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS points (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    latitude REAL NOT NULL,
                    longitude REAL NOT NULL,
                    distance REAL
                )
            """)

    def insert_point(self, latitude, longitude, distance):
        with self.connection:
            self.connection.execute("""
                INSERT INTO points (latitude, longitude, distance)
                VALUES (?, ?, ?)
            """, (latitude, longitude, distance))

    def fetch_all_points(self):
        with self.connection:
            return self.connection.execute("SELECT * FROM points").fetchall()

    def close(self):
        self.connection.close()

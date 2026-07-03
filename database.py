import sqlite3


def init_db():
    # Connect to (or create) the database file
    conn = sqlite3.connect("skymood.db")
    cursor = conn.cursor()

    # Create Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    # Create Mood Logs table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mood_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            date TEXT,
            weather_condition TEXT,
            mood TEXT,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    """)

    conn.commit()
    conn.close()
    print("Database initialized successfully!")


if __name__ == "__main__":
    init_db()

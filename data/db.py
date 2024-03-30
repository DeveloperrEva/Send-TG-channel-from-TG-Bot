import sqlite3
from datetime import datetime, timedelta

today = datetime.now().date()

try:
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()
    print("База данных успешно подключена к SQLite")
except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
    
def select():
    cursor.execute("SELECT channel_id FROM channel")

    data = cursor.fetchall()
    conn.commit()

    return data

def add(id):
    cursor.execute(
        "INSERT INTO channel (channel_id) VALUES (?)", (id)
    )
    conn.commit()
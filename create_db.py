import sqlite3

db = sqlite3.connect('moneyKeeper.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name TEXT,
    password TEXT,
    created datetime DEFAULT CURRENT_TIMESTAMP
)""")

sql.execute("""CREATE TABLE IF NOT EXISTS wallet (
    user_id TEXT,
    user_name TEXT,
    category TEXT,
    expense_type TEXT,
    price FLOAT,
    dates TIMESTAMP
)""")

db.commit()
db.close()
# import sqlite3
#
# db = sqlite3.connect('moneyKeeper.db')
# sql = db.cursor()
#
# def check_credential(userName, password):
#     items = sql.execute(f"SELECT id, user_name FROM users WHERE user_name ='{userName}'").fetchall()
#     if items == []:
#         sql.execute("INSERT INTO users(user_name, password) VALUES (?, ?)", (userName, password))
#         db.commit()
#         return None
#     else:
#         return 'this username is already taken'

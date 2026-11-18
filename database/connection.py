import sqlite3
def conectar():
 return sqlite3.connect("database.db",check_same_thread=False)

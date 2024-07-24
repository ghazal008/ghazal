import sqlite3


def connect():
    conn = sqlite3.connect('hotel.db')
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS passengers(id INTEGER PRIMARY KEY,name text,city text,year INTEGER,roomNo INTEGER)")
    conn.commit()
    conn.close()


def insert(name, city, year, roomNo):
    conn = sqlite3.connect('hotel.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO passengers VALUES (NULL,?,?,?,?)", (name, city, year, roomNo))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect('hotel.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM passengers")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(name="", city="", year="", roomNo=""):
    conn = sqlite3.connect('hotel.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM passengers WHERE name=? or city=? or year=? or roomNo=?", (name, city, year, roomNo))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect('hotel.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM passengers WHERE id = ?", (id,))
    conn.commit()
    conn.close()


def update(id, name, city, year, roomNo):
    conn = sqlite3.connect('hotel.db')
    cur = conn.cursor()
    cur.execute("UPDATE passengers SET name=?, city=?, year=?, roomNo=? WHERE id=?", (name, city, year, roomNo,id))
    conn.commit()
    conn.close()


connect()
# insert("Alireza", "Milano", 1378, 105)
# insert("Sanaz", "Torghabe", 1363, 106)
# insert("Mohammad", "Tehran", 1373, 110)
# insert("Maryam", "Shiraz", 1357, 54)
# insert("Mohammad", "Esfehan", 1365, 67)

# delete(9)
# update(3,"Alireza","Milano",1345,43)
# print(view())

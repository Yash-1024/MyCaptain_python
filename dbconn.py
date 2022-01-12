import sqlite3

def connect(dbname):
    conn = sqlite3.connect(dbname)
    conn.execute("CREATE TABLE IF NOT EXISTS Flipkart_Mobiles (NAME, PRICE, SPECIFICATION, RATING, REVIEWS)")
    print("Table Sucessfully Created !")
    conn.close()

def insert_into_table(dbname, values):
    conn = sqlite3.connect(dbname)
    insert_sql = "INSERT INTO Flipkart_Mobiles (NAME, PRICE, SPECIFICATION, RATING, REVIEWS) VALUES(?,?,?,?,?)"
    conn.execute(insert_sql, values)
    conn.commit()
    conn.close()

def get_mobile_info(dbname):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Flipkart_Mobiles")
    table_data = cur.fetchall()
    for record in table_data:
        print(record)
    conn.close()
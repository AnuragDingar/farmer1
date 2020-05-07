import sqlite3


def connect():

    '''=============================================================================================================
    ==================================||| DATABASE CONNECTION ESTABLISHING |||======================================
    ================================================================================================================'''
    conn = sqlite3.connect('new.sqlite')
    cur = conn.cursor()

    '''=============================================================================================================
    =======================================||| TABLE BEING CREATED |||==============================================
    ============================================================================================================='''
    cur.execute('''
                                CREATE TABLE IF NOT EXISTS farmer(
                                name VARCHAR(20),
                                gender VARCHAR(20),
                                category INTEGER(3),
                                mob_num INTEGER(10),
                                district VARCHAR(50),
                                village VARCHAR(20),
                                block VARCHAR(20))''')

    conn.commit()
    conn.close()


def insert(name, gender, category, mob_num, district, village, block):
    conn = sqlite3.connect('new.sqlite')
    cur = conn.cursor()
    cur.execute('''INSERT INTO farmer
                   (name, 
                   gender, 
                   category, 
                   mob_num, 
                   district, 
                   village, 
                   block) VALUES(?, ?, ?, ?, ?, ?, ?)''',(name, gender, category, mob_num, district, village, block))
    conn.commit()
    conn.close()

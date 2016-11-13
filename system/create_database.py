import os
import sqlite3


def create_database():
    if not os.path.isfile('./system/system.db'):

        connect = sqlite3.connect('./system/system.db')
        cursor = connect.cursor()
        
        cursor.execute('''
            CREATE TABLE customer 
            (id INT PRIMARY KEY,
            name NVARCHAR2(128) NOT NULL,
            gender NVARCHAR2(8) NOT NULL,
            phone_number NVARCHAR2(32) NOT NULL,
            address NVARCHAR2(512) NOT NULL,
            email NVARCHAR2(256) NOT NULL)
        ''')

        connect.commit()
        connect.close()
        print('Initial database created')
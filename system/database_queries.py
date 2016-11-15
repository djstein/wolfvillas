import os
import sqlite3
import sys

def create_database():
    if not os.path.isfile('./system/system.db'):
        try:
            connect = sqlite3.connect('./system/system.db')
            cursor = connect.cursor()
            
            # check for foreign keys
            cursor.execute('''PRAGMA foreign_keys = ON''')
            connect.commit()

            cursor.execute('''
                CREATE TABLE customer (
                    id INT PRIMARY KEY,
                    name NVARCHAR2(128) NOT NULL,
                    gender NVARCHAR2(8) NOT NULL,
                    phone_number NVARCHAR2(32) NOT NULL,
                    address NVARCHAR2(512) NOT NULL,
                    email NVARCHAR2(256) NOT NULL
                )''')

            cursor.execute('''
                CREATE TABLE billing (
                    id INT PRIMARY KEY,
                    customer_id NOT NULL,
                    ssn NVARCHAR2(11) NOT NULL,
                    billing_address NVARCHAR2(512) NOT NULL,
                    payment_method NVARCHAR2(32) NOT NULL,
                    credit_card_number NVARCHAR2(19) NOT NULL,
                    FOREIGN KEY(customer_id) REFERENCES customer(id) ON DELETE CASCADE
                )''')

            cursor.execute('''
                CREATE TABLE hotel (
                    id INT PRIMARY KEY,
                    manager_id INT,
                    name NVARCHAR2(32) NOT NULL,
                    address NVARCHAR2(512) NOT NULL,
                    phone_number NVARCHAR2(32) NOT NULL
                )''')

            cursor.execute('''
                CREATE TABLE staff (
                    id INT PRIMARY KEY,
                    hotel_id INT NOT NULL,
                    ssn NVARCHAR2(11) NOT NULL,
                    name NVARCHAR2(128) NOT NULL,
                    age INT NOT NULL,
                    gender NVARCHAR2(8) NOT NULL,
                    job_title NVARCHAR2(32) NOT NULL,
                    department NVARCHAR2(32) NOT NULL,
                    phone_number NVARCHAR2(32) NOT NULL,
                    address NVARCHAR2(512) NOT NULL,
                    FOREIGN KEY(hotel_id) REFERENCES hotel(id) ON DELETE CASCADE
                )''')

            cursor.execute('''
                DROP TABLE hotel
                ''')
            
            cursor.execute('''
                CREATE TABLE hotel (
                    id INT PRIMARY KEY,
                    manager_id INT,
                    name NVARCHAR2(32) NOT NULL,
                    address NVARCHAR2(512) NOT NULL,
                    phone_number NVARCHAR2(32) NOT NULL,
                    FOREIGN KEY(manager_id) REFERENCES staff(id) ON DELETE CASCADE
                )''')

            cursor.execute('''
                CREATE TABLE room (
                    id INT PRIMARY KEY,
                    hotel_id INT NOT NULL,
                    availability NUMBER(1) DEFAULT 0 NOT NULL,
                    category NVARCHAR2(12) NOT NULL,
                    max_occupancy INT NOT NULL,
                    rate INT NOT NULL,
                    FOREIGN KEY(hotel_id) REFERENCES hotel(id) ON DELETE CASCADE
                )''')

            cursor.execute('''
                CREATE TABLE reservation (
                    id INT PRIMARY KEY,
                    customer_id INT NOT NULL,
                    hotel_id INT NOT NULL,
                    room_id INT NOT NULL,
                    current_occupancy INT NOT NULL,
                    check_in DATE,
                    check_out DATE,
                    FOREIGN KEY(customer_id) REFERENCES customer(id) ON DELETE CASCADE,
                    FOREIGN KEY(hotel_id) REFERENCES hotel(id) ON DELETE CASCADE,
                    FOREIGN KEY(room_id) REFERENCES room(id) ON DELETE CASCADE
                )''')
            
            cursor.execute('''
                CREATE TABLE service (
                    id INT PRIMARY KEY,
                    hotel_id INT NOT NULL,
                    name NVARCHAR2(32) NOT NULL,
                    cost INT NOT NULL,
                    FOREIGN KEY(hotel_id) REFERENCES hotel(id) ON DELETE CASCADE
                )''')
            
            cursor.execute('''
                CREATE TABLE service_availed (
                    id INT PRIMARY KEY,
                    reservation_id INT NOT NULL,
                    service_id INT NOT NULL,
                    staff_id INT NOT NULL,
                    FOREIGN KEY(reservation_id) REFERENCES reservation(id) ON DELETE CASCADE,
                    FOREIGN KEY(service_id) REFERENCES service(id) ON DELETE CASCADE,
                    FOREIGN KEY(staff_id) REFERENCES staff(id) ON DELETE CASCADE
                )''')


            connect.commit()

            connect.close()
            print('Initial database created')
            os.remove('./system/system.db')
            print('Initial database killed')
        except:
            print(sys.exc_info()[0])
            os.remove('./system/system.db')
            print('Creation error')
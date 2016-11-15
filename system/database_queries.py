import os
import sqlite3
import sys

class Database(object):

    def __init__(self):
        self.connect = None
        self.cursor = None


    def open_connection(self):
        if not os.path.isfile('./system/system.db'):
            self.connect = sqlite3.connect('./system/system.db')
            self.cursor = self.connect.cursor()

            # Check for foreign keys
            self.cursor.execute('''PRAGMA foreign_keys = ON''')
            self.connect.commit()


    def close_connection(self):
        self.connect.close()


    def create_database(self):
        if self.connect is not None and self.cursor is not None:

            self.cursor.execute('''
                CREATE TABLE customer (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name NVARCHAR2(128) NOT NULL,
                    gender NVARCHAR2(8) NOT NULL,
                    phone_number NVARCHAR2(32) NOT NULL,
                    address NVARCHAR2(512) NOT NULL,
                    email NVARCHAR2(256) NOT NULL
                )''')

            self.cursor.execute('''
                CREATE TABLE billing (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_id NOT NULL,
                    ssn NVARCHAR2(11) NOT NULL,
                    billing_address NVARCHAR2(512) NOT NULL,
                    payment_method NVARCHAR2(32) NOT NULL,
                    credit_card_number NVARCHAR2(19) NOT NULL,
                    FOREIGN KEY(customer_id) REFERENCES customer(id) ON DELETE CASCADE
                )''')

            self.cursor.execute('''
                CREATE TABLE hotel (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    manager_id INT,
                    name NVARCHAR2(32) NOT NULL,
                    address NVARCHAR2(512) NOT NULL,
                    phone_number NVARCHAR2(32) NOT NULL
                )''')

            self.cursor.execute('''
                CREATE TABLE staff (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
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

            self.cursor.execute('''
                DROP TABLE hotel
                ''')
            
            self.cursor.execute('''
                CREATE TABLE hotel (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    manager_id INT,
                    name NVARCHAR2(32) NOT NULL,
                    address NVARCHAR2(512) NOT NULL,
                    phone_number NVARCHAR2(32) NOT NULL,
                    FOREIGN KEY(manager_id) REFERENCES staff(id) ON DELETE CASCADE
                )''')

            self.cursor.execute('''
                CREATE TABLE room (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    hotel_id INT NOT NULL,
                    availability NUMBER(1) DEFAULT 0 NOT NULL,
                    category NVARCHAR2(12) NOT NULL,
                    max_occupancy INT NOT NULL,
                    rate INT NOT NULL,
                    FOREIGN KEY(hotel_id) REFERENCES hotel(id) ON DELETE CASCADE
                )''')

            self.cursor.execute('''
                CREATE TABLE reservation (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
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
            
            self.cursor.execute('''
                CREATE TABLE service (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    hotel_id INT NOT NULL,
                    name NVARCHAR2(32) NOT NULL,
                    cost INT NOT NULL,
                    FOREIGN KEY(hotel_id) REFERENCES hotel(id) ON DELETE CASCADE
                )''')
            
            self.cursor.execute('''
                CREATE TABLE service_availed (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    reservation_id INT NOT NULL,
                    service_id INT NOT NULL,
                    staff_id INT NOT NULL,
                    FOREIGN KEY(reservation_id) REFERENCES reservation(id) ON DELETE CASCADE,
                    FOREIGN KEY(service_id) REFERENCES service(id) ON DELETE CASCADE,
                    FOREIGN KEY(staff_id) REFERENCES staff(id) ON DELETE CASCADE
                )''')


            self.connect.commit()

            print('Initial database created')


    def load_initial_data(self):
        self.cursor.execute(''' 
            INSERT INTO hotel(manager_id, name, address, phone_number) VALUES (NULL, 'Dylan Bed N Breakfast', '2 B and B Drive', '369-555-1234')
            ''')
        self.cursor.execute(''' 
            INSERT INTO hotel(manager_id, name, address, phone_number) VALUES (NULL, 'Royal Suites by Carl', '1 Hotel Street', '123-555-6789')
            ''')
        self.cursor.execute(''' 
            INSERT INTO hotel(manager_id, name, address, phone_number) VALUES (NULL, 'ABANDONED HOTEL 3', '3 Hotel Street', '391-555-2713')
            ''')
        self.cursor.execute(''' 
            INSERT INTO hotel(manager_id, name, address, phone_number) VALUES (NULL, 'ABANDONED HOTEL 2', '4 Hotel Street', '892-555-4782')
            ''')
        self.connect.commit()

        # self.cursor.execute(''' 
        #     ''')
        # self.cursor.execute(''' 
        #     ''')
        # self.cursor.execute(''' 
        #     ''')
        # self.cursor.execute(''' 
        #     ''')
        # connect.commit()


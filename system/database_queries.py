import os
import sqlite3
import sys

class Database(object):

    def __init__(self):
        self.connect = None
        self.cursor = None


    def open_connection(self):
        self.connect = sqlite3.connect('./system/system.db')
        self.cursor = self.connect.cursor()

        # Check for foreign keys
        self.cursor.execute('''PRAGMA foreign_keys = ON''')
        self.connect.commit()


    def close_connection(self):
        self.connect.close()


    def delete_database(self):
        os.remove('./system/system.db')


    def display_hotels(self):
        # TODO: return hotels
        print('hotels')

#########################################################

    def display_customers(self):
        # TODO: return customers
        print('customers')


    def create_customers(self):
        # TODO: create customer
        print('create customers')


    def update_customer(self, customer_id):
        # TODO: update customer
        print('update customers')


    def delete_customer(self, customer_id):
        # TODO: delete customer
        print('delete customers')

#########################################################

    def display_staff(self):
        # TODO: return staff
        print('statff')


    def create_staff(self):
        # TODO: create staff
        print('create staff')


    def update_staff(self, staff_id):
        # TODO: update staff
        print('update staff')


    def delete_staff(self, staff_id):
        # TODO: delete staff
        print('delete staff')

#########################################################

    def display_reservation(self):
        # TODO: return reservations
        print('reservation')


    def create_reservation(self):
        # TODO: create reservation
        print('create reservation')


    def update_reservation(self, reservation_id):
        # TODO: update reservation
        print('update reservation')


    def delete_reservation(self, reservation_id):
        # TODO: delete reservation
        print('delete reservation')

#########################################################

    def display_service_avail(self):
        # TODO: return service_avail
        print('service_avail')


    def create_service_avail(self):
        # TODO: create service_avail
        print('create service_avail')


    def update_service_avail(self, service_avail_id):
        # TODO: update service_avail
        print('update service_avail')


    def delete_service_avail(self, service_avail_id):
        # TODO: delete service_avail
        print('delete service_avail')

#########################################################

    def create_tables(self):
        if self.connect is not None and self.cursor is not None:

            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS customer (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name NVARCHAR2(128) NOT NULL,
                    gender NVARCHAR2(8) NOT NULL,
                    phone_number NVARCHAR2(32) NOT NULL,
                    address NVARCHAR2(512) NOT NULL,
                    email NVARCHAR2(256) NOT NULL
                )''')

            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS billing (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_id NOT NULL,
                    ssn NVARCHAR2(11) NOT NULL,
                    billing_address NVARCHAR2(512) NOT NULL,
                    payment_method NVARCHAR2(32) NOT NULL,
                    credit_card_number NVARCHAR2(19) NOT NULL,
                    FOREIGN KEY(customer_id) REFERENCES customer(id) ON DELETE CASCADE
                )''')

            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS hotel (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    manager_id INT,
                    name NVARCHAR2(32) NOT NULL,
                    address NVARCHAR2(512) NOT NULL,
                    phone_number NVARCHAR2(32) NOT NULL
                )''')

            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS staff (
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
                CREATE TABLE IF NOT EXISTS hotel (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    manager_id INT,
                    name NVARCHAR2(32) NOT NULL,
                    address NVARCHAR2(512) NOT NULL,
                    phone_number NVARCHAR2(32) NOT NULL,
                    FOREIGN KEY(manager_id) REFERENCES staff(id) ON DELETE CASCADE
                )''')

            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS room (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    hotel_id INT NOT NULL,
                    availability NUMBER(1) DEFAULT 0 NOT NULL,
                    category NVARCHAR2(12) NOT NULL,
                    max_occupancy INT NOT NULL,
                    rate INT NOT NULL,
                    FOREIGN KEY(hotel_id) REFERENCES hotel(id) ON DELETE CASCADE
                )''')

            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS reservation (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_id INT NOT NULL,
                    hotel_id INT NOT NULL,
                    room_id INT NOT NULL,
                    current_occupancy INT NOT NULL,
                    check_in DATETIME,
                    check_out DATETIME,
                    FOREIGN KEY(customer_id) REFERENCES customer(id) ON DELETE CASCADE,
                    FOREIGN KEY(hotel_id) REFERENCES hotel(id) ON DELETE CASCADE,
                    FOREIGN KEY(room_id) REFERENCES room(id) ON DELETE CASCADE
                )''')
            
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS service (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    hotel_id INT NOT NULL,
                    name NVARCHAR2(32) NOT NULL,
                    cost INT NOT NULL,
                    FOREIGN KEY(hotel_id) REFERENCES hotel(id) ON DELETE CASCADE
                )''')
            
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS service_availed (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    reservation_id INT NOT NULL,
                    service_id INT NOT NULL,
                    staff_id INT NOT NULL,
                    FOREIGN KEY(reservation_id) REFERENCES reservation(id) ON DELETE CASCADE,
                    FOREIGN KEY(service_id) REFERENCES service(id) ON DELETE CASCADE,
                    FOREIGN KEY(staff_id) REFERENCES staff(id) ON DELETE CASCADE
                )''')

            self.connect.commit()


    def insert_test_hotel(self):
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


    def insert_test_staff(self):
        self.cursor.execute(''' 
           INSERT INTO staff(hotel_id, ssn, name, age, gender, job_title, department, phone_number, address) VALUES (1, '123-45-6789', 'Dylan Stein', 22, 'Male', 'CEO', 'Management', '369-555-1235', '1 Staff Lane')
            ''')
        self.cursor.execute(''' 
           INSERT INTO staff(hotel_id, ssn, name, age, gender, job_title, department, phone_number, address) VALUES (2, '9876-54-321', 'Carl Hiltbrunner', 21, 'Male', 'CEO', 'Management', '123-555-9876', '2 Staff Lane')
            ''')

        self.cursor.execute('''
            UPDATE hotel SET manager_id = 1 WHERE id = 1;
            ''')
        self.cursor.execute(''' 
            UPDATE hotel SET manager_id = 2 WHERE id = 2;
            ''')

        self.cursor.execute(''' 
            INSERT INTO staff(hotel_id, ssn, name, age, gender, job_title, department, phone_number, address) VALUES (1, '8291-37-172', 'John Doe', 51, 'Male', 'Chef', 'Catering', '246-555-3812', '3 Staff Lane')            
            ''')
        self.cursor.execute(''' 
            INSERT INTO staff(hotel_id, ssn, name, age, gender, job_title, department, phone_number, address) VALUES (1, '6382-38-281', 'Jane Doe', 38, 'Female', 'Front Desk Assistant', 'Service', '357-555-9271', '3 Staff Lane')
            ''')
        self.cursor.execute(''' 
            INSERT INTO staff(hotel_id, ssn, name, age, gender, job_title, department, phone_number, address) VALUES (2, '3182-58-221', 'David Smith', 12, 'Male', 'Laundry Person', 'Service', '258-555-7291', '4 Staff Lane');
            ''')
        self.cursor.execute(''' 
            INSERT INTO staff(hotel_id, ssn, name, age, gender, job_title, department, phone_number, address) VALUES (2, '2381-47-182', 'Rachel Smith', 27, 'Female', 'Food Carter', 'Catering', '150-555-3281', '4 Staff Lane');
            ''')
        self.connect.commit()


    def insert_test_customer(self):
        self.cursor.execute(''' 
            INSERT INTO customer(name, gender, phone_number, address, email) VALUES ('Jack Daniels', 'Male', '281-555-1739', '1 Customer Alley', 'jack@example.co')
            ''')
        self.cursor.execute(''' 
            INSERT INTO customer(name, gender, phone_number, address, email) VALUES ('Chris Jenkins', 'Male', '381-555-2812', '2 Customer Alley', 'chris@example.co')
            ''')
        self.cursor.execute(''' 
            INSERT INTO customer(name, gender, phone_number, address, email) VALUES ('Sally Smith', 'Female', '841-555-2181', '3 Customer Alley', 'sally@example.co')
            ''')
        self.cursor.execute(''' 
            INSERT INTO customer(name, gender, phone_number, address, email) VALUES ('Molly Hamilton', 'Female', '183-555-5893', '4 Customer Alley', 'molly@example.co')
            ''')
        self.connect.commit()


    def insert_test_billing(self):
        self.cursor.execute(''' 
            INSERT INTO billing(customer_id, ssn, billing_address, payment_method, credit_card_number) VALUES (1, '417-22-9248', '1 Customer Alley', 'Credit Card', '4916-6153-4460-3360')
            ''')
        self.cursor.execute(''' 
            INSERT INTO billing(customer_id, ssn, billing_address, payment_method, credit_card_number) VALUES (2, '536-60-7072', '2 Customer Alley', 'Credit Card', '4163-8860-4333-5857')
            ''')
        self.cursor.execute(''' 
            INSERT INTO billing(customer_id, ssn, billing_address, payment_method, credit_card_number) VALUES (3, '441-09-1550', '3 Customer Alley', 'Credit Card', '5419-8404-7660-0328')
            ''')
        self.cursor.execute(''' 
            INSERT INTO billing(customer_id, ssn, billing_address, payment_method, credit_card_number) VALUES (4, '037-54-4135', '4 Customer Alley', 'Credit Card', '3441-777641-54242')
            ''')
        self.connect.commit()


    def insert_test_service(self):
        self.cursor.execute(''' 
            INSERT INTO service(hotel_id, name, cost) VALUES (1, 'Breakfast in Bed', 15)
            ''')
        self.cursor.execute(''' 
            INSERT INTO service(hotel_id, name, cost) VALUES (1, 'Room Service', 3)
            ''')
        self.cursor.execute(''' 
            INSERT INTO service(hotel_id, name, cost) VALUES (1, 'Laundry Service', 10)
            ''')
        self.cursor.execute(''' 
            INSERT INTO service(hotel_id, name, cost) VALUES (2, 'Laundry Service', 12)
            ''')
        self.cursor.execute(''' 
            INSERT INTO service(hotel_id, name, cost) VALUES (2, 'Room Service', 5)
            ''')
        self.connect.commit()


    def insert_test_room(self):
        self.cursor.execute(''' 
            INSERT INTO room(hotel_id, availability, category, max_occupancy, rate) VALUES (1, 1, 'Deluxe', 2, 75)
            ''')
        self.cursor.execute(''' 
            INSERT INTO room(hotel_id, availability, category, max_occupancy, rate) VALUES (1, 1, 'Economy', 4, 100)
            ''')
        self.cursor.execute(''' 
            INSERT INTO room(hotel_id, availability, category, max_occupancy, rate) VALUES (2, 1, 'Deluxe', 2, 125)
            ''')
        self.cursor.execute(''' 
            INSERT INTO room(hotel_id, availability, category, max_occupancy, rate) VALUES (2, 1, 'Economy', 4, 150)
            ''')
        self.cursor.execute(''' 
            INSERT INTO room(hotel_id, availability, category, max_occupancy, rate) VALUES (1, 0, 'Economy', 4, 100)
            ''')
        self.cursor.execute(''' 
            INSERT INTO room(hotel_id, availability, category, max_occupancy, rate) VALUES (2, 0, 'Deluxe', 1, 75)
            ''')
        self.connect.commit()


    def insert_test_reservation(self):
        self.cursor.execute(''' 
            INSERT INTO reservation(customer_id, hotel_id, room_id, current_occupancy, check_in, check_out) VALUES (1, 1, 1, 2, '2016-10-08 08:00', '2016-10-16 12:00')
            ''')
        self.cursor.execute(''' 
            INSERT INTO reservation(customer_id, hotel_id, room_id, current_occupancy, check_in, check_out) VALUES (2, 1, 2, 4, '2016-10-19 09:00', '2016-10-22 13:00')
            ''')
        self.cursor.execute(''' 
            INSERT INTO reservation(customer_id, hotel_id, room_id, current_occupancy, check_in, check_out) VALUES (3, 2, 1, 2, '2016-10-16 10:00', '2016-10-23 10:00')
            ''')
        self.cursor.execute(''' 
            INSERT INTO reservation(customer_id, hotel_id, room_id, current_occupancy, check_in, check_out) VALUES (4, 2, 2, 4, '2016-10-20 08:00', '2016-10-24 04:00')
            ''')
        self.connect.commit()


    def insert_test_service_availed(self):
        self.cursor.execute(''' 
            INSERT INTO service_availed(reservation_id, service_id, staff_id) VALUES (1, 1, 1)
            ''')
        self.cursor.execute(''' 
            INSERT INTO service_availed(reservation_id, service_id, staff_id) VALUES (1, 2, 2)
            ''')
        self.cursor.execute(''' 
            INSERT INTO service_availed(reservation_id, service_id, staff_id) VALUES (2, 3, 2)
            ''')
        self.cursor.execute(''' 
            INSERT INTO service_availed(reservation_id, service_id, staff_id) VALUES (3, 4, 3)
            ''')
        self.cursor.execute(''' 
            INSERT INTO service_availed(reservation_id, service_id, staff_id) VALUES (3, 5, 4)
            ''')
        self.cursor.execute(''' 
            INSERT INTO service_availed(reservation_id, service_id, staff_id) VALUES (4, 5, 4)
            ''')
        self.connect.commit()


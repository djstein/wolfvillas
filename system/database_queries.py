import os
import sqlite3

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

#########################################################

    def display_hotels(self):
        self.cursor.execute('SELECT * FROM hotel;')
        results = self.cursor.fetchall()
        if len(results) == 0:
            print 'No hotels found.'
        else:
            print 'Hotel ID, Manager ID, Name, Address, Phone Number'
            print '-------------------------------------------------'
            for result in results:
                print '{0}, {1}, {2}, {3}, {4}'.format(result[0], result[1], result[2], result[3], result[4])

#########################################################

    def display_customers(self):
        self.cursor.execute('SELECT * FROM customer;')
        results = self.cursor.fetchall()
        if len(results) == 0:
            print 'No customers found.'
        else:
            print 'Customer ID, Name, Gender, Phone Number, Address, Email'
            print '-------------------------------------------------------'
            for result in results:
                print '{0}, {1}, {2}, {3}, {4}, {5}'.format(result[0], result[1], result[2], result[3], result[4], result[5])


    def create_customer(self, name, gender, phone_number, address, email):
        self.cursor.execute('''
            INSERT INTO customer(name, gender, phone_number, address, email) 
            VALUES ('{0}', '{1}', '{2}', '{3}', '{4}');'''.format(
                name, gender, phone_number, address, email));
        self.connect.commit()


    def update_customer(self, customer_id, name, gender, phone_number, address, email):
        self.cursor.execute('''
            UPDATE customer SET name='{0}', gender='{1}', phone_number='{2}', address='{3}', email='{4}'
                            WHERE id={5};'''.format(
                name, gender, phone_number, address, email, customer_id));
        self.connect.commit()


    def delete_customer(self, customer_id):
        self.cursor.execute('''
            DELETE FROM customer WHERE id={0};'''.format(customer_id))
        self.connect.commit()

#########################################################

    def display_staff(self):
        self.cursor.execute('SELECT * FROM staff;')
        results = self.cursor.fetchall()
        if len(results) == 0:
            print 'No staff found.'
        else:
            print 'Staff ID, Hotel ID, Name, Age, Gender, Job Title, Department, Phone Number, Address, Email'
            print '------------------------------------------------------------------------------------------'
            for result in results:
                    print '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}'.format(result[0], result[1], result[2], result[3],
                                                              result[4], result[5], result[6], result[7], result[8], result[9])


    def create_staff(self, hotel_id, ssn, name, age, gender, job_title, department, phone_number, address):
        self.cursor.execute('''
            INSERT INTO staff(hotel_id, ssn, name, age, gender, job_title,
                              department, phone_number, address) 
            VALUES ({0}, '{1}', '{2}', {3}, '{4}', '{5}', '{6}', '{7}', '{8}');'''.format(
                hotel_id, ssn, name, age, gender,
                job_title, department, phone_number, address));
        self.connect.commit()


    def update_staff(self, staff_id, hotel_id, ssn, name, age, gender, job_title, department, phone_number, address):
        self.cursor.execute('''
            UPDATE staff SET hotel_id={0}, ssn='{1}', name='{2}', age={3}, gender='{4}',
                             job_title='{5}', department='{6}', phone_number='{7}', address='{8}' 
                         WHERE id={9}'''.format( hotel_id, ssn, name, age, gender, job_title,
                                                 department, phone_number, address, staff_id));
        self.connect.commit()


    def delete_staff(self, staff_id):
        self.cursor.execute('''
            DELETE FROM staff WHERE id={0};'''.format(staff_id))
        self.connect.commit()

    #########################################################

    def display_rooms(self):
        self.cursor.execute('SELECT * FROM room;')
        results = self.cursor.fetchall()
        if len(results) == 0:
            print 'No rooms found.'
        else:
            print 'Room Number, Hotel ID, Availability, Category, Max Occupancy, Rate'
            print '------------------------------------------------------------------'
            for result in results:
                print '{0}, {1}, {2}, {3}, {4}, {5}'.format(
                        result[0], result[1], result[2], result[3], result[4], result[5])


    def display_available_rooms(self):
        self.cursor.execute('SELECT * FROM room WHERE availability = 1;')
        results = self.cursor.fetchall()
        if len(results) == 0:
            print 'No available rooms found.'
        else:
            for result in results:
                print '{0}, {1}, {2}, {3}, {4}, {5}'.format(
                        result[0], result[1], result[2], result[3], result[4], result[5])

    def find_room(self, customer_id, hotel_id, required_occupancy, category):
        self.cursor.execute('''SELECT * FROM room WHERE availability=1
                AND hotel_id={0} AND max_occupancy >= {1} AND category='{2}';'''.format(hotel_id, required_occupancy, category))
        results = self.cursor.fetchall()
        if len(results) == 0:
            print 'No available rooms found.'
        else:
            rooms = []
            print 'Room Number, Hotel ID, Availability, Category, Max Occupancy, Rate'
            print '------------------------------------------------------------------'
            for result in results:
                print '{0}, {1}, {2}, {3}, {4}, {5}'.format(
                        result[0], result[1], result[2], result[3], result[4], result[5])
                rooms.append(result[0])
            room_number = int(raw_input('room: '))
            while room_number not in rooms:
                print 'invalid room, choose again'
                room_number = int(raw_input('room: '))

            check_in = raw_input('check in: ')
            check_out = raw_input('check out: ')
            self.cursor.execute('''
                INSERT INTO reservation(customer_id, hotel_id, room_id, current_occupancy, check_in, check_out)
                VALUES({0}, {1}, {2}, {3}, '{4}', '{5}');'''.format(
                    customer_id, hotel_id, room_number, required_occupancy, check_in, check_out))
            self.occupy_room(room_number)
            self.connect.commit()


    
    def release_room(self, room_number):
        self.cursor.execute('UPDATE room SET availability = 1 WHERE id={0};'.format(room_number))
        self.connect.commit()

    def occupy_room(self, room_number):
        self.cursor.execute('UPDATE room SET availability = 0 WHERE id={0};'.format(room_number))
        self.connect.commit()

    def create_room(self, room_number, hotel_id, availability, category, max_occupancy, rate):
        self.cursor.execute('''
            INSERT INTO room(room_number, hotel_id, availability, category, max_occupancy, rate) 
            VALUES({0}, {1}, {2}, '{3}', {4}, {5});'''.format(
                room_number, hotel_id, availability, category, max_occupancy, rate))
        self.connect.commit()


    def update_room(self, room_number, hotel_id, availability, category, max_occupancy, rate):
        self.cursor.execute('''
            UPDATE room SET id={0}, hotel_id={1}, availability={2},
                            category='{3}', max_occupancy={4}, rate={5}
                            WHERE id={6}'''.format(room_number, hotel_id, availability,
                                                   category, max_occupancy, rate, room_number))
        self.connect.commit()


    def delete_room(self, room_number):
        self.cursor.execute('''
            DELETE FROM room WHERE id={0};'''.format(room_number))
        self.connect.commit()

#########################################################

    def display_reservations(self):
        self.cursor.execute('SELECT * FROM reservation;')
        results = self.cursor.fetchall()
        if len(results) == 0:
            print 'No reservations found.'
        else:
            print 'Reservation Number, Customer ID, Hotel ID, Room Number, Current Occupancy, Check In, Check Out'
            print '----------------------------------------------------------------------------------------------'
            for result in results:
                print '{0}, {1}, {2}, {3}, {4}, {5}, {6}'.format(result[0], result[1], result[2], result[3], result[4], result[5], result[6])


    def create_reservation(self, customer_id, hotel_id, room_id, current_occupancy,
                           check_in, check_out):
        self.cursor.execute('''
                INSERT INTO reservation(customer_id, hotel_id, room_id,
                                        current_occupancy, check_in, check_out)
                VALUES ({0}, {1}, {2}, {3}, '{4}', '{5}');
            '''.format(customer_id, hotel_id, room_id, current_occupancy, check_in, check_out))
        self.connect.commit()


    def update_reservation(self, reservation_id, room_id, current_occupancy, check_in, check_out):
        self.cursor.execute('''
                UPDATE reservation SET room_id={0}, current_occupancy={1}, check_in='{2}', check_out='{3}'
                WHERE id={4};
            '''.format(room_id, current_occupancy, check_in, check_out, reservation_id))
        self.connect.commit()


    def delete_reservation(self, reservation_id):
        self.cursor.execute('DELETE FROM reservation WHERE id={0};'.format(reservation_id))
        self.connect.commit()

#########################################################

    def display_services(self):
        self.cursor.execute('SELECT * FROM service;')
        results = self.cursor.fetchall()
        if len(results) == 0:
            print 'No services found.'
        else:
            print 'Service ID, Hotel ID, Name, Cost'
            print '--------------------------------'
            for result in results:
                print '{0}, {1}, {2}, {3}'.format(result[0], result[1], result[2], result[3]) 


    def create_service(self, hotel_id, name, cost):
        self.cursor.execute('''
            INSERT INTO service(hotel_id, name, cost)
            VALUES({0}, '{1}', {2});'''.format(hotel_id, name, cost))
        self.connect.commit()


    def update_service(self, service_id, hotel_id, name, cost):
        self.cursor.execute('''
            UPDATE service SET hotel_id={0}, name='{1}', cost={2}
                           WHERE id={3};'''.format(hotel_id, name, cost, service_id))
        self.connect.commit()


    def delete_service(self, service_id):
        self.cursor.execute('''
            DELETE FROM service WHERE id={0};'''.format(service_id))
        self.connect.commit()

#########################################################

    def display_services_availed(self):
        self.cursor.execute('SELECT * FROM service_availed;')
        results = self.cursor.fetchall()
        if len(results) == 0:
            print 'No services availed.'
        else:
            print 'Services Availed ID, Reservation ID, Service ID, Staff ID'
            print '---------------------------------------------------------'
            for result in results:
                print '{0}, {1}, {2}, {3}'.format(result[0], result[1], result[2], result[3]) 


    def create_service_availed(self, reservation_id, service_id, staff_id):
        self.cursor.execute('''
            INSERT INTO service_availed(reservation_id, service_id, staff_id)
            VALUES({0}, {1}, {2});'''.format(reservation_id, service_id, staff_id))
        self.connect.commit()


    def update_service_availed(self, service_availed_id, reservation_id, service_id, staff_id):
        self.cursor.execute('''
            UPDATE service_availed SET reservation_id={0}, service_id={1}, staff_id={2}
            WHERE id={3};'''.format(reservation_id, service_id, staff_id, service_availed_id))
        self.connect.commit()


    def delete_service_availed(self, service_availed_id):
        self.cursor.execute('''
            DELETE FROM service_availed WHERE id={0};'''.format(service_availed_id))
        self.connect.commit()

#########################################################

    def create_tables(self):
        if self.connect and self.cursor:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS customer (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name NVARCHAR2(128) NOT NULL,
                    gender NVARCHAR2(8) NOT NULL,
                    phone_number NVARCHAR2(32) NOT NULL,
                    address NVARCHAR2(512) NOT NULL,
                    email NVARCHAR2(256) NOT NULL
                );''')

            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS billing (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_id NOT NULL,
                    ssn NVARCHAR2(11) NOT NULL,
                    billing_address NVARCHAR2(512) NOT NULL,
                    payment_method NVARCHAR2(32) NOT NULL,
                    credit_card_number NVARCHAR2(19) NOT NULL,
                    FOREIGN KEY(customer_id) REFERENCES customer(id) ON DELETE CASCADE
                );''')

            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS hotel (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    manager_id INT,
                    name NVARCHAR2(32) NOT NULL,
                    address NVARCHAR2(512) NOT NULL,
                    phone_number NVARCHAR2(32) NOT NULL
                );''')

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
                );''')

            self.cursor.execute('DROP TABLE IF EXISTS hotel;')
            
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS hotel (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    manager_id INT,
                    name NVARCHAR2(32) NOT NULL,
                    address NVARCHAR2(512) NOT NULL,
                    phone_number NVARCHAR2(32) NOT NULL,
                    FOREIGN KEY(manager_id) REFERENCES staff(id) ON DELETE CASCADE
                );''')

            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS room (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    hotel_id INT NOT NULL,
                    availability NUMBER(1) DEFAULT 0 NOT NULL,
                    category NVARCHAR2(12) NOT NULL,
                    max_occupancy INT NOT NULL,
                    rate INT NOT NULL,
                    FOREIGN KEY(hotel_id) REFERENCES hotel(id) ON DELETE CASCADE
                );''')

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
                );''')
            
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS service (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    hotel_id INT NOT NULL,
                    name NVARCHAR2(32) NOT NULL,
                    cost INT NOT NULL,
                    FOREIGN KEY(hotel_id) REFERENCES hotel(id) ON DELETE CASCADE
                );''')
            
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS service_availed (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    reservation_id INT NOT NULL,
                    service_id INT NOT NULL,
                    staff_id INT NOT NULL,
                    FOREIGN KEY(reservation_id) REFERENCES reservation(id) ON DELETE CASCADE,
                    FOREIGN KEY(service_id) REFERENCES service(id) ON DELETE CASCADE,
                    FOREIGN KEY(staff_id) REFERENCES staff(id) ON DELETE CASCADE
                );''')

            self.connect.commit()


    def insert_test_hotel(self):
        self.cursor.execute(''' 
            INSERT INTO hotel(manager_id, name, address, phone_number)
            VALUES (NULL, 'WolfVilla', '27 Timber Dr, Garner, NC 27529', '976-728-1980');
            ''')

        self.connect.commit()


    def insert_test_staff(self):
        self.cursor.execute(''' 
           INSERT INTO staff(hotel_id, ssn, name, age, gender, job_title, department, phone_number, address)
           VALUES (1, '409-02-1234', 'David D. Clukey', 40, 'Male', 'Front Desk representative', 'Administration', '980-131-1238', '106, Cloverdale Ct, Raleigh, NC, 27607');
            ''')

        self.cursor.execute(''' 
            INSERT INTO staff(hotel_id, ssn, name, age, gender, job_title, department, phone_number, address)
            VALUES (1, '143-22-9089', 'James M Gooden', 25, 'Male', 'Catering Staff', 'Catering', '980-187-1983', '109, Cloverdale Ct, Raleigh, NC, 27607');
            ''')
        
        self.cursor.execute(''' 
            INSERT INTO staff(hotel_id, ssn, name, age, gender, job_title, department, phone_number, address)
            VALUES (1, '479-50-0120', 'Jasper N. Daniel', 167, 'Male', 'Cleaning Staff', 'Cleaning', '202-555-0110', '182 Lynchburg Highway, Lynchburg, TN, 37352');
            ''')

        self.cursor.execute(''' 
            INSERT INTO staff(hotel_id, ssn, name, age, gender, job_title, department, phone_number, address)
            VALUES (1, '132-67-4793', 'Todd C. Chen', 48, 'Male', 'Manager', 'Administration', '976-728-1980', '1048, Avent Ferry Road, Raleigh, NC, 27606');
            ''')

        self.cursor.execute("UPDATE hotel SET manager_id = 3 WHERE name = 'WolfVilla';")

        self.connect.commit()


    def insert_test_customer(self):
        self.cursor.execute(''' 
            INSERT INTO customer(name, gender, phone_number, address, email)
            VALUES ('Carl T. Ashcraft', 'Male', '701-555-0143', '881 Java Lane, Graniteville, SC 29829', 'carlashcraft@kmail.us')
            ''');
        self.cursor.execute(''' 
            INSERT INTO customer(name, gender, phone_number, address, email)
            VALUES ('Angela J. Roberts', 'Female', '202-555-0118', '2697 Stroop Hill Road, Atlanta, GA 30342', 'angelaroberts@kmail.us');
            ''')

        self.connect.commit()


    def insert_test_billing(self):
        self.cursor.execute(''' 
            INSERT INTO billing(customer_id, ssn, billing_address, payment_method, credit_card_number)
            VALUES (1, '144-54-9090', '881 Java Lane, Graniteville, SC 29829', 'Credit Card', '5184-9505-0558-9328');
            ''')
        self.cursor.execute(''' 
            INSERT INTO billing(customer_id, ssn, billing_address, payment_method, credit_card_number)
            VALUES (2, '678-90-0900', '2697 Stroop Hill Road, Atlanta, GA 30342', 'Credit Card', '5196-5914-3238-5020');
            ''')

        self.connect.commit()


    def insert_test_room(self):
        self.cursor.execute('''
            INSERT INTO room(id, hotel_id, availability, category, max_occupancy, rate)
            VALUES (101, 1, 0, 'Economy', 2, 150);
            ''')
        self.cursor.execute(''' 
            INSERT INTO room(id, hotel_id, availability, category, max_occupancy, rate)
            VALUES (201, 1, 0, 'Executive Suite', 2, 250);
            ''')
        self.cursor.execute(''' 
            INSERT INTO room(id, hotel_id, availability, category, max_occupancy, rate)
            VALUES (301, 1, 1, 'Deluxe', 2, 350);
            ''')

        self.connect.commit()


    def insert_test_reservation(self):
        self.cursor.execute(''' 
            INSERT INTO reservation(customer_id, hotel_id, room_id, current_occupancy, check_in, check_out)
            VALUES (1, 1, 101, 2, '2016-11-12 12:00', '2016-11-16 12:00');
            ''')
        self.cursor.execute(''' 
            INSERT INTO reservation(customer_id, hotel_id, room_id, current_occupancy, check_in, check_out)
            VALUES (2, 1, 201, 2, '2016-11-14 12:00', '2016-11-22 12:00');
            ''')

        self.connect.commit()


    def insert_test_service(self):
        self.cursor.execute(''' 
            INSERT INTO service(hotel_id, name, cost) VALUES (1, 'Restaurant Combo 1', 30);
            ''')
        self.cursor.execute(''' 
            INSERT INTO service(hotel_id, name, cost) VALUES (1, 'Restaurant Combo 2', 35);
            ''')
        self.cursor.execute(''' 
            INSERT INTO service(hotel_id, name, cost) VALUES (1, 'Restaurant Combo 3', 40);
            ''')
        self.cursor.execute(''' 
            INSERT INTO service(hotel_id, name, cost) VALUES (1, 'Laundry Deluxe', 15);
            ''')
        self.cursor.execute(''' 
            INSERT INTO service(hotel_id, name, cost) VALUES (1, 'Laundry Standard', 10);
            ''')

        self.connect.commit()

    def insert_test_service_availed(self):
        self.cursor.execute(''' 
            INSERT INTO service_availed(reservation_id, service_id, staff_id)
            VALUES (1, 1, 2);
            ''')
        self.cursor.execute(''' 
            INSERT INTO service_availed(reservation_id, service_id, staff_id) 
            VALUES (1, 2, 2);
            ''')
        self.cursor.execute(''' 
            INSERT INTO service_availed(reservation_id, service_id, staff_id)
            VALUES (2, 4, 3);
            ''')
        self.cursor.execute(''' 
            INSERT INTO service_availed(reservation_id, service_id, staff_id)
            VALUES (2, 3, 2);
            ''')
        self.cursor.execute(''' 
            INSERT INTO service_availed(reservation_id, service_id, staff_id)
            VALUES (2, 4, 3);
            ''')
        self.cursor.execute(''' 
            INSERT INTO service_availed(reservation_id, service_id, staff_id)
            VALUES (2, 5, 3);
            ''')

        self.connect.commit()

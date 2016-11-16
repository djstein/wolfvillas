import sys
from database_queries import Database


def hotel(database, hotel_id):
    commands_hotel()
    command = raw_input("db_mgmt: ").lower()
    while command != 'return':
        command = command.split()
        if len(command) == 0:
            print ''
        elif command[0] == 'customers':
            if len(command) == 1:
                database.display_customers()
            elif command[1] == 'create':
                name = raw_input('name: ')
                gender =  raw_input('gender: ')
                phone_number = raw_input('phone number: ')
                address = raw_input('address: ')
                email = raw_input('email: ')
                database.create_customer(name, gender, phone_number, address, email)

            elif command[1] == 'update' and len(command) == 3 and command[2].isdigit():
                name = raw_input('name: ')
                gender =  raw_input('gender: ')
                phone_number = raw_input('phone number: ')
                address = raw_input('address: ')
                email = raw_input('email: ')
                database.update_customer(command[2], name, gender, phone_number, address, email)

            elif command[1] == 'delete' and len(command) == 3 and command[2].isdigit():
                database.delete_customer(command[2])

            else:
                print 'Invalid Input'

        elif command[0] == 'rooms':
            if len(command) == 1:
                database.display_rooms()

            elif command[1] == 'available':
                database.display_available_rooms()

            elif command[1] == 'create':
                room_number = raw_input('room number: ')
                category = raw_input('category: ')
                max_occupancy = raw_input('max occupancy: ')
                rate = raw_input('rate: ')
                database.create_room(room_number, hotel_id, 1, category, max_occupancy, rate)

            elif command[1] == 'update' and len(command) == 3 and command[2].isdigit():
                room_number = raw_input('room number: ')
                category = raw_input('category: ')
                max_occupancy = raw_input('max occupancy: ')
                rate = raw_input('rate: ')
                database.update_room(room_number, hotel_id, 1, category, max_occupancy, rate)

            elif command[1] == 'release' and len(command) == 3 and command[2].isdigit():
                database.release_room(command[2])

            elif command[1] == 'delete' and len(command) == 3 and command[2].isdigit():
                database.delete_room(command[2])
            
            else:
                print 'Invalid Input'

        elif command[0] == 'reservations':
            if len(command) == 1:
                database.display_reservations()
            elif command[1] == 'create':
                customer_id = raw_input('customer id: ')
                required_occupancy = raw_input('required occupancy: ')
                category = raw_input('category: ')
                database.find_room(customer_id, hotel_id, required_occupancy, category)

            elif command[1] == 'update' and len(command) == 3 and command[2].isdigit():
                room_id = raw_input('room number: ')
                current_occupancy = raw_input('current occupancy: ')
                check_in = raw_input('check in: ')
                check_out = raw_input('check out: ')
                database.update_reservation(command[2], room_id, current_occupancy, check_in, check_out)

            elif command[1] == 'delete' and len(command) == 3 and command[2].isdigit():
                database.delete_reservation(command[2])
            
            else:
                print 'Invalid Input'

        elif command[0] == 'services':
            if len(command) == 1:
                database.display_services()
            elif command[1] == 'create':
                name = raw_input('name: ')
                cost = raw_input('cost: ')
                database.create_service(hotel_id, name, cost)

            elif command[1] == 'update' and len(command) == 3 and command[2].isdigit():
                name = raw_input('name: ')
                cost = raw_input('cost: ')
                database.update_service(command[2], hotel_id, name, cost)

            elif command[1] == 'delete' and len(command) == 3 and command[2].isdigit():
                database.delete_service(command[2])

            else:
                print 'Invalid Input'

        elif command[0] == 'services_availed':
            if len(command) == 1:
                database.display_services_availed()
            elif command[1] == 'create':
                reservation_id = raw_input('reservation ID: ')
                service_id = raw_input('service ID: ')
                staff_id = raw_input('staff ID: ')
                database.create_service_availed(reservation_id, service_id, staff_id)

            elif command[1] == 'update' and len(command) == 3 and command[2].isdigit():
                reservation_id = raw_input('reservation ID: ')
                service_id = raw_input('service ID: ')
                staff_id = raw_input('staff ID: ')
                database.update_service_availed(command[2], reservation_id, service_id, staff_id)

            elif command[1] == 'delete' and len(command) == 3 and command[2].isdigit():
                database.delete_service_availed(command[2])

            else:
                print 'Invalid Input'

        elif command[0] == 'staff':
            if len(command) == 1:
                database.display_staff()

            elif command[1] == 'create':
                ssn = raw_input('ssn: ')
                name = raw_input('name: ')
                age = raw_input('age: ')
                gender =  raw_input('gender: ')
                job_title =  raw_input('job title: ')
                department = raw_input('department: ')
                phone_number = raw_input('phone number: ')
                address = raw_input('address: ')
                database.create_staff(hotel_id, ssn, name, age, gender, job_title, department, phone_number, address)

            elif command[1] == 'update' and len(command) == 3 and command[2].isdigit():
                ssn = raw_input('ssn: ')
                name = raw_input('name: ')
                age = raw_input('age: ')
                gender =  raw_input('gender: ')
                job_title =  raw_input('job title: ')
                department = raw_input('department: ')
                phone_number = raw_input('phone number: ')
                address = raw_input('address: ')
                database.update_staff(command[2], hotel_id, ssn, name, age, gender, job_title, department, phone_number, address)

            elif command[1] == 'delete' and len(command) == 3 and command[2].isdigit():
                database.delete_staff(command[2])

            else:
                print 'Invalid Input'

        elif command[0] == 'help' and len(command) == 1:
            commands_hotel()

        elif command[0] == 'quit' and len(command) == 1:
            quit(database)

        else:
            print 'Invalid Input'

        command = raw_input("db_mgmt: ").lower()

    commands_main()


def staff(database):
    print(
        """
    Commands for Staff:
        display: 
        create: create/update/delete customer info
        update: create/update/delete customer reservations
        delete: create/update/delete services availed

        help: prompt the commands
        return: returns to main menu"""
    )

def commands_hotel():
    print(
        """
        Commands for customers:
            customers: display all customers
            customers create
            customers update [id]
            customers delete [id]
        
        Commands for reservations:
            reservations: display all reservations for this hotel
            reservations create
            reservations update [id]
            reservations delete [id]
        
        Commands for rooms
            rooms: display all rooms for this hotel
            rooms available: display available rooms in this hotel
            rooms release [number]: make room available
            rooms create
            rooms update [number]
            rooms delete [number]

        Commands for service types:
            services: display all services at this hotel
            services create
            services update [id]
            services delete [id]

        Commands for services availed:
            services_availed: display all services at this hotel
            services_availed create
            services_availed update [id]
            services_availed delete [id]

        Commands for staff availed:
            staff: display all staff at this hotel
            staff create
            staff update [id]
            staff delete [id]

        return: to main menu
        help: accessible commands
        quit: end the current session"""
    )


def commands_main():
    print(
        """WolfVillas Database Management System
    Version: 1.0.0
    Commands:
        display hotels: display the hotels with IDs and name's
        hotel [id]: begin operations with customers, reservations
            services, and stff

        load: load test data
        wipe: delete data
        help: accessible commands
        quit: end the current session"""
    )


def quit(database):
    if database.connect is not None:
        database.close_connection()
    sys.exit()


def load_test_data(database):
    if database.connect is not None:
        database.insert_test_hotel()
        database.insert_test_staff()
        database.insert_test_customer()
        database.insert_test_billing()
        database.insert_test_service()
        database.insert_test_room()
        database.insert_test_reservation()
        database.insert_test_service_availed()


if __name__ == '__main__':
    commands_main()

    database = Database()
    database.open_connection()
    database.create_tables()

    command = raw_input("db_mgmt: ").lower()
    while command != 'quit':
        command = command.split()
        if len(command) == 0:
            print ''
        elif ' '.join(command) == 'display hotels':
            database.display_hotels()
        elif command[0] == 'hotel' and len(command) == 2 and command[1].isdigit():
            # Check if command[1] is existing hotel id
            hotel(database, command[1])
        elif command[0] == 'help':
            commands_main()
        elif command[0] == 'load':
            load_test_data(database)
        elif command[0] == 'wipe':
            database.delete_database()
        else:
            print 'Invalid Input'

        command = raw_input("db_mgmt: ").lower()

    quit(database)

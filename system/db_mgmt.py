import os
import sys
from database_queries import Database


def hotel(database, hotel_id):
    commands_hotel()
    command = raw_input("db_mgmt: ").lower()
    while command != 'return':
        command = command.split()
        if command[0] == 'customers':
            database.display_customers()
        elif command[0] == 'reservations':
            display_reservations(database)
        elif command[0] == 'services':
            display_services(database)
        elif command[0] == 'staff':
            display_staff(database)
        elif command[0] == 'help':
            commands_hotel()
        elif command[0] == 'quit':
            quit(database)
        else:
            print("Invalid Input")
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
            customers : display all customers
            customers create
            customers update [id]
            customers delete [id]
        
        Commands for reservations:
            reservations : display all reservations for this hotel
            reservations create
            reservations update [id]
            reservations delete [id]

        Commands for services availed:
            services : display all services at this hotel
            services create
            services update [id]
            services delete [id]

        Commands for staff availed:
            staff : display all staff at this hotel
            staff create
            staff update [id]
            staff delete [id]

        return: to main menu
        help: accessable commands
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

        help: accessable commands
        quit: end the current session"""
    )


def quit(database):
    if database.connect is not None:
        database.close_connection()
    sys.exit()


# def load_test_data(database):
#     if database.connect is not None:
#         database.insert_test_hotel()
#         database.insert_test_staff()
#         database.insert_test_customer()
#         database.insert_test_billing()
#         database.insert_test_service()
#         database.insert_test_room()
#         database.insert_test_reservation()
#         database.insert_test_service_availed()


if __name__ == '__main__':
    commands_main()

    database = Database()
    database.open_connection()
    database.create_tables()

    command = raw_input("db_mgmt: ").lower()
    while command != 'quit':
        if command == 'display hotels':
            database.display_hotels()
        elif command == 'hotel 1':
            hotel(database, command)
        elif command == 'help':
            commands_main()
        else:
            print("Invalid Input")
        command = raw_input("db_mgmt: ").lower()

    quit(database)
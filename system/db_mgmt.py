import os
import sys
from database_queries import Database

def commands():
    print(
        """WolfVillas Database Management System
    Version: 1.0.0
    Commands:
        create
        help: prompt the commands
        quit: end the current session"""
    )


def quit():
    sys.exit()


if __name__ == '__main__':
    commands()
    
    database = Database()
    database.open_connection()
    database.create_database()

    database.insert_test_hotel()
    database.insert_test_staff()
    database.insert_test_customer()
    database.insert_test_billing()
    database.insert_test_service()
    database.insert_test_room()
    database.insert_test_reservation()
    database.insert_test_service_availed()

    command = raw_input("db_mgmt: ").lower()
    while command != 'quit':
        if command == 'load':
            database.load_initial_data()
        if command == 'help':
            commands()
        command = raw_input("db_mgmt: ").lower()
    
    database.close_connection()
    # database.delete_database()

    quit()
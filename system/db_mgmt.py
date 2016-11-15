import os
import sys
from database_queries import Database

def commands():
    print(
        """WolfVillas Database Management System
    Version: 1.0.0
    Commands:

        DATA OPERATIONS
        delete data: removes all data from tables
        load test data: removes all data. recreates tables with testing data
        
        TABLE OPERATIONS
        create tables: create tables for the database
        drop tables: drop all tables from the database
        
        help: prompt the commands
        quit: end the current session"""
    )

def quit(database):
    if database.connect is not None:
        database.close_connection()
    sys.exit()


def load_test_data(database):
    if database.connect is not None:
        database.delete_all_rows()

        database.drop_tables()
        database.create_tables()

        database.insert_test_hotel()
        database.insert_test_staff()
        database.insert_test_customer()
        database.insert_test_billing()
        database.insert_test_service()
        database.insert_test_room()
        database.insert_test_reservation()
        database.insert_test_service_availed()


if __name__ == '__main__':
    commands()
    
    database = Database()
    database.open_connection()
    database.create_tables()

    command = raw_input("db_mgmt: ").lower()
    while command != 'quit':
        if command == 'create tables':
            database.create_tables()
        
        elif command == 'drop tables':
            database.delete_all_rows()
            database.drop_tables()
        
        elif command == 'delete data':
            database.delete_all_rows()

        elif command == 'load test data':
            load_test_data(database)
        
        elif command == 'drop tables':
            database.drop_tables()
        
        elif command == 'help':
            commands()
        else:
            print("Invalid Input")
        command = raw_input("db_mgmt: ").lower()

    quit(database)
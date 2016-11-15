import os
import sys
from create_database import create_database

def commands():
    print(
        """WolfVillas Database Management System
    Version: 1.0.0
    Commands:
        help: prompt the commands
        quit: end the current session"""
    )


def user_commands():
    command = raw_input("db_mgmt: ").lower()
    while command != 'quit':
        if command == 'help':
            commands()
        command = raw_input("db_mgmt: ").lower()
    quit()


def quit():
    sys.exit()


if __name__ == '__main__':
    commands()
    create_database()
    user_commands()
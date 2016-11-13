import os
import sys
from create_database import create_database

def commands():
    print(
        """WolfVillas Database Management System
    Version: 1.0.0
    Commands:
        quit: end the current session
        help: prompt the commands"""
    )


def quit():
    sys.exit()


if __name__ == '__main__':
    commands()
    create_database()
    quit()
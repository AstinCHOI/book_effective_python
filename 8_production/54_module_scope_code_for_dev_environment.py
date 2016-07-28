
# module: db_connection.py
import __main__


class TestingDatabase(object):
    pass

class RealDatabase(object):
    pass

if __main__.TESTING:
    Database = TestingDatabase
else:
    Database = RealDatabase


# dev_main.py
TESTING = True
import db_connection
db = db_db_connection.Database()

# prod_main.py
TESTING = False
import db_connection
db = db_db_connection.Database()

# if development enviroment is complex, consider to move constants like TESTING to separate configuration file 
# ref: inner module configparser


# db_connection.py
import sys

class Win32Database(object):
    pass

class PosixDatabase(object):
    pass

if sys.platform.startswith('win32'):
    Database = Win32Database
else:
    Database = PosixDatabase
__author__ = 'viczmandi'

import mysql.connector

# building up db connection
db = mysql.connector.connect(user="root", password="", host="localhost")

# prepare a cursor object using cursor() method
cursor = db.cursor()

try:
    for row in open("../sql/01_hr_db_creation.sql"):
        cursor.execute(row)
except Exception as ex:
    print("Something went wrong: ", ex)
    db.rollback()

# disconnect from server
db.close()
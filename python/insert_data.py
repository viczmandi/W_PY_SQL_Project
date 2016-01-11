__author__ = 'viczmandi'

import mysql.connector

# building up db connection
db = mysql.connector.connect(user="root", password="", host="localhost", database="customtask")

# prepare a cursor object using cursor() method
cursor = db.cursor()

try:
    for row in open("../sql_scripts/insert_customtask.sql"):
        cursor.execute(row)
    db.commit()
except Exception as ex:
    print("Something went wrong: ", ex)
    db.rollback()

# disconnect from server
db.close()

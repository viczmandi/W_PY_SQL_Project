__author__ = 'viczmandi'

import mysql.connector

# building up db connection
db = mysql.connector.connect(user="root", password="", host="localhost", database="hr_db")

# prepare a cursor object using cursor() method
cursor = db.cursor()

menu = input("""
1. ---Basic select---
2. ---Restricting and Sorting Data---
3. ---Aggregate Functions and GROUP BY---
4. ---Subqueries---
5. ---Joins---
6. ---String Functions---
""")

sql_file_path = ""

if int(menu) == 1:
    sql_file_path = "../sql/basic_select_query.sql"
elif int(menu) == 2:
    sql_file_path = "../sql/restricting_and_sorting_data_query.sql"
elif int(menu) == 3:
    sql_file_path = "../sql/aggregate_functions_and_GROUP_BY_query.sql"
elif int(menu) == 4:
    sql_file_path = "../sql/subqueries_query.sql"
elif int(menu) == 5:
    sql_file_path = "../sql/joins_query.sql"
elif int(menu) == 6:
    sql_file_path = "../sql/string_functions_query.sql"

try:
    for query in open(sql_file_path):
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            print(row)
        print("-"*50)
except Exception as ex:
    print("Error: unable to fetch data: ", ex)

# disconnect from server
db.close()
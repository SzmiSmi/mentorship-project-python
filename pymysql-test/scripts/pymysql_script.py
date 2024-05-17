import pymysql
# from csv_handler import CsvFile
import pandas as pd
from processor_insolvency_statistics import parser




insolvency_data_path = 'resources/historical_insolvency_statistics_-_naics_monthly-march-2024.csv'

new_parser = parser()
new_parser.province_fill(insolvency_data_path)


# # database connection
# connection = pymysql.connect(host="localhost", 
#                             port=3306, 
#                             user="root", 
#                             password="example", 
#                             database="MYDATABASE")
# print("Connection Success!")

# with connection.cursor() as cursor:
#     # Create a table if it does not exist
#     sqlQueryString = "CREATE TABLE IF NOT EXISTS Users (id int NOT NULL AUTO_INCREMENT, email varchar(255) NOT NULL, password varchar(255) NOT NULL, PRIMARY KEY (id)) AUTO_INCREMENT=1;"
#     cursor.execute(sqlQueryString)
#     connection.commit()

#     # Create a new record
#     sql = "INSERT INTO Users (email, password) VALUES (%s, %s)"
#     cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

#     # Read a single record
#     sql = "SELECT `id`, `password` FROM `Users` WHERE `email`=%s"
#     cursor.execute(sql, ('webmaster@python.org',))
#     result = cursor.fetchall()
#     print(result)
    
# connection.close()




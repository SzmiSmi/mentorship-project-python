import pymysql

# database connection
connection = pymysql.connect(host="localhost", 
                             port=3306, 
                             user="root", 
                             password="example", 
                             database="MYDATABASE")
print("Connection Success!")

with connection.cursor() as cursor:
    # Create a table if it does not exist
    sqlQueryString = "CREATE TABLE IF NOT EXISTS Users (id int NOT NULL AUTO_INCREMENT, email varchar(255) NOT NULL, password varchar(255) NOT NULL, PRIMARY KEY (id)) AUTO_INCREMENT=1;"
    cursor.execute(sqlQueryString)
    connection.commit()

    # Create a new record
    sql = "INSERT INTO Users (email, password) VALUES (%s, %s)"
    cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # Read a single record
    sql = "SELECT `id`, `password` FROM `Users` WHERE `email`=%s"
    cursor.execute(sql, ('webmaster@python.org',))
    result = cursor.fetchone()
    print(result)

connection.close()
print("Connection Closed!")
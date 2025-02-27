import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host='localhost',
        database='vollmed_api',
        user='root',   
        password='Admin#2025'     )

    if connection.is_connected():
        print("Successfully connected to the database")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM medicos LIMIT 5;") 

        result = cursor.fetchall()

        for row in result:
            print(row)
    
except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

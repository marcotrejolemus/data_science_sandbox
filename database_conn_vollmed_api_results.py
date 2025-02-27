import mysql.connector
from mysql.connector import Error

try:
    # Establish connection to the database
    connection = mysql.connector.connect(
        host='localhost',        # e.g. 'localhost' or '127.0.0.1'
        database='vollmed_api', # Your database name
        user='root',    # Your MySQL username
        password='Admin#2025' # Your MySQL password
    )

    if connection.is_connected():
        print("Successfully connected to the database")
        cursor = connection.cursor()

        # Example query to fetch data
        cursor.execute("SELECT * FROM medicos LIMIT 5;")  # Replace with your table name

        # Fetch all rows of the query result
        result = cursor.fetchall()

        # Print each row
        for row in result:
            print(row)
    
except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if connection.is_connected():
        # Close the connection
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

import mysql.connector
from mysql.connector import Error

def get_user_data(user_id):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            database='vollmed_api',
            user='root',
            password='Admin#2025'
        )
        if conn.is_connected():
            cursor = conn.cursor()
            query = "SELECT * FROM medicos WHERE id = %s"
            cursor.execute(query, (user_id,))
            result = cursor.fetchall()
            return result
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

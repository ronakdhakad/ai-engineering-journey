import mysql.connector
from mysql.connector import Error

try:
    # 1. Establish the connection to the database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",          
        password="root@123",  
        database="pandas_db",
        port="3306"
    )

    if connection.is_connected():
        print("Connected to MySQL database successfully!")
        
        # 2. Create a cursor object to execute SQL commands
        cursor = connection.cursor()
        
        # 3. Execute a sample query
        cursor.execute("select * from student;") 
        
        # 4. Fetch and print the result
        rows= cursor.fetchall()
        print(rows)
        for row in rows:
            print(row)

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    # 5. Always close the cursor and connection when done
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed.")

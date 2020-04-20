import mysql.connector
from mysql.connector import Error

def connect_update():

    conn = None

     
    try:
         
        conn = mysql.connector.connect(host='localhost',database='demo',user='mmesomachukwu',password='mimisoso123',auth_plugin='mysql_native_password')
        print('Database Connecting')
        if conn.is_connected:
            print('Database connected')
             
            cursor = conn.cursor()

            print("Before Updating a record")
            sql_query = 'select * from games where OrderNumber = 0006'
            cursor.execute(sql_query)
            records = cursor.fetchone()
            print(records)

            sql_query_update = "update games set OrderMonth = 'October' where OrderNumber = 0006"
            cursor.execute(sql_query_update)
            conn.commit()
            print("record Updated Successfully")
    except Error as e:
        print('Connection failed due to the following :', e)
    finally:
        if conn is not None and conn.is_connected:
            conn.close
            print('Disconnected from database')

connect_update()



import mysql.connector
from mysql.connector import Error

def connect_fetch():

    conn = None
    try:
        conn = mysql.connector.connect(host="localhost",database="demo",user="mmesomachukwu",password="mimisoso123",auth_plugin="mysql_native_password")
        print("Database is connecting")
        if conn.is_connected:
            print("Database connected")
            sql_query = "Select * from human"
            cursor = conn.cursor()
            cursor.execute(sql_query)
            records = cursor.fetchall()
            print('Row count is: ', cursor.rowcount)
             
            for row in records:
                print("HumanId : ", row[0])
                print("Name : ", row[1])
                print("Color : ", row[2])
                print("Gender : ", row[3])
                print("Bloodgroup : ", row[4], '\n')
            
            sql_select_query ="Select * from games"
            cursor.execute(sql_select_query)
            records1 = cursor.fetchall()
            print('Row count is: ', cursor.rowcount)

            for row in records1:
                print("OrderNumber: ",row[0])
                print("StoreNumber: ",row[1])
                print("StoreZip: ", row[2])
                print("OrderMonth: ",row[3])
                print("OrderYear: ",row[4])
                print("OrderTotal: ",row[5])
                print("HumanId: ",row[6])
    except Error as e:
        print('Not connecting due to: ', e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('database shutdown')
connect_fetch()
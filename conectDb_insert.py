import mysql.connector
from mysql.connector import Error

def connect_insert():

    conn = None
    try:
        conn = mysql.connector.connect(host='localhost', database='demo',user='mmesomachukwu',password='mimisoso123',auth_plugin='mysql_native_password')
        print('Connecting to database')
        if conn.is_connected:
            print('Database is connected')
            cursor = conn.cursor()

            sql = "INSERT INTO HUMAN(HumanId,Name,Color,Sex,BloodGroup) Values(%s,%s,%s,%s,%s)"

            value = [
                        ('1005','Mallam Pedro','Grey','Male','B+'),
                        ('1006','Agness Sammu','Pink','Female','B-'),
                        ('1007','Huwaii Idion','Black','Male','O'),
                        ('1008','Mary Pauline','Grey','Female','O-')
                     ]

            cursor.execute(sql,value)
            #conn.commit()
            print(cursor.rowcount, "rows was inserted")
            
            
            cursor.close
            
    except Error as e:
        print('Failure in connecting is due to the following errors :', e)
    finally:
        if conn is not None and conn.is_connected:
            conn.close
            print('Connection Closed')
connect_insert()


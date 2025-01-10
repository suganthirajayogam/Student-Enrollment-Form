
import pymysql

def create_table():
    connection = pymysql.connect(host="127.0.0.1", user="root", password="", database="student")
    cursor = connection.cursor()
    cQuery = '''create table studdata(
                date VARCHAR(20),
                name CHAR(20),
                Mb_no VARCHAR(20),
                Alter_no VARCHAR(20),
                Email_id VARCHAR(50),
                Address VARCHAR(100),
                course VARCHAR(50),
                batch VARCHAR(50),
                came VARCHAR(50),
                exp VARCHAR(50),
                contact_per CHAR(20),
                couns VARCHAR(20),
                Fees VARCHAR(20),
                comment VARCHAR(255)
            )'''
    cursor.execute(cQuery)
    connection.commit()
    print("Table created successfully")
    connection.close()
    




        

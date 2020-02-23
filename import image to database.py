import pymysql
import os

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def pyinsertBLOB(conn, Species, photo, Class):
    print("Inserting BLOB into python_employee table")
    cursor = conn.cursor()
    try:
        sql_insert_blob_query = """  INSERT INTO caffe ( Species, photo, Class) VALUES (%s,%s,%s)"""

        empPicture = convertToBinaryData(photo)

        # Convert data into tuple format
        insert_blob_tuple =  ( Species, empPicture, Class)
        
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        
        
        print("Image and file inserted successfully as a BLOB into python_employee table", result)
    except:
        conn.rollback()
        print('Failed inserting BLOB data into MySQL table')

        
# set Database configure     
conn = pymysql.connect(host='localhost', user='root',
                       passwd='41464146', charset='utf8', autocommit=True)
cursor = conn.cursor()
cursor.execute("USE python_db")
cursor.execute("SET SQL_SAFE_UPDATES=0")

# set image path
folder = r"other_bean"

for filename in os.listdir(folder):
    pyinsertBLOB(conn, "caffe", os.path.join(folder,filename), "shell")
    conn.commit()

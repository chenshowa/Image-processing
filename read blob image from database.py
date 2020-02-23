import pymysql
from io import BytesIO
from PIL import Image

# set Database configure  
conn = pymysql.connect(host='localhost', user='root',
                       passwd='41464146', charset='utf8', autocommit=True)
cursor = conn.cursor()
cursor.execute("USE python_db")
cursor.execute("SET SQL_SAFE_UPDATES=0")

# read image from database
cursor.execute("SELECT photo FROM `caffe` WHERE Class='normal';")
record = cursor.fetchall()

# convert  binary format to digital data
for img in record:

    data = img[0]
    stream = BytesIO(data)
    photo = Image.open(stream)
    photo.show()

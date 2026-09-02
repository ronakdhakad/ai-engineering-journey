import mysql.connector as sqlcon

conn=sqlcon.connect(host="localhost",
                    database="demo_py",
                    user="root",
                    password="root@123",
                    port="3306")

cursor=conn.cursor()

query="insert into students (name , age) values ('ujjwal',22);"

cursor.execute(query)
conn.commit()

q2="select * from students;"

cursor.execute(q2)
data=cursor.fetchall()
print(data)
print("data inserted success.")
cursor.close()
conn.close()

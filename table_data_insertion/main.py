import mysql.connector
from datetime import date
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="temp_db"
)

# INSERT INTO orders (order_id, customer_id, order_date) VALUES (1,Customer 1,2023-01-20 02:19:20,ok);
val=''
cursor = mydb.cursor()
insrt = "INSERT INTO orders (order_id, customer_id) VALUES (?,?)"
for x in range(1,10):
    val = (x,'Customer')
    # print(val)
    cursor.execute(insrt, val)
    # print(val)
    # print(val)
#   insrt = 'INSERT INTO orders (order_id, customer_id, order_date) VALUES (',x,'Customer_',x,"'",date.today(),"'"
    # cursor.execute(insrt,val)

# print(val)
# mycursor.execute(sql, val)
# result = cursor.fetchmany(size =1000);
# print(result)

#Closing the connection
mydb.close()
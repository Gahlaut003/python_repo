import mysql.connector
import random
from datetime import date
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="temp_db"
)

# INSERT INTO orders (order_id, customer_id, order_date) VALUES (1,Customer 1,2023-01-20 02:19:20,ok);
cursor = mydb.cursor()

# Generate the random data
data = [(random.randint(1, 100), i_,random.randint(1, 100), date.today()) for i in range(10000)]

# Insert the data into the table
query = "INSERT INTO orders (order_id, customer_id, order_date) VALUES (%s, %s, %s)"
cursor.executemany(query, data)
mydb.commit()

import mysql.connector
import random
from datetime import datetime, timedelta

# Connect to the MySQL server
cnx  = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="temp_db"
)
cursor = cnx.cursor()

# Generate the random data
data = []
start_date = datetime(2020, 1, 1)
end_date = datetime(2022, 1, 1)
for i in range(100000):
    order_id = i+1 # to make sure the order_id is unique
    customer_id = random.randint(1, 1000)
    order_date = start_date + timedelta(days=random.randint(0, (end_date-start_date).days))
    data.append((order_id, customer_id, order_date))
print(data)
# Insert the data into the table
query = "INSERT INTO orders (order_id, customer_id, order_date) VALUES (%s, %s, %s)"
cursor.executemany(query, data)
cnx.commit()

# Close the cursor and connection
cursor.close()
cnx.close()
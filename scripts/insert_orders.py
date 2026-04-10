from db_connect import mycursor, mydb

sql = "INSERT INTO orders (user_id, product) VALUES (%s, %s)"
val = (2, "Laptop")

mycursor.execute(sql, val)
mydb.commit()

print("Order inserted!")
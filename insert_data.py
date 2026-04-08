from db_connect import mycursor, mydb

sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
val = ("Tejas", "tejas@gmail.com")

mycursor.execute(sql, val)
mydb.commit()

print("Data inserted!")
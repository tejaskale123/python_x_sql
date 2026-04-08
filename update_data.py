from db_connect import mycursor, mydb

sql = "UPDATE users SET name=%s WHERE id=%s"
val = ("Tejas Kale", 1)

mycursor.execute(sql, val)
mydb.commit()

print("Data updated!")
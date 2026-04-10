from db_connect import mycursor, mydb

sql = "DELETE FROM users WHERE id=%s"
val = (1,)

mycursor.execute(sql, val)
mydb.commit()

print("Data deleted!")
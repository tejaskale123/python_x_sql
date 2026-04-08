from db_connect import mycursor

mycursor.execute("SELECT * FROM users")

result = mycursor.fetchall()


for row in result:
    print(row)
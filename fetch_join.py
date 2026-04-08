from db_connect import mycursor

mycursor.execute("""
SELECT users.name, orders.product
FROM users
JOIN orders ON users.id = orders.user_id
""")

result = mycursor.fetchall()

for row in result:
    print(row)
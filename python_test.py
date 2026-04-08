import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Tejas@123"
)

print("Connected successfully!")
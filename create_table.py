from db_connect import mycursor

mycursor.execute("""
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
)
""")

print("Table created!")
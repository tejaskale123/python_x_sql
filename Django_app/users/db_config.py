import mysql.connector

def get_connection():
    """Create and return a new MySQL database connection"""
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Tejas@123",
            database="tejas_db"
        )
        return conn
    except mysql.connector.Error as err:
        raise Exception(f"Database connection failed: {err}")

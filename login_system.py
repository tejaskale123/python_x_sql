import mysql.connector
import hashlib

# 🔌 Database connect
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Tejas@123",
    database="tejas_db"
)

cursor = db.cursor()


# 🔥 REGISTER
def register():
    name = input("Enter name: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
    if cursor.fetchone():
        print("Email already exists!")
        return

    cursor.execute(
        "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
        (name, email, hashed_password)
    )
    db.commit()

    print("User registered successfully!")


# 🔥 CHANGE PASSWORD
def change_password(user):
    current_password = input("Enter current password: ")
    new_password = input("Enter new password: ")

    current_hashed = hashlib.sha256(current_password.encode()).hexdigest()

    if current_hashed != user[3]:
        print("Wrong current password!")
        return

    new_hashed = hashlib.sha256(new_password.encode()).hexdigest()

    cursor.execute(
        "UPDATE users SET password=%s WHERE id=%s",
        (new_hashed, user[0])
    )
    db.commit()

    print("Password updated successfully!")


# 🔥 FORGOT PASSWORD
def forgot_password():
    email = input("Enter your email: ").strip().lower()

    cursor.execute("SELECT * FROM users WHERE LOWER(TRIM(email))=%s", (email,))
    user = cursor.fetchone()

    if not user:
        print("Email not found!")
        return

    new_password = input("Enter new password: ")

    hashed = hashlib.sha256(new_password.encode()).hexdigest()

    cursor.execute(
        "UPDATE users SET password=%s WHERE email=%s",
        (hashed, email)
    )
    db.commit()

    print("Password reset successful!")


# 🔥 LOGIN
def login():
    email = input("Enter email: ")
    password = input("Enter password: ")

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    cursor.execute(
        "SELECT * FROM users WHERE email=%s AND password=%s",
        (email, hashed_password)
    )
    result = cursor.fetchone()

    if result:
        print("\nLogin successful!")
        print(f"Welcome {result[1]}!")

        while True:
            print("\n==== USER MENU ====")
            print("1. View Profile")
            print("2. Change Password")
            print("3. Logout")

            choice = input("Enter choice: ")

            if choice == "1":
                print(f"\nName: {result[1]}")
                print(f"Email: {result[2]}")

            elif choice == "2":
                change_password(result)

            elif choice == "3":
                print("Logged out!")
                break

            else:
                print("Invalid choice")

    else:
        print("Invalid credentials")


# 🔥 MAIN MENU
while True:
    print("\n==== MAIN MENU ====")
    print("1. Register")
    print("2. Login")
    print("3. Forgot Password")
    print("4. Exit")

    choice = input("Enter choice: ").strip().lower() 

    if choice == "1" or choice == "register":
        register()

    elif choice == "2" or choice == "login":
        login()

    elif choice == "3" or choice == "forgot":
        forgot_password()

    elif choice == "4" or choice == "exit":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
            
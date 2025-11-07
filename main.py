USERNAME_SYSTEM = "admin"
PASSWORD_SYSTEM = "secret"

def login(username, password):
    if username == USERNAME_SYSTEM and password == PASSWORD_SYSTEM:
        print("Login successful!")
    else:
        print("Login failed!")
    
username = input("Enter username: ")
password = input("Enter password: ")
login(username, password)
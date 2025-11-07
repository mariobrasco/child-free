def login(username, password):
    if username == "admin" and password == "secret":
        print("Login successful!")
    else:
        print("Login failed!")
    
username = input("Enter username: ")
password = input("Enter password: ")
login(username, password)

a = 13
b = 9
c = a * b
print(c)
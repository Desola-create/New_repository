
def get_all_users():
        users = ["Desola", "John", "Alice", "Bob"]
        return users

def user_info():
    username = input("Enter your name: ")
    password = input("Enter your password: ")

    if(username == "Desola" and password == "1234"):
        print("You are logged in, " + username)
    else:
        print("Access denied. Invalid username or password.")

def loop(): 
    for i in range(10):
        print("welcome")

def repeat():
    count = 0
    while (count <= 10):
        if(count == 10):
            continue
        count = count + 1

def exercise():
    name = input("Enter your name: ")
    if(name == "Desola"):
        print("Hello, " + name + "! Welcome back.")
    else:
        print("invalid name. Please try again.")

    

    
get_all_users()   
user_info()
loop()
repeat()
exercise()



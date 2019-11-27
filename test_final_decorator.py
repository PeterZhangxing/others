#!/usr/bin/python3.5

user,passwd = "zx","123"
def auth(auth_type):
    def outer_wrapper(func):
        def wrapper(*args,**kwargs):
            if auth_type == "local":
                username = input("Yourname: ")
                password = input("Your password: ")
                if username == user and password == passwd:
                    print("You have enter the home page!")
                    res = func(*args,**kwargs)
                    return res
                else:
                    exit("Invalid input!")
            elif auth_type == "ldap":
                print("Another athenticational method!")
        return wrapper
    return outer_wrapper

@auth(auth_type="local")
def home():
    print('welcome to the home page')
home()

import hashlib

def get_integer_input(message, error, low, high):
    while True:
        try:
            inpt = int(input(message))
            if low < inpt < high:
                return inpt
            else:
                print(error)
        except ValueError:
            print(error)

new_user = get_integer_input("would you like to creat a new user or login to existing user. \n1 new user. \n2 login to existing user. \n", "please enter 1 or 2 to select your answer", 0, 3)

if new_user == 1:
    f= open("QuizQuest/Username.txt", "a")
    Username = input("please enter a username. please note that no numbers are allowed. \n")
    Password = input("please enter a password. please note that no numbers are allowed. \n")
    Password_hashing = hashlib.sha224(Password.encode())
    hashed = Password_hashing.hexdigest()
    f.write(f"{Username} {hashed} \n")
    f.close()

if new_user == 2:
    f= open("QuizQuest/Username.txt", "r")
    Username = input("please enter your username. \n")
    Password = input("please enter your password. \n")
    Password_hashing = hashlib.sha224(Password.encode())
    hashed = Password_hashing.hexdigest()
    lines = f.readlines()
    clean_lines = []
    for line in lines:
        arr = line.split(' ')
        clean_lines.append(arr[0:2])
    for user, password in clean_lines:
        if user == Username and password == hashed:
            print("login successful")
        if user != Username or password != hashed:
            print("username or password incorrect")
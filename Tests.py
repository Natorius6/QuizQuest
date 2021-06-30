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
    f= open("QuizQuest/Username.py", "a")
    Username = input("please enter a username. please note that no numbers are allowed. \n")
    Password = input("please enter a password. please note that no numbers are allowed. \n")
    Password_hashing = hashlib.sha224(Password.encode())
    still_hashing = Password_hashing.hexdigest()
    hashed_password = (f"{still_hashing}")
    f.write(f"{Username} = '{hashed_password}'\n")
    f.close()
if new_user == 2:
    f= open("Username.py", "r")
    Username = input("please enter your username. \n")
    Password = input("please enter your password. \n")
    Password_hashing = hashlib.sha224(Password.encode())
    still_hashing = Password_hashing.hexdigest()
    hashed_password_check = (f"{still_hashing}")
    Username_check = hashed_password_check
    try:
        from Username.py import 
    except ImportError:
        print('User not found')
#    if :
#        print("success")
#    f.close()
import requests
from html import unescape
import hashlib
import os
import random

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

while True:
    response = requests.get('https://opentdb.com/api.php?amount=10&category=15&difficulty=easy&type=multiple')

    questions = response.json()['results']




    num_correct = 0

        
    new_user = get_integer_input("would you like to create a new user or login to existing user. \n1 new user. \n2 login to existing user. \n", "please enter 1 or 2 to select your answer", 0, 3)

    if new_user == 1:
        f= open("QuizQuest/Username.txt", "a")
        Username = input("please enter a username. please note that no numbers are allowed. \n")
        Password = input("please enter a password. please note that no numbers are allowed. \n")
        os.system('cls')
        Password_hashing = hashlib.sha224(Password.encode())
        hashed = Password_hashing.hexdigest()
        f.write(f"{Username} {hashed} \n")
        f.close()

    if new_user == 2:
        f= open("QuizQuest/Username.txt", "r")
        Username = input("please enter your username. \n")
        Password = input("please enter your password. \n")
        os.system('cls')
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

    print('''\033[1;32;40m
    *****************************WELCOME TO THE \033[1;31;40m QUIZ \033[1;32;40m QUEST*********************************
        \033[1;30;47m your mission if you choose to accept is to answer the most questions possible.\033[1;33;40m
    ''')
    num_correct = 0
    for i, question in enumerate(questions):
        print(f"question {i + 1}")
        print(unescape(question['question']))
        all_answers = []
        all_answers.append(question['correct_answer'])
        for ans in question["incorrect_answers"]:
            all_answers.append(ans)
        random.shuffle(all_answers)
        for num, ans in enumerate(all_answers):
            print(f"{num+1}: {ans}")
        correct_num = all_answers.index(question['correct_answer']) + 1
        user_answer = get_integer_input("\n", "that is not one of the options", 0, 5)
        if user_answer == correct_num:
            print("you got the right answer")
            num_correct += 1
        elif user_answer != num:
            print("you got it wrong try the next question")
        print(correct_num)
    if num_correct == 10:
        replay = input("congrats you got a perfect score. You are clearly a genius. \n Press enter to replay. \n")
    if 6 <= num_correct >= 9:
        replay = input("You nearly got a perfect score. So close \n Press enter to replay. \n")
    if 2 <= num_correct >= 5:
        replay = input("Nearly half points. Maybe try again. \n Press enter to replay. \n")
    if num_correct == 1:
        replay = input("You got one point \n Press enter to replay. \n")

# Ideas
# add multiple rounds
# add multiple users
# save history
# show highscore 
# show improvement over time
# statistics
# saving previous questions \ history to file
# chance to re answer wrong question - like a study app 
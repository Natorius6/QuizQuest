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

    logged_in = False

    quiz_finished = False
    num_questions = 0
    num_correct = 0

    while logged_in == False:
        new_user = get_integer_input("would you like to create a new user or login to existing user. \n1 new user. \n2 login to existing user. \n", "please enter 1 or 2 to select your answer", 0, 3)
        if new_user == 1:
            f= open("Username.txt", "a")
            username = input("please enter a username. please note that no numbers are allowed. \n")
            password = input("please enter a password. please note that no numbers are allowed. \n")
            os.system('cls')
            password_hashing = hashlib.sha224(password.encode())
            hashed = password_hashing.hexdigest()
            f.write(f"{username} {hashed} \n")
            f.close()
            logged_in = True

        if new_user == 2:
            f= open("Username.txt", "r")
            username = input("please enter your username. \n")
            password = input("please enter your password. \n")
            os.system('cls')
            password_hashing = hashlib.sha224(password.encode())
            hashed = password_hashing.hexdigest()
            lines = f.readlines()
            clean_lines = []
            for line in lines:
                arr = line.split(' ')
                clean_lines.append(arr[0:2])
            for user, password in clean_lines:
                if user == username and password == hashed:
                    print("login successful")
                    logged_in = True
                if user != username or password != hashed:
                    print("username or password incorrect")
            f.close()
            logged_in = True

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
            print(unescape(f"{num+1}: {ans}"))
        correct_ans = all_answers.index(question['correct_answer']) + 1
        user_answer = get_integer_input("\n", "answer the question with 1-4.", 0, 5)
        if user_answer == correct_ans:
            print("you got the right answer")
            num_correct += 1
            num_questions += 1
        elif user_answer != correct_ans:
            print("you got it wrong try the next question")
            num_questions += 1
        print(correct_ans)
        if num_questions == 10:
            quiz_finished = True
    if quiz_finished == True:
        if num_correct == 10:
            replay = input("congrats you got a perfect score. You are clearly a genius. \n Press enter to replay. \n")
        if 6 <= num_correct >= 9:
            replay = input(f"You got {num_correct}. So close \n Press enter to replay. \n")
        if 2 <= num_correct >= 5:
            replay = input(f"You got {num_correct}. Maybe try again. \n Press enter to replay. \n")
        if num_correct == 1:
            replay = input(f"You got {num_correct} \n Press enter to replay. \n")
        f= open("Scores.txt", "a")
        f.write(f"{username} {num_correct} \n")

# Ideas
# add multiple rounds
# add multiple users
# save history
# show highscore 
# show improvement over time
# statistics
# saving previous questions \ history to file
# chance to re answer wrong question - like a study app 
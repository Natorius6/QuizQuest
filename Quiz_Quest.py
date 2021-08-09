import requests
from html import unescape
import hashlib
import os
import random

def register_user():
    check_login_file = open("QuizQuest/Username.txt", "r")
    username = input("please enter a username. please note that no spaces are allowed. \n")
    password = input("please enter a password. please note that no spaces are allowed. \n")
    lines = check_login_file.readlines()
    clean_lines = []
    valid = False
    for line in lines:
        arr = line.split(' ')
        clean_lines.append(arr[0:2])
    for user, password in clean_lines:
        if username == user:
            print("username already taken")
    os.system('cls')
    login_file = open("QuizQuest/Username.txt", "a")
    password_hashing = hashlib.sha224(password.encode())
    hashed = password_hashing.hexdigest()
    login_file.write(f"{username} {hashed} \n")
    login_file.close()
    scores_file = open("QuizQuest/Scores.txt", "a")
    scores_file.write(f"{username} 0\n")
    scores_file.close()
    logged_in = True

def get_highscore():
    f= open("QuizQuest/scores.txt", "r")
    lines = f.readlines()
    clean_lines = []
    for line in lines:
        arr = line.split(' ')
        clean_lines.append(arr[0:2])
    for user, score in clean_lines:
        if user == username:
            if int(score) < 1:
                print("You have not played the quiz yet")
            else:
                print(f"{user}s highscore is {score}")
    return_to_homebase = input("press enter to return to homebase. \n")

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

def give_user_score(num_correct):
    if num_correct == 10:
        replay = input("congrats you got a perfect score. You are clearly a genius. \n Press enter to return to homebase. \n")
    if 6 <= num_correct >= 9:
        replay = input(f"You got {num_correct} correct. So close \n Press enter to return to homebase. \n")
    if num_correct == 5:
        replay = input(f"You got {num_correct} correct. average score. \n Press enter to return to homebase. \n")
    if 2 <= num_correct >= 4:
        replay = input(f"You got {num_correct} correct. Maybe try again. \n Press enter to return to homebase. \n")
    if num_correct == 1:
        replay = input(f"You got {num_correct} correct \n Press enter to return to homebase. \n")

def finish_quiz(num_correct):
    give_user_score(num_correct)
    new_file_info = ""
    scores_file = open("QuizQuest/Scores.txt", "r")
    lines = scores_file.readlines()
    clean_lines = []
    for line in lines:
        user, score = line.split(' ')
        if user == username:
            if int(score) < num_correct:
                new_line_info = line.replace(score,str(num_correct))
                new_file_info = f"{new_file_info}{new_line_info}\n"
            else:
                new_file_info = f"{new_file_info}{line}"
        else:
            new_file_info = f"{new_file_info}{line}"
    scores_file.close()
    with open("QuizQuest/Scores.txt", "w") as scores_file:
        scores_file.write(new_file_info)


logged_in = False

while True:

    file = open("QuizQuest/Scores.txt", "a")
    file.close()

    file = open("QuizQuest/Username.txt", "a")
    file.close()

    response = requests.get('https://opentdb.com/api.php?amount=10&category=15&difficulty=easy&type=multiple')

    questions = response.json()['results']

    num_correct = 0

    while logged_in == False:
        new_user = get_integer_input("would you like to create a new user or login to existing user. Please note that you have to create an account if on a new machine. \n1 new user. \n2 login to existing user. \n", "please enter 1 or 2 to select your answer", 0, 3)
        #creates new user
        if new_user == 1:
            register_user()

        #logs in to existing user
        if new_user == 2:
            login_file = open("QuizQuest/Username.txt", "r")
            username = input("please enter your username. \n")
            password = input("please enter your password. \n")
            os.system('cls')
            password_hashing = hashlib.sha224(password.encode())
            hashed = password_hashing.hexdigest()
            lines = login_file.readlines()
            clean_lines = []
            valid = False
            for line in lines:
                arr = line.split(' ')
                clean_lines.append(arr[0:2])
            for user, password in clean_lines:
                if user == username and password == hashed:
                    print("login successful")
                    valid = True
                    logged_in = True
            if valid == False:
                print("username or password incorrect")
            login_file.close()

    print('''\033[1;32;40m
    *****************************WELCOME TO THE \033[1;31;40m QUIZ \033[1;32;40m QUEST*********************************
        \033[1;30;47m your mission if you choose to accept is to answer the most questions possible.\033[1;33;40m
    ''')

    print("Welcome to your home base, from here you can go do the quiz or check your highscore.")
    #user picks where to go
    gamemode = get_integer_input("what would you like to do \n1 highscore. \n2 gaming quiz. \n3 quit \n", "please enter 1, 2 or 3 to select your answer.", 0, 4)

    #quit
    if gamemode == 3:
        print("mission failed, we'll get them next time.")
        break

    #highscores
    if gamemode == 1:
        get_highscore()


    #quiz
    if gamemode == 2:
        quiz_finished = False
        num_questions = 0
        num_correct = 0

        for i, question in enumerate(questions):
            print(f"question {i + 1}")
            print(unescape(question['question']))
            question_answers = []
            question_answers.append(question['correct_answer'])
            for ans in question["incorrect_answers"]:
                question_answers.append(ans)
            random.shuffle(question_answers)
            for num, ans in enumerate(question_answers):
                print(unescape(f"{num+1}: {ans}"))
            correct_ans = question_answers.index(question['correct_answer']) + 1

            #gets users answer
            user_answer = get_integer_input("\n", "answer the question with 1-4.", 0, 5)
            if user_answer == correct_ans:
                print("you got the right answer\n")
                num_correct += 1
                num_questions += 1
            elif user_answer != correct_ans:
                print("you got it wrong")
                print(f"the correct answer was {correct_ans}\n")
                num_questions += 1
            if num_questions == 10:
                quiz_finished = True

        #tells user what their score was
        if quiz_finished == True:
            finish_quiz(num_correct)
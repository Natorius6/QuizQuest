import requests
from html import unescape

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


response = requests.get('https://opentdb.com/api.php?amount=10&category=15&difficulty=easy&type=multiple')

questions = response.json()['results']



print('''
*****************************WELCOME TO THE QUIZ QUEST*********************************
                    answer the most questions correctly as you can
''')

num_correct = 0

for i, question in enumerate(questions):
    print(f"******************************Question {i + 1}***************************")
    print(unescape(question['question']))
    print(1, question['correct_answer'])
    for i, wrong_ans in enumerate(question['incorrect_answers']):
        print(i + 2, wrong_ans)
    user_answer = get_integer_input('Type 1, 2, 3 or 4 to select your answer \n', 'Please select your answer using by typing 1, 2, 3 or 4', 0, 5)
    if user_answer == question['correct_answer']:
        print('congrats you got the answer correct!')
        num_correct += 1
    elif user_answer == wrong_ans:
        print('You got the answer incorrect!')
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
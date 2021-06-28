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
    print(question['question'])
    print(1, question['correct_answer'])
    for i, wrong_ans in enumerate(question['incorrect_answers']):
        print(i + 2, wrong_ans)
    user_answer = get_integer_input('Type 1, 2, 3 or 4 to select your answer', 'Please select your answer using by typing 1, 2, 3 or 4', 0, 5)
    if user_answer == 1:
        print('congrats you got the answer correct!')
        num_correct += 1
    elif user_answer == 2 or 3 or 4:
        print('You got the answer incorrect!')
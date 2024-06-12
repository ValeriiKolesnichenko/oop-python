import random
from classes import Participant
# Creating a participant
participant = Participant('Oleg')

questions = [
    {'Who is considered the greatest chess player of all time?': 'Garry Kasparov'},
    {'What is the term for a move that puts the opponent\'s king in a position where it cannot escape capture?': 'Checkmate'},
    {'In which country did the game of chess originate?': 'India'},
    {'How many squares are there on a standard chessboard? (Enter the number)': '64'},
    {'Who is the most popular chess youtuber nowadays?': 'Levy Rozman'},
    {'Who holds the record for the most points scored in a single NBA game?': 'Wilt Chamberlain'},
    {'Which NBA player is known as "The King"?': 'Lebron James'},
    {'How many players are on the court for each team during a standard basketball game?(spell a number)': 'Five'},
    {'Which team won the first NBA championship?': 'Philadelphia Warriors'},
    {'Which NBA player is known as "Black Mamba"?': 'Kobe Bryant'},
]
user_input = input('Hello! It is really cool to see you here! Do you want to play sport quiz?\n'
                   '-Yes\n'
                   '-No\n')
while True:
    if user_input.lower().strip() == 'yes':
        try:
            random_dict_question = random.choice(questions)  # -> variable, which refers to dict with {'question': 'answer'}
            question = list(random_dict_question.keys())[0]  # -> Retrieving the question
            print(f'Question: {question}')
        except Exception as e:
            print('The quiz done!')
            break
        answer = input('Your answer: ')
        # checking whether user's answer is correct.
        if answer.capitalize().strip() == random_dict_question[question].capitalize().strip():
            print('Correct!')
            participant.add_points()
            questions.remove(random_dict_question)
        else:
            print('Wrong!')
            participant.delete_points()
            questions.remove(random_dict_question)
    elif user_input.lower().strip() == 'no':
        break
    else:
        print('Incorrect choice. Try again')
        break

print('Good Bye!')

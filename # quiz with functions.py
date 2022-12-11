# quiz with functions

def ask_question(question, answer):
    if input(question).lower() == answer.lower():
        print('Correct!')
    else:
        print('Incorrect')


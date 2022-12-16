
class Quiz:
    def __init__(self, questions):
        self.questions = questions
    
    def ask_questions(self):
        # Ask each question in the list of questions
        for question in self.questions:
            answer = input(question['text'] + ' ')

            # Check if the answer is correct
            if answer.lower() == question['answer'].lower():
                print('Correct!')
            else:
                print('Incorrect')

# Create a list of quiz questions
questions = [
    {'text': "Powershell commands are based on what kind of relationship?", 'answer': 'verb noun'},
    {'text': "Powershell commands are referred to as...?", 'answer': 'cmdlets'},
    {'text': "To update help for Powershell, you use the command...? Clue: U...-H...", 'answer': 'Update-Help'},
    {'text': "To get help for a specific command, you use the command...?", 'answer': 'Get-Help <command>'},
    {'text': "To get a list of all the commands in a module, you use the command...?", 'answer': 'Get-Command -Module <module>'},
    {'text': "To get a list of all the modules, you use the command...?", 'answer': 'Get-Module'},
    {}
]

# Create a Quiz object
quiz = Quiz(questions)

# Ask the questions
quiz.ask_questions()

# Print a message when the quiz is finished
print("That's all the questions for now! Thanks for playing! ")

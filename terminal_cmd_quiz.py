# Import the necessary libraries
import random

class Quiz:
    def __init__(self):
        # Create a list of quiz questions and answers
        self.questions = [
            {"question": "What command is used to create a new directory?", "answer": "mkdir"},
            {"question": "What command is used to change the current directory?", "answer": "cd"},
            {"question": "What command is used to display the contents of a file?", "answer": "cat"},
            {"question": "What command is used to search for a string in a file?", "answer": "grep"},
            {"question": "What command is used to run a command with root privileges?", "answer": "sudo"},
            {"question": "What command is used to list the contents of a directory?", "answer": "ls"},
            {"question": "What command is used to print the current working directory?", "answer": "pwd"},
            {"question": "What command is used to copy files?", "answer": "cp"},
            {"question": "What command is used to move files?", "answer": "mv"},
            {"question": "What command is used to remove files?", "answer": "rm"},
            {"question": "What command is used to display the current date and time?", "answer": "date"},
            {"question": "What command is used to create a new file?", "answer": "touch"},
            
        ]

        # Shuffle the questions
        random.shuffle(self.questions)

        # Initialize the score
        self.score = 0

    def ask_question(self, question):
        # Ask the question
        print(question["question"])

        # Get the user's answer
        answer = input("Your answer: ")

        # Check if the answer is correct
        if answer.lower() == question["answer"].lower():
            # Increment the score
            self.score += 1

            # Print a correct message
            print("Correct!")
        else:
            # Print an incorrect message
            print(f"Incorrect. The correct answer is {question['answer']}.")

    def start(self):
        # Loop through the questions
        for question in self.questions:
            self.ask_question(question)

        # Print the final score
        print(f"You scored {self.score} out of {len(self.questions)}.")

# Create a new Quiz object
quiz = Quiz()

# Start the quiz
quiz.start()

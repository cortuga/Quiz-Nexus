# Import the necessary libraries
import random

class Quiz:
    def __init__(self):
        # Create a list of quiz questions and answers
        self.questions = [
            {"question": "What is the command for cloning a repository?", "answer": "git clone"},
            {"question": "What is the command for checking the current status of files in a repository?", "answer": "git status"},
            {"question": "What is the command for adding files to the staging area?", "answer": "git add"},
            {"question": "What is the command for committing changes to a repository?", "answer": "git commit"},
            {"question": "What is the command for pushing changes to a remote repository?", "answer": "git push"},
            {"question": "What is the command for pulling changes from a remote repository?", "answer": "git pull"},
            {"question": "What is the command for viewing the commit history of a repository?", "answer": "git log"},
            {"question": "What is the command for branching in a repository?", "answer": "git branch"},
            {"question": "What is the command for merging branches in a repository?", "answer": "git merge"},
            {"question": "What is the command for displaying differences between files in a repository?", "answer": "git diff"}
            
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

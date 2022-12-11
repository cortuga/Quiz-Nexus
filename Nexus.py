# import libraries for quiz functions
# set introduction prompts
# call functions for each quiz
# culminate with a final score
# import powershell_quiz as ps
import math
import python_quiz as pyt

# def progress_bar(progress, total):
#     percent = 100 * (progress / float(total))
#     bar = '█' * int(percent) + '-' * (100 - int(percent))
#     print(f"\r|{bar}| {percent:.2f}%", end="\r")
    
# numbers = [x * 5 for x in range(2000, 3000)]
# results = []

# for i, x in enumerate(numbers):
#     results.append(math.factorials(x))
#     progress_bar(0, len(numbers))

print('Welcome to the quiz nexus!' )

playing = input("Do you want to learn? ")

if playing.lower() != "yes":
    quit()
    print("OK! Let's go! ")
    
pyt.pythonTest()

def nexusGreetings():
    print('Welcome to the quiz nexus!' )
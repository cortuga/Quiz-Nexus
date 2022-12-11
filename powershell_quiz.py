
print('Welcome to the terminal nexus Quiz!' )

playing = input("Do you want to learn? ")

if playing.lower() != "yes":
    quit()
    print("OK! Let's go! :)")

answer = input("Powershell commands are based on what kind of relationship? ")
if answer.lower() == 'verb noun':
    print('Correct!')
else:
    print('Incorrect')

answer = input("Powershell commands are referred to as...? ")
if answer.lower() == 'cmdlets':
    print('Correct!')
else:
    print('Incorrect')
    
answer = input("To update help for Powershell, you use the command...? Clue: U...-H... ")
if answer.lower() == 'Update-Help'.lower():
    print('Correct!')
else:
    print('Incorrect \n Update-Help is the correct answer')
    
answer = input("To get help for a specific command, you use the command...? ")
if answer == 'Get-Help <command>':
    print('Correct!')
else:
    print('Incorrect')
    
    print("That's all the questions for now! Thanks for playing! ")
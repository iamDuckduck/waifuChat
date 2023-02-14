from promptModule import promptSetUp

userChoice = input('1 for the most customized prompt \n'
                   '2 for creating a similar characteristic of a well-known character\n'
                   '3 for testing the prompt(pre-set background)\n'
                   'Please input:')

while not (userChoice == '1' or userChoice == '2' or userChoice == '3'):
    userChoice = input('error. Please input 1,2 or 3:')


promptSetUp(userChoice)

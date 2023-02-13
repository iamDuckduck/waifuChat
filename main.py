from promptModule import promptSetUp

userPrompt = input('1 for the most customized prompt \n'
                   '2 for creating a similar characteristic of a well-known character\n'
                   '3 for testing the prompt(pre-set background)\n'
                   'Please input:')

while not (userPrompt == '1' or userPrompt == '2' or userPrompt == '3'):
    userPrompt = input('error. Please input 1,2 or 3:')


promptSetUp(userPrompt)


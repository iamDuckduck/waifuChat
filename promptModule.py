from promptDrawing import promptForDrawing1
from promptDrawing import promptForDrawing2
from promptDrawing import previewDrawing
from chatgpt_wrapper import ChatGPT  ##https://stackoverflow.com/questions/31235376/pycharm-doesnt-recognize-installed-module, if chatgpt_wrapper not working try to find solution from the link


def promptSetUp(userChoice): ##receive prompt setting from the user

    if userChoice == '1': ##option 1
        bot = ChatGPT()
        preview = '1'

        while preview == '1':
            name = input("What is the name of your waifu? ")
            gender = input("What is the gender of your waifu?(female or male) ")
            if gender == 'female':
                gender = '1girl'
            elif gender == 'male':
                gender = '1boy'

            hair = (input("What is the hair color of your waifu? ") + " hair")
            eye = (input("What is the eye color of your waifu? ") + " eyes")
            clothes = input("What clothes is your waifu wearing? ")
            trait = input("What Characteristics do you want your waifu to have? ")
            userPrompt = f"{gender}, {hair}, {eye}, {clothes}, {trait}"
            print('Previewing your waifu.')
            previewDrawing(hair, userPrompt)
            preview = input('press 1 if you want to regenerate your waifu, else press 2:')

        print("Generating your waifu, please wait......")
        character = bot.ask("Can you help me to create a character in 200 words, with the name " + name +
                            " and the following characteristics " + trait + ". The character also need to be " + gender +
                            ". The character also need to have " + hair + eye + clothes)
        print(character)
        bot.ask(
            "I want you to act like " + name + ". I want you to respond and answer like " + name + ". Using the tone, manner and vocabulary " + name + "would use. Do not write any explanations. Only answer like " + name + ". You must know all of the knowledge of " + name + ".")

        promptForDrawing1(bot, userPrompt, name)

    if userChoice == '2':
        bot = ChatGPT()
        preview = '1'

        while preview == '1':
            name = input("What is the name of your waifu? ")
            series = input("from what series? ")
            hair = (input("What is the hair color of your waifu? ") + " hair")
            eye = (input("What is the eye color of your waifu? ") + " eyes")
            otherTrait = input('other things you would like to add?(Yes or No)')
            if otherTrait == 'Yes':
                otherTrait = input('please input:')
            else:
                otherTrait = ''

            userPrompt = f"{hair}, {eye}, {otherTrait}"
            print('Previewing your waifu.')
            previewDrawing(hair, userPrompt)
            preview = input('press 1 if you want to regenerate your waifu, else press 2:')

        print("Generating your waifu, please wait......")

        bot.ask(
            "I want you to act like " + name + " from " + series + ". I want you to respond and answer like " + name + ". Using the tone, manner and vocabulary " + name + " would use. Do not write any explanations. Only answer like " + name + ". You must know all of the knowledge of " + name + "." + "My first sentence is Hi " + name + ".")

        print(f"{name}: {bot.ask(f'User: Hi {name}')}")
        promptForDrawing2(bot, name, userPrompt)

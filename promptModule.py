from promptDrawing import promptForDrawing1
from promptDrawing import promptForDrawing2
from promptDrawing import previewDrawing
from chatgpt_wrapper import ChatGPT ##https://stackoverflow.com/questions/31235376/pycharm-doesnt-recognize-installed-module, if chatgpt_wrapper not working try to find solution from the link
import os


def promptSetUp(userPrompt):##receive prompt setting from the
    if userPrompt == '1':
        bot = ChatGPT()
        name = input("What is the name of your CodeMate? ")
        gender = input("What is the gender of your CodeMate? ")
        hair = (input("What is the hair color of your CodeMate? ") + " hair")
        eye = (input("What is the eye color of your CodeMate? ") + " eyes")
        clothes = input("What clothes is your CodeMate wearing? ")
        trait = input("What Characteristics do you want your CodeMate to have? ")
        print("Generating your CodeMate, please wait......")

        character = bot.ask(
            "Can you help me to create a character in 200 words, with the name " + name + " and the following characteristics " + trait + ". The character also need to be " + gender + ". The character also need to have " + hair + eye + clothes)
        print(character)
        bot.ask(
            "I want you to act like " + name + ". I want you to respond and answer like " + name + ". Using the tone, manner and vocabulary " + name + "would use. Do not write any explanations. Only answer like " + name + ". You must know all of the knowledge of " + name + ".")

        promptForDrawing1(bot, gender, hair, eye, clothes, trait, name)

    if userPrompt == '2':
        bot = ChatGPT()
        preview = 1
        while preview == 1:
            name = input("What is the name of your waifu? ")
            series = input("from what series? ")
            hair = (input("What is the hair color of your waifu? ") + " hair")
            eye = (input("What is the eye color of your waifu? ") + " eyes")
            previewDrawing(hair, eye)
            preview = input('press 1 if you want to regenerate your waifu, else press 2')
        print("Generating your waifu, please wait......")
        bot.ask(
            "I want you to act like " + name + " from " + series + ". I want you to respond and answer like " + name + ". Using the tone, manner and vocabulary " + name + " would use. Do not write any explanations. Only answer like " + name + ". You must know all of the knowledge of " + name + "." + "My first sentence is Hi " + name +".")
        temp = bot.ask(f'User: Hi {name}')
        print(f"{name}: {temp}")

        promptForDrawing2(bot, hair, eye, name)
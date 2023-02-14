import replicate
from PIL import Image
import requests
from io import BytesIO
import os


def promptForDrawing1(bot, userPrompt, name):
    os.environ["REPLICATE_API_TOKEN"] = "4e43941c916c15479dd0d72421a8c51c5a905bba"
    image = "Please list no more than 6 keywords from our conversation, we will use them for image generator."

    while True:
        user_input = input("You : ")
        if user_input == "exit":
            break

        if user_input == "Image.":
            response = bot.ask(image)
            keyword = response
            print("keyword: \n", keyword, "Generating Image......")

            model = replicate.models.get("cjwbw/anything-v3-better-vae")
            version = model.versions.get("09a5805203f4c12da649ec1923bb7729517ca25fcac790e640eaa9ed66573b65")

            # https://replicate.com/cjwbw/anything-v3-better-vae/versions/09a5805203f4c12da649ec1923bb7729517ca25fcac790e640eaa9ed66573b65#input
            inputs = {
                # Input prompt
                'prompt': "masterpiece, best quality, 1person, age friendly " + userPrompt + keyword,

                # The prompt or prompts not to guide the image generation (what you do
                # not want to see in the generation). Ignored when not using guidance.
                # 'negative_prompt': ...,

                # Width of output image. Maximum size is 1024x768 or 768x1024 because
                # of memory limits
                'width': 512,

                # Height of output image. Maximum size is 1024x768 or 768x1024 because
                # of memory limits
                'height': 512,

                # Number of images to output
                'num_outputs': 1,

                # Number of denoising steps
                # Range: 1 to 500
                'num_inference_steps': 20,

                # Scale for classifier-free guidance
                # Range: 1 to 20
                'guidance_scale': 7,

                # Choose a scheduler.
                'scheduler': "DPMSolverMultistep",

                # Random seed. Leave blank to randomize the seed
                # 'seed': ...,
            }

            # https://replicate.com/cjwbw/anything-v3-better-vae/versions/09a5805203f4c12da649ec1923bb7729517ca25fcac790e640eaa9ed66573b65#output-schema
            output = version.predict(**inputs)
            response = requests.get(output[0])
            img = Image.open(BytesIO(response.content))
            img.show()
        else:
            response = bot.ask(user_input)
            print(name, ": ", response)

def promptForDrawing2(bot, name, userPrompt):
    os.environ["REPLICATE_API_TOKEN"] = "4e43941c916c15479dd0d72421a8c51c5a905bba"
    image = "Please list no more than 6 keywords from our conversation, we will use them for image generator."

    while True:
        user_input = input("You : ")
        if user_input == "exit":
            break

        if user_input == "Image.":
            response = bot.ask(image)
            keyword = response
            print("keyword: \n", keyword, "Generating Image......")

            model = replicate.models.get("cjwbw/anything-v3-better-vae")
            version = model.versions.get("09a5805203f4c12da649ec1923bb7729517ca25fcac790e640eaa9ed66573b65")

            # https://replicate.com/cjwbw/anything-v3-better-vae/versions/09a5805203f4c12da649ec1923bb7729517ca25fcac790e640eaa9ed66573b65#input
            inputs = {
                # Input prompt
                'prompt': "masterpiece, best quality, 1girl, age friendly " + userPrompt,

                # The prompt or prompts not to guide the image generation (what you do
                # not want to see in the generation). Ignored when not using guidance.
                # 'negative_prompt': ...,

                # Width of output image. Maximum size is 1024x768 or 768x1024 because
                # of memory limits
                'width': 512,

                # Height of output image. Maximum size is 1024x768 or 768x1024 because
                # of memory limits
                'height': 512,

                # Number of images to output
                'num_outputs': 1,

                # Number of denoising steps
                # Range: 1 to 500
                'num_inference_steps': 20,

                # Scale for classifier-free guidance
                # Range: 1 to 20
                'guidance_scale': 7,

                # Choose a scheduler.
                'scheduler': "DPMSolverMultistep",

                # Random seed. Leave blank to randomize the seed
                # 'seed': ...,
            }

            # https://replicate.com/cjwbw/anything-v3-better-vae/versions/09a5805203f4c12da649ec1923bb7729517ca25fcac790e640eaa9ed66573b65#output-schema
            output = version.predict(**inputs)
            response = requests.get(output[0])
            img = Image.open(BytesIO(response.content))
            img.show()
        else:
            response = bot.ask(user_input)
            print(name, ": ", response)

def previewDrawing(hair, userPrompt):
    os.environ["REPLICATE_API_TOKEN"] = "4e43941c916c15479dd0d72421a8c51c5a905bba"
    model = replicate.models.get("cjwbw/anything-v3-better-vae")
    version = model.versions.get("09a5805203f4c12da649ec1923bb7729517ca25fcac790e640eaa9ed66573b65")

    # https://replicate.com/cjwbw/anything-v3-better-vae/versions/09a5805203f4c12da649ec1923bb7729517ca25fcac790e640eaa9ed66573b65#input
    inputs = {
        # Input prompt
        'prompt': "masterpiece, best quality, 1girl, age friendly " + hair + userPrompt,

        # The prompt or prompts not to guide the image generation (what you do
        # not want to see in the generation). Ignored when not using guidance.
        # 'negative_prompt': ...,

        # Width of output image. Maximum size is 1024x768 or 768x1024 because
        # of memory limits
        'width': 512,

        # Height of output image. Maximum size is 1024x768 or 768x1024 because
        # of memory limits
        'height': 512,

        # Number of images to output
        'num_outputs': 1,

        # Number of denoising steps
        # Range: 1 to 500
        'num_inference_steps': 20,

        # Scale for classifier-free guidance
        # Range: 1 to 20
        'guidance_scale': 7,

        # Choose a scheduler.
        'scheduler': "DPMSolverMultistep",

        # Random seed. Leave blank to randomize the seed
        # 'seed': ...,
    }

    # https://replicate.com/cjwbw/anything-v3-better-vae/versions/09a5805203f4c12da649ec1923bb7729517ca25fcac790e640eaa9ed66573b65#output-schema
    output = version.predict(**inputs)
    response = requests.get(output[0])
    img = Image.open(BytesIO(response.content))
    img.show()

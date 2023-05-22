import openai
openai.api_key = "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"

currentUser = "NandoGod"

#Used to call the completion
def get_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use the Davinci model for best results
        prompt=prompt,
        max_tokens= 300,
        n=1,
        stop=None,
        temperature=0.5,
        user = currentUser
    )

    message = response.choices[0].text.strip()
    return message

#Used to call the imageCompletion
def get_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024",
        user = currentUser
    )
    image_url = response['data'][0]['url']
    return image_url
    
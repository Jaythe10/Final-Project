import os
import openai # pip install openai


openai.api_key = ""

user_project = "cat wesring red cape"

response = openai.Image.create(
    prompt="user_prompt",
    n=1,
    size="1024x1024"
)


image_url = response['data'][0]['url']
print(image_url)
 
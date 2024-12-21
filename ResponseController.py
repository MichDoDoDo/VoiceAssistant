from openai import OpenAI
import os
from dotenv import load_dotenv

class ResponseControler:
    Chatlog = {}
    text = ''
    def __init__(self):
        pass
    def generate_chat_response(self, message):
        load_dotenv()
        
        client = OpenAI()
        response =  client.chat.completions.create(
            model= "gpt-3.5-turbo",
            messages=[
                {
                    "role": "assistant", "content": "you are a helpful voice assistant, like jarvis from ironman"
                },
                {
                    "role" : "user",
                    "content": str(message)
                }
            ]
        ) 
        print(response.choices[0].message.content)
        self.Chatlog.update({message:response.choices[0].message.content})
        self.text = response.choices[0].message.content
        return 
    
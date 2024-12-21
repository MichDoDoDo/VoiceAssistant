import os
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError
from playsound import playsound 
from pathlib import Path
class TextToSpeechController:
    
    def __init__(self):
        pass
    
    
    def  generate_TTS(self, message):
        load_dotenv()
        client = OpenAI()
        try: 
            response = client.audio.speech.create(
                model="tts-1",
                voice="nova",
                input=str(message),
            )
            
            currentDirc = os.getcwdb()

            response.stream_to_file("test.mp3")
            
            playsound("test.mp3")
            
            if(os.path.exists("test.mp3")):
                os.remove("test.mp3")
                
            print("now im done")
        except OpenAIError as ex:
            print("Error occured while fetching audio stream " + ex)
        
    def TTS(self, message): 

        print("bn")
        
import speech_recognition as speech
import os
class SpeechToTextController:
    
    text = ""
    history = []
    device = None
    
    def __init__(self, language):
        self.speechLanguage = language 
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="credentials.json"
        
    def fetch_audio_from_mic(self):
        while True: 
            record = speech.Recognizer()
            try:
                with speech.Microphone(device_index= self.device) as micSource:
                    record.adjust_for_ambient_noise(source=micSource, duration=0.5)
                    audio = record.listen(micSource)
                    outputText = record.recognize_google_cloud(audio)
                    return outputText
            except speech.UnknownValueError:
                print("UnknownValueError")
                continue
        
    def record_stt(self):
        text = self.fetch_audio_from_mic()
        self.text = text
        self.history.append(text)
             
    def initiate_speech(self):
        while True:
            text = self.fetch_audio_from_mic()
            if "hello helper" in text:
                self.text = text
                return True
                    
    def select_mic(self):
        vailddevice = False
        mics = speech.Microphone
        
        workingdevice = mics.list_working_microphones()
        for key, value in workingdevice.items() :
            print(f"Index {key} Mic: {value}")
        while not vailddevice :
            selectedDevice = input ("please enter the index of the Mic you would like to use: ")
            if(int(selectedDevice) in workingdevice.keys()):
                self.device = int(selectedDevice)
                vailddevice = True
            
        
        
    
       
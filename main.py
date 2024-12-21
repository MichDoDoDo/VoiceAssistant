from SpeechToTextController import SpeechToTextController
from SupportedLanguages import Languages
from ResponseController import ResponseControler
from TextToSpeechController import TextToSpeechController
def main():
    #lets call the methode to get the messsages from mic
    recordFromMic = SpeechToTextController(Languages.ENGLISH)
    recordFromMic.select_mic()
    if recordFromMic.initiate_speech():
        generateSpeechResponse = ResponseControler()
        textToSpeechAudio = TextToSpeechController()
        generateSpeechResponse.generate_chat_response(recordFromMic.text)

        while True:
            recordFromMic.record_stt()
            generateSpeechResponse.generate_chat_response(recordFromMic.text)
            textToSpeechAudio.generate_TTS(generateSpeechResponse.text)
    
if __name__ == "__main__":
    main()
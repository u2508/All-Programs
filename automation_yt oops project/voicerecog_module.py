import speech_recognition as sr
import pyttsx3
class recog:
	speak = sr.Recognizer()
	engine = pyttsx3.init('sapi5')
	voices = engine.getProperty('voices')
	voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
	engine.setProperty('rate', 125)
# Use female voice
	engine.setProperty('voice', voice_id)
obj=recog
def Speech(audio):
    
    obj.engine.say(audio)
    obj.engine.runAndWait()
    
def voice ():
	
		try:
			with sr.Microphone() as mic:
	
		# adjust the energy threshold based on
				# the surrounding noise level
				obj.speak.adjust_for_ambient_noise(mic,duration=2)
				print("listening...")
		
		# listens for the user's input
				searchquery = obj.speak.listen(mic)
		
		# Using google to recognize audio
				MyText = obj.speak.recognize_google(searchquery)
				text = MyText.lower()
				Speech('you said'+text)
				return text
		except sr.RequestError as e:
			print("Could not request results; {0}".format(e))

		except sr.UnknownValueError:
			pass
if __name__ == '__main__':
    Speech("hello sir")
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import speech_recognition as sr
import pyttsx3
import time
from selenium.webdriver.chrome.service import Service
def automateYoutube(searchtext):
    # giving the path of chromedriver to selenium webdriver
    path = "chromedriver.exe"
    url = "https://www.youtube.com/"
    # opening the youtube in chromedriver
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument('--log-level=3')
    options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
    path=Service("C:\Program Files\BraveSoftware\Brave-Browser\Application\108.1.46.144")
    driver = webdriver.Chrome(service=path,options=options)
    driver.get(url)
    # find the search bar using selenium find_element function
    driver.find_element(By.NAME,"search_query").send_keys(searchtext)
    # clicking on the search button
    driver.find_element(By.CSS_SELECTOR,"#search-icon-legacy.ytd-searchbox").click()
    # For finding the right match search
    a=WebDriverWait(driver, 10)
    '''code=expected_conditions.title_contains(searchtext)
    a.until(code)
    code.click()'''
    
    # clicking on the match search having same as in searched query
    codepress=a.until(expected_conditions.element_to_be_clickable((By.ID,'inline-preview-player')))
    codepress.click()
    time.sleep(10)
	# while(True):
	#	 passḥ
speak = sr.Recognizer()
try:
	with sr.Microphone() as mic:
	
		# adjust the energy threshold based on
		# the surrounding noise level
		speak.adjust_for_ambient_noise(mic, duration=0.5)
		print("listening...")
		
		# listens for the user's input
		searchquery = speak.listen(mic)
		
		# Using google to recognize audio
		MyText = speak.recognize_google(searchquery)
		MyText = MyText.lower()
        
except sr.RequestError as e:
	print("Could not request results; {0}".format(e))

except sr.UnknownValueError:
	print("unknown error occurred")

# Calling the function
automateYoutube(MyText)

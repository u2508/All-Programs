from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
# Taking input from user
search_string = input("Input the URL or string you want to search for:")

# This is done to structure the string
# into search url.(This can be ignored)
search_string = search_string.replace(' ', '+')

# Assigning the browser variable with chromedriver of Chrome.
# Any other browser and its respective webdriver
# like geckodriver for Mozilla Firefox can be used
options = Options()
options.add_argument("--incognito")
options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
driver_path = Service("C:\Program Files\BraveSoftware\Brave-Browser\Application\108.1.46.144")
drvr = webdriver.Chrome(options = options, service= driver_path)

drvr.get("https://www.google.com/search?q=" +
									search_string + "&start=0")
drvr.get("https://www.youtube.com/watch?v=MjdpR-TY6QU")
time.sleep(10)

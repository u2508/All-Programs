from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument('--log-level=3')
options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
path=Service("C:\Program Files\BraveSoftware\Brave-Browser\Application\108.1.46.144")
driver = webdriver.Chrome(service=path,options=options)
# Open 200 tabs
for i in range(200):
    driver.get('https://www.google.com')
    
# Wait for 10 seconds
time.sleep(10)

# Close all tabs and quit the browser
driver.quit()

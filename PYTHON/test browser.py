# Import the required modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Main Function
if __name__ == '__main__':

	# Provide the email and password
	email = 'utkarshgupta64825@gmail.com'
	password = '123456'

	options = webdriver.ChromeOptions()
	options.add_argument("--start-maximized")
	options.add_argument('--log-level=3')
	options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
	path=Service("C:\Program Files\BraveSoftware\Brave-Browser\Application\108.1.46.144")
	driver = webdriver.Chrome(service=path,options=options)
	#driver.set_window_size(1920,1080)

	# Send a get request to the url
	driver.get('https://demo.applitools.com/')
	time.sleep(5)

	# Finds the input box by name in DOM tree to send both
	# the provided email and password in it.
	a=driver.find_element("id",'username')
	a.send_keys(email)
	time.sleep(2)
	a.submit()
	# Find the signin button and click on it.
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.button#PersonalDetailsButton[data-controltovalidate='PersonalDetails']"))).click()
	'''driver.find_element(By.CSS_SELECTOR,
		'button.btn.btn-green.signin-button').click()'''
	time.sleep(5)
	# Returns the list of elements
	# having the following css selector.
	container = driver.find_element(By.CSS_SELECTOR,
		'div.mdl-cell.mdl-cell--9-col.mdl-cell--12-col-phone.textBold')
	
	# Extracts the text from name,
	# institution, email_id css selector.
	name = container[0].text
	try:
		institution = container[1].find_element(By.CSS_SELECTOR,'a').text
	except:
		institution = container[1].text
	email_id = container[2].text

	# Output Example 1
	print("Basic Info")
	print({"Name": name,
		"Institution": institution,
		"Email ID": email})

	# Clicks on Practice Tab
	driver.find_element(By.CSS_SELECTOR,
	'a.mdl-navigation__link')[1].click()
	time.sleep(5)

	# Selected the Container containing information
	container = driver.find_element_by_css_selector(
	'div.mdl-cell.mdl-cell--7-col.mdl-cell--12-col-phone.\
	whiteBgColor.mdl-shadow--2dp.userMainDiv')
	
	# Selected the tags from the container
	grids = container.find_elements_by_css_selector(
	'div.mdl-grid')
	
	# Iterate each tag and append the text extracted from it.
	res = set()
	for grid in grids:
		res.add(grid.text.replace('\n',':'))

	# Output Example 2
	print("Practice Info")
	print(res)

	# Quits the driver
	driver.close()
	driver.quit()

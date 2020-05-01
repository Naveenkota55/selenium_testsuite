from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Safari()
driver.get('https://phptravels.org/clientarea.php')
usr_name=driver.find_element_by_name('username')
print(usr_name.is_displayed())
usr_name.send_keys('hi')
time.sleep(2)
driver.close()
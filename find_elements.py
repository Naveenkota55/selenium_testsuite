#trying to find elements in webpages can be helpful incase if we want to see totel number of common elements

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

driver=webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
driver.maximize_window()
driver.get("http://demo.guru99.com/test/login.html")

input_boxes=driver.find_elements(By.CLASS_NAME,"is_required validate account_input form-control")
print (len(input_boxes))

driver.quit()
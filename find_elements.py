#trying to find elements in webpages can be helpful incase if we want to see totel number of common elements

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

driver=webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
driver.maximize_window()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
#using class as commomn attribute
input_boxes=driver.find_elements(By.CLASS_NAME,"text_field")
print(len(input_boxes))  #to find number of input boxes
driver.quit()
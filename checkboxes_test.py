#just made modifications from find_elements.py
#changes are  >Added  is_selected 

from selenium import webdriver  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import time

driver=webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
driver.maximize_window()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
status=driver.find_element(By.ID,"RESULT_RadioButton-7_0").is_selected()

if status==False:
    driver.find_element(By.ID,"RESULT_RadioButton-7_0").click()
else:
    pass

driver.quit()




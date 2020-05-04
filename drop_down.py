# working with dropdown
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
driver=webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
driver.maximize_window()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
element=driver.find_element(By.ID,"RESULT_RadioButton-9")
drp=Select(element)

#drp.select_by_visible_text("Morning")

#drp.select_by_index(1)

drp.select_by_value("Radio-1")
time.sleep(2)
driver.quit()
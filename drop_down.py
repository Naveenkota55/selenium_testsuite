# working with dropdown
#options test
#all the imported modules are not used*just imported for practise
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
driver=webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
driver.maximize_window()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
element=driver.find_element(By.ID,"RESULT_RadioButton-9")
drp=Select(element)
# dropdown menus can be selected by 3 option values, visiable_text,Values


#drp.select_by_visible_text("Morning")
#drp.select_by_index(1)
drp.select_by_value("Radio-1")
#to find how many options are availble
print(len(drp.options))
#to print all the options
for texts in drp.options:
    print(texts.text)
time.sleep(2)
driver.quit()

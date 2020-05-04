#this script contains importing modules requirerd for keys , by ,select, expected conditions

#importing modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import time

#using firefox module
driver=webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
driver.maximize_window()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")  #get webpage

total_txt_field=driver.find_elements(By.CLASS_NAME,"text_field")     #for text field
print("total_text_fields_in_webpages=",len(total_txt_field))

total_links=driver.find_elements(By.TAG_NAME,"a")               #for links with anchor
print("totel links present in webpage:",len(total_links))

element_1=driver.find_elements(By.ID,"RESULT_RadioButton-9")            #for dropdown
element=driver.find_element(By.ID,"RESULT_RadioButton-9")
drp=Select(element)
drp_options=drp.options
print ("totel number of dropdowns:",len(element_1))
print("options available in dropdown::",len(drp_options))           #to view dropdown options

status=driver.find_element(By.ID,"RESULT_RadioButton-7_0").is_selected()    #to check status of checkboxes and radios
status_1=driver.find_element(By.ID,"RESULT_CheckBox-8_1").is_selected()


driver.find_element(By.ID,"RESULT_TextField-1").send_keys("Naveen")         #enter values
driver.find_element(By.ID,"RESULT_TextField-2").send_keys("kota")
driver.find_element(By.ID,"RESULT_TextField-3").send_keys("9012222222")
driver.find_element(By.ID,"RESULT_TextField-4").send_keys("Canada")
driver.find_element(By.ID,"RESULT_TextField-5").send_keys("Halifax")
driver.find_element(By.ID,"RESULT_TextField-6").send_keys("@dal.ca")

if status==False & status_1==False:                                 #to change only certain conditions meet
    driver.find_element(By.ID,"RESULT_CheckBox-8_1").click()
    driver.find_element(By.ID,"RESULT_RadioButton-7_0").click()

for option in drp_options:                                  #to view options in drop down in text
    print(option.text)

drp.select_by_visible_text("Morning")                       #to select option
driver.find_element(By.PARTIAL_LINK_TEXT,"Software").click()       #to click the link by partial text
time.sleep(3)                                   #wait before quit
driver.quit()                                   #to close firefox automation driver
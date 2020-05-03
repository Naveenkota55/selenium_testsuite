#explicit wait 2 practice
#working test_1
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
driver=webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
driver.maximize_window()
#get web page
driver.get("https://www.amazon.ca")
#implicit wait
driver.implicitly_wait(5)
#actions on search bar
search_bar=driver.find_element(By.ID,"twotabsearchtextbox")
search_bar.click()
search_bar.clear()
search_bar.send_keys("books")
search_bar.send_keys(Keys.ENTER)
#implimenting wait
wait=WebDriverWait(driver,10)
element=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='p_85/5690392011']/span/a/div/label/i")))
element.click()
time.sleep(2)
driver.quit()'''

from selemnium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.support import expected_conditions as EC
from selenium.common.support.ui import WebDriverWait
import time

#automation through firefox
driver=webdriver.Firefox(executable_path='/usr/local/bin/geakodriver')
#get website in this case amazon


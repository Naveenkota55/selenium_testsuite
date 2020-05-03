#explicit wait 2

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
driver=webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
driver.maximize_window()

driver.get("https://www.amazon.ca")
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
driver.quit()
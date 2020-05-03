#explicit wait 2 practice
#working test_1
#second test msy not work everytime cause amazon seems to update the webpage every time with new suggestion but first will work cause i am using search bar id
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

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

#automation through firefox
driver=webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
#get website in this case amazon
driver.get("https://www.amazon.ca")
#selection of electronic store just to load other page
driver.find_element(By.CSS_SELECTOR,"#nav-xshop > a:nth-child(4)")
#selection of wearable electonics
#implimenting explict wait with expected conditions

wait=WebDriverWait(driver,10)
element=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='leftNav']/ul[1]/ul/div/li[15]/span/a/span")))
element.click()

#explicit wait by time module
time.sleep(5)
#closing browser
driver.close()



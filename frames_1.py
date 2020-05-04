 #swithces between frames

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")

driver.get("https://www.selenium.dev/selenium/docs/api/java/")  #get website
driver.implicitly_wait(3)

driver.switch_to.frame("packageListFrame")  #switching to first_frame
driver.find_element_by_link_text("org.openqa.selenium").click() 

driver.switch_to.default_content()  #swiching to default frame

driver.switch_to.frame("packageFrame")   #swich to second frame
driver.find_element_by_link_text("Rotatable").click()

driver.switch_to.default_content()

time.sleep(3)
driver.switch_to.frame("classFrame")#switch to third frame
driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/ul[1]/li[5]/a").click()


time.sleep(2)
driver.close()
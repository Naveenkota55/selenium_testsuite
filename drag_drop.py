from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
driver.maximize_window()
driver.get("http://testautomationpractice.blogspot.com")
src_element=driver.find_element(By.XPATH,"//*[@id='draggable']")
dest_element=driver.find_element(By.XPATH,"//*[@id='droppable']")
actions=ActionChains(driver)
actions.drag_and_drop(src_element,dest_element).perform()
time.sleep(5)
driver.close()
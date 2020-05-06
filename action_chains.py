from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
driver.get("https://opensource-demo.orangehrmlive.com")
driver.find_element(By.ID,"txtUsername").send_keys("Admin")
driver.find_element(By.ID,"txtPassword").send_keys("admin123")
driver.find_element(By.ID,"btnLogin").click()

time.sleep(3)
driver.quit()
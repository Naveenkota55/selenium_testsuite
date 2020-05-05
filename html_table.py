from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")

driver.get("http://testautomationpractice.blogspot.com")

rows=len(driver.find_elements(By.XPATH,"//*[@id='HTML1']/div[1]/table/tbody/tr"))

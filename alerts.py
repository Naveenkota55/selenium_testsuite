from selenium import webdriver
import time

driver=webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")

driver.get("http://testautomationpractice.blogspot.com")

driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()
time.sleep(2)

driver.switch_to_alert().accept()
time.sleep(2)
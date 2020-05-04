#contains code to accept and dismiss the alert by using sithch to alert
from selenium import webdriver
import time

driver=webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")

driver.get("http://testautomationpractice.blogspot.com")

driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()
time.sleep(2)

#driver.switch_to_alert().accept()   #to accept
driver.switch_to_alert().dismiss()  #to dismiss
time.sleep(2)
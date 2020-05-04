from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
driver.maximize_window()
driver.get("http://testautomationpractice.blogspot.com")

print(driver.current_window_handle)
driver.find_element_by_xpath("//*[@id='Wikipedia1_wikipedia-search-form']/div/span[1]/a/img").click()
print(driver.window_handles)
time.sleep(3)
driver.quit()
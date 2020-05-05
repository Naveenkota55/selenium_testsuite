#this script contains the window handles, switching between them and also closing
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
driver.maximize_window()
driver.get("http://testautomationpractice.blogspot.com")

print(driver.current_window_handle)
driver.find_element_by_xpath("//*[@id='Wikipedia1_wikipedia-search-form']/div/span[1]/a/img").click()
handles=driver.window_handles
print(handles)

'''driver.switch_to.window(handles[1])  #switching the window
print(driver.current_window_handle)
print(driver.title)'''

for handle in handles:                  #to get all the windows handles , title,and also switching
    driver.switch_to.window(handle)
    print (handle)
    print(driver.title)
    if driver.title=='Automation Testing Practice':
        driver.close()      #closing specific window


time.sleep(3)
driver.quit()
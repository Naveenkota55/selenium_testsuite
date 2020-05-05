from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")

driver.get("http://testautomationpractice.blogspot.com")

rows=len(driver.find_elements(By.XPATH,"//*[@id='HTML1']/div[1]/table/tbody/tr"))
print("number of rows in table =",rows)

coloums=len(driver.find_elements(By.XPATH,"//*[@id='HTML1']/div[1]/table/tbody/tr[1]/th"))
print("number of rows in table =",coloums)

for r in range(1,rows+1):
    for c in range(1,coloums+1):
        key=driver.find_element(By.XPATH,"//*[@id='HTML1']/div[1]/table/tbody/tr["+str(r)+"]/th["+str(c)+"]").text
        print(key)
driver.quit()
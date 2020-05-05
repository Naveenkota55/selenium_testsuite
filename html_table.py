#this script contains how to read table contents, find rows &coloums

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")

driver.get("http://testautomationpractice.blogspot.com")

rows=len(driver.find_elements(By.XPATH,"//*[@id='HTML1']/div[1]/table/tbody/tr"))#to find number of rows
print("number of rows in table =",rows)

coloums=len(driver.find_elements(By.XPATH,"//*[@id='HTML1']/div[1]/table/tbody/tr[1]/th"))#to find number of columns
print("number of rows in table =",coloums)

for r in range(2,rows+1):#to print the table for header we can just use regular print command, below code just retrives table contents
    for c in range(1,coloums+1):
        key=driver.find_element(By.XPATH,"//*[@id='HTML1']/div[1]/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(key,end="      ")
    print()
driver.quit()

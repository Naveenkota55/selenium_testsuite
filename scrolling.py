from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.execute_script("window.scrollBy(0,1000)","")
flag=driver.find_element(By.XPATH,"//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[35]/td[1]/img")
driver.execute_script("arguments[0].scrollIntoView();",flag)
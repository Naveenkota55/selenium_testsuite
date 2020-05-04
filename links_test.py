#working on links

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")

driver.get("https://www.edureka.co/blog/keyboard-mouse-events-actions-class")
all_links=driver.find_elements(By.TAG_NAME,"a")
#to get totel number of links
print(len(all_links))

#to print links in text
for links in all_links:
    print (links.text)

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
driver.maximize_window()
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

driver.execute_script("window.scrollBy(0,1000)","")

driver.quit()
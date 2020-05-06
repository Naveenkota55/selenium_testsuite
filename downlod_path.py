from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromeoptions=Options()
chromeoptions.add_experimental_option("prefs",{"download.default_directory":"/usr/local/bin/"})

driver=webdriver.Chrome(executable_path="/usr/local/bin/chromedriver",chrome_options=chromeoptions)



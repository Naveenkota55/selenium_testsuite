#test the wait implicit

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
driver.get("https://edel.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX/my-profile/oMJK8Ea08Ix0fAl6IK8vZvnwaps_Q4tIimQQPQw1JIHtc6JioQSurgjJ9dTTgNfKD19GDOpzuIB9jM8nBL8kS0thpM6dE3D-9JORf6ZHM5bcIRKJlBe1B9_oUGc2wgx_sU_XAR1NTgwzeA2HHO5nqHBmchw2EdP7")

#implict wait for 5 sec
driver.implicitly_wait(10)

time.sleep(2)
driver.quit()
'''from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Safari()
driver.get('https://phptravels.org/clientarea.php')
usr_name=driver.find_element_by_name('username')
print(usr_name.is_displayed())
usr_name.send_keys('hi')
time.sleep(2)
driver.close()'''
#retesting the click option
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Safari()
driver.get('https://www.premiumexam.net/cybersecurity-essentials-1-1/cybersecurity-essentials-1-1-chapter-3-quiz-answers-100-2018/')
click_opt=driver.find_element_by_xpath('//*[@id="categories-2"]/ul/li[1]/a')
print(click_opt.is_displayed())
driver.maximize_window()
time.sleep(4)
click_opt.click()

time.sleep(2)
driver.quit()
'''
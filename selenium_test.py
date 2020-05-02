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
#automation of web
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')

driver.maximize_window()
driver.get('https://www.saucedemo.com')
driver.find_element_by_id('user-name').send_keys('standard_user')
driver.find_element_by_id('password').send_keys('secret_sauce')
driver.find_element_by_class_name('btn_action').click()
driver.find_element_by_xpath('//*[@id="inventory_container"]/div/div[1]/div[3]/button').click()
driver.find_element_by_css_selector('.svg-inline--fa > path:nth-child(1)').click()
'''driver.find_element_by_class_name('/html/body/div/div[2]/div[1]/div[2]/a/svg/path').click()'''
'''check weather item is added in cart
if check_item==True:
    driver.find_element_by_xpath('//*[@id="cart_contents_container"]/div/div[2]/a[2]').click()
'''
time.sleep(3)
driver.quit()

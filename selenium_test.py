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
#click cart button
driver.find_element_by_css_selector('.svg-inline--fa > path:nth-child(1)').click()
time.sleep(3)
#check weather the item is added to cart or not
check_item_add=driver.find_element_by_css_selector('button.btn_secondary').is_displayed()
if check_item_add==True:
    driver.find_element_by_css_selector('.btn_action').click()
    time.sleep(2)
    #entering details
    driver.find_element_by_id('first-name').send_keys('Naveen')
    driver.find_element_by_id('last-name').send_keys('kota')
    driver.find_element_by_id('postal-code').send_keys('B3j2k9')
    #click continue
    driver.find_element_by_css_selector('.btn_primary').click()
    time.sleep(2)
    #final confi
    driver.find_element_by_css_selector('.btn_action').click()
    #showing the order placed successfully
    if (driver.find_element_by_css_selector('html body.main-body div#page_wrapper.page_wrapper div#contents_wrapper div#checkout_complete_container.checkout_complete_container h2.complete-header').is_displayed())==True:
        print('order_placed successfully')
print('test_completed_successfully')
time.sleep(3)
driver.quit()

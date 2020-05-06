#performed action chain by mouse hover action
#seems like firefox and safari having issues to perform actionchain so opted for chrome
#contains mouse hover acttion

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
driver.maximize_window()

#following code for mouse hover actions
'''
driver.get("https://opensource-demo.orangehrmlive.com")
driver.find_element(By.ID,"txtUsername").send_keys("Admin")#enter login details and click login button
driver.find_element(By.ID,"txtPassword").send_keys("admin123")
driver.find_element(By.ID,"btnLogin").click()
admin=driver.find_element(By.XPATH,"//*[@id='menu_admin_viewAdminModule']/b")#storing the menu in variables
user_mag=driver.find_element(By.XPATH,"//*[@id='menu_admin_UserManagement']")
users=driver.find_element(By.XPATH,"//*[@id='menu_admin_viewSystemUsers']")
actions=ActionChains(driver)
actions.move_to_element(admin).move_to_element(user_mag).move_to_element(users).click().perform()#performing action chains *will not work unless there is perform() at the end
'''

#following code consists to double click
'''driver.get("http://testautomationpractice.blogspot.com")
element=driver.find_element(By.XPATH,"//*[@id='HTML10']/div[1]/button")
action=ActionChains(driver)
action.double_click(element).perform()'''

#following script is for double click()
driver.get("http://demo.guru99.com/test/simple_context_menu.html")
element=driver.find_element(By.XPATH,"//*[@id='authentication']/span")
actions=ActionChains(driver)
actions.context_click(element).perform()
time.sleep(5)
driver.quit()
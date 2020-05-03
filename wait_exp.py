#explict_wait

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
driver=webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')

driver.get("https://expedia.com/")
driver.maximize_window()
driver.implicitly_wait(4)

driver.find_element(By.XPATH,"//*[@id='tab-flight-tab-hp']").click()
driver.find_element(By.XPATH,"//*[@id='flight-type-one-way-label-hp-flight']").click()
driver.find_element(By.ID,"flight-origin-hp-flight").send_keys("YHZ")
driver.find_element(By.ID,'flight-destination-hp-flight').send_keys('HYD')

driver.find_element(By.ID,"flight-departing-single-hp-flight").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/meso-native-marquee/section/div/div/div[1]/section/div/div[2]/div[2]/section[1]/form/fieldset[2]/div/div[1]/div/div/div[2]/div[2]/table/tbody/tr[3]/td[5]/button").click()

driver.find_element(By.XPATH,'/html/body/meso-native-marquee/section/div/div/div[1]/section/div/div[2]/div[2]/section[1]/form/div[8]/label/button').click()

#explict wait line
wait=WebDriverWait(driver,10)
wait.until(EC.element_to_be_clickable.By.XPATH("//*[@id='tab-flight-tab-hp']"))


time.sleep(3)
driver.quit()
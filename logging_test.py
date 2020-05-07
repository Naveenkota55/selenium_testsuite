#following script to enable logging
from selenium import webdriver
import logging              #module for logging

logging.basicConfig(filename="/Users/naveenkota/Documents/selenium/logtest.log",
level=logging.DEBUG)                        #set location and level of log 
logging.debug("this is debug message")
logging.info("this is info")
logging.warning("this is warning")
logging.error("this is error message")
logging.critical("this is critical")
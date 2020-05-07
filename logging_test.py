from selenium import webdriver
import logging

logging.basicConfig(filename="/Users/naveenkota/Documents/selenium/logtest.log",
level=logging.debug)
logging.debug("this is debug message")
logging.info("this is info")
logging.warning("this is warning")
logging.error("this is error message")
logging.critical("this is critical")
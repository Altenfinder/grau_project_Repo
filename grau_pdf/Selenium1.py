from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import sys





driver = webdriver.Firefox(executable_path="/home/felipe/geckodriver")
print "After opening driver"
driver.get("http://www.facebook.com")
print "After get url"
#driver.quit()

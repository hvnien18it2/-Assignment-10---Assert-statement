from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver_path="C:\Selenium\chromedriver.exe"
driver=webdriver.Chrome(driver_path)

driver.get(" http://practice.automationtesting.in/")
title = "Automation Practice Site"
try:
    assert title in driver.title
    print("Pass")
except Exception as e:
    print("Failed",format(e))

time.sleep(2)



driver.close()
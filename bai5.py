from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver_path="C:\Selenium\chromedriver.exe"
driver=webdriver.Chrome(driver_path)

driver.get(" http://practice.automationtesting.in/")




time.sleep(2)
driver.set_window_size(600, 320)

time.sleep(2)

print(driver.current_url)

try:
    assert "600" in driver.get_window_size().get('width').__str__()
    assert "320" in driver.get_window_size().get('height').__str__()
    assert "http://practice.automationtesting.in/" in driver.current_url
    print("Pass")
except Exception as e:
    print("Failed",format(e))


time.sleep(2)

driver.close()
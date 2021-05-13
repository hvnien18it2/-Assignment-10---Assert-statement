from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver_path="C:\Selenium\chromedriver.exe"
driver=webdriver.Chrome(driver_path)

driver.get(" http://practice.automationtesting.in/")




driver.set_window_size(480, 320)

we = driver.get_window_size().get('width')
he = driver.get_window_size().get('height')
print(we,he)

time.sleep(2)

try:
    assert "480" in driver.get_window_size().get('width').__str__()
    assert "320" in driver.get_window_size().get('height').__str__()
    print("Pass")
except Exception as e:
    print("Failed",format(e))



time.sleep(2)
driver.close()
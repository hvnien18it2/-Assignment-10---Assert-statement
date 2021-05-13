from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver_path="C:\Selenium\chromedriver.exe"
driver=webdriver.Chrome(driver_path)

driver.get(" http://practice.automationtesting.in/")


time.sleep(2)

we1= driver.get_window_size().get('width')
he1 = driver.get_window_size().get('height')
print(we1,he1)


driver.maximize_window()

we = driver.get_window_size().get('width')
he = driver.get_window_size().get('height')
print(we,he)

try:
    assert "1314" in driver.get_window_size().get('width').__str__()
    assert "784" in driver.get_window_size().get('height').__str__()
    print("Pass")
except Exception as e:
    print("Failed",format(e))


time.sleep(2)
driver.close()
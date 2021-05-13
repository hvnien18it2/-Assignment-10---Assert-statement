from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

driver_path="C:\Selenium\chromedriver.exe"
driver=webdriver.Chrome(driver_path)

driver.get("https://itmscoaching.herokuapp.com/form")




time.sleep(2)


firstname=driver.find_element_by_id("first-name")
firstname.send_keys("Binh")

time.sleep(2)

lastname=driver.find_element_by_id("last-name")
lastname.send_keys("Nguyen")

time.sleep(2)

job=driver.find_element_by_id("job-title")
job.send_keys("Tester")

time.sleep(2)

education=driver.find_element_by_id("radio-button-3")
education.click()

time.sleep(2)


sex=driver.find_element_by_id("checkbox-2")
sex.click()

time.sleep(2)


select = Select(driver.find_element_by_id('select-menu'))
selected_option = select.select_by_index(3)
time.sleep(2)


date_click=driver.find_element_by_id("datepicker")
date_click.click()
time.sleep(2)

date_choose=driver.find_element_by_css_selector("body > div.datepicker.datepicker-dropdown.dropdown-menu.datepicker-orient-left.datepicker-orient-top > div.datepicker-days > table > tbody > tr:nth-child(3) > td:nth-child(3)")
date_choose.click()
time.sleep(2)

click=driver.find_element_by_css_selector("body > div.container > form > div > div:nth-child(15) > a")
click.click()

time.sleep(2)
try:
    assert "The form was successfully submitted!" in driver.page_source
    print("Pass click on Submit")
except Exception as e:
    print("Failed click on Submit", format(e))


driver.close()
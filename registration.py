from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support.ui import Select

driver= webdriver.Chrome('E:\\chromedriver.exe')
name = "tarun"
pwd = "teacher"
adrs = "Spring Acres"
city = "Omaha"
state = "NE"
zipc = "68124"
email = "tbattula@unomaha.edu"
phone = "402123456"
role = "student"
driver.get("http://omschool.herokuapp.com/register")
elem = driver.find_element_by_id("id_name")
elem.send_keys(name)
elem = driver.find_element_by_id("id_password")
elem.send_keys(pwd)
elem = driver.find_element_by_id("id_address")
elem.send_keys(adrs)
elem = driver.find_element_by_id("id_city")
elem.send_keys(city)
elem = driver.find_element_by_id("id_state")
elem.send_keys(state)
elem = driver.find_element_by_id("id_zipcode")
elem.send_keys(zipc)
elem = driver.find_element_by_id("id_email")
elem.send_keys(email)      
elem = driver.find_element_by_id("id_cell_phone")
elem.send_keys(phone)
select = Select(driver.find_element_by_id('id_role'))
select.select_by_value('Teacher')
btn=driver.find_element_by_css_selector('button.save.btn.btn-default')
btn.click()
time.sleep(5)
driver.close()
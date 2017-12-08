from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
user = "instructor"
pwd = "instructor1a"
driver= webdriver.Chrome('E:\\chromedriver.exe')
driver.get("http://omschool.herokuapp.com/admin/")
time.sleep(2)
elem = driver.find_element_by_id("id_username")
elem.send_keys(user)
elem = driver.find_element_by_id("id_password")
elem.send_keys(pwd)
logi=driver.find_element_by_xpath("//input[@value='Log in']")
logi.click()
time.sleep(5)
assert "Admin Logged In"
driver.close()
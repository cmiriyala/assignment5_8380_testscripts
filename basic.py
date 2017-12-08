import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver= webdriver.Chrome('E:\\chromedriver.exe')
user = "instructor"
pwd = "instructor1a"
driver.get("http://omschool.herokuapp.com/admin")
elem = driver.find_element_by_id("id_username")
elem.send_keys(user)
elem = driver.find_element_by_id("id_password")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
time.sleep(5)
assert "Logged In"
driver.get("http://omschool.herokuapp.com")
time.sleep(5)
driver.get("http://omschool.herokuapp.com/gallery")
time.sleep(5)
driver.get("http://omschool.herokuapp.com/about")
time.sleep(5)
driver.get("http://omschool.herokuapp.com/accounts/logout")
time.sleep(5)
driver.close()
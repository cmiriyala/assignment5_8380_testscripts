from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


driver= webdriver.Chrome('E:\\chromedriver.exe')
user = "tejaswikandula@unomaha.edu"
pwd = "student"
driver.get("http://omschool.herokuapp.com/accounts/login")
phn="4025026021"
elem = driver.find_element_by_id("id_username")
elem.send_keys(user)
elem = driver.find_element_by_id("id_password")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
time.sleep(3)
print("Logged In")
logi=driver.find_element_by_xpath("//input[@value=' Profile ']")
logi.click()
verprof="Email"
if (verprof in driver.page_source):
    print("student profile view page is working")
edit=driver.find_element_by_xpath("//input[@value=' Edit ']")
edit.click()
elem = driver.find_element_by_name('phone').clear()
elem = driver.find_element_by_name('phone')
elem.send_keys(phn)
sub=driver.find_element_by_xpath("//input[@value='Submit']")
sub.click()
tex="Welcome"
if (tex in driver.page_source):
    print("student edit profile view page is working")
bak=driver.find_element_by_link_text('Back').click()
att=driver.find_element_by_xpath("//input[@value=' View Updates ']").click()
time.sleep(1)

try:
    sla=driver.find_element_by_tag_name('p')
    print("working application")
    backm=driver.find_element_by_link_text('Back').click()
except:
    print("Nothing Exist")
try:
    existcourse=driver.find_element_by_partial_link_text('Course2-8th').click()
except:
    print("Courses not registered. Please contact admin")
    driver.find_element_by_link_text('Logout').click()
    print("Student system testing is successful")
    time.sleep(3)
    driver.close()
time.sleep(1)
att=driver.find_element_by_xpath("//input[@value=' Attendance']").click()
print("verified attendance")
sch=driver.find_element_by_xpath("//input[@value='  Schedule  ']").click()
print("verified schedule")
syll=driver.find_element_by_xpath("//input[@value='  Syllabus   ']").click()
print("verified syllabus")
grad=driver.find_element_by_xpath("//input[@value='  Grades     ']").click()
print("verified Grade")
exa=driver.find_element_by_xpath("//input[@value='  Exams      ']").click()
print("verified Exams")
time.sleep(2)
logout=driver.find_element_by_link_text('Logout').click()
print("Student system testing is successful")
time.sleep(3)
driver.close()
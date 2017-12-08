from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from builtins import print


driver= webdriver.Chrome('E:\\chromedriver.exe')
user = "kmangugari@unomaha.edu"
pwd = "teacher"
driver.get("http://omschool.herokuapp.com/accounts/login")
elem = driver.find_element_by_id("id_username")
elem.send_keys(user)
elem = driver.find_element_by_id("id_password")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
time.sleep(5)
print("Logged In")
logi=driver.find_element_by_xpath("//input[@value=' Profile ']")
logi.click()
edit=driver.find_element_by_xpath("//input[@value=' Edit ']")
edit.click()
phone="4344535678"
elem = driver.find_element_by_name('phone').clear()
elem = driver.find_element_by_name('phone')
elem.send_keys(phone)
sub=driver.find_element_by_xpath("//input[@value='Submit']")
sub.click()
time.sleep(1)
bk=driver.find_element_by_link_text('Back').click()
chtest=driver.find_element_by_xpath("//input[@value=' Post Updates ']").click()
elem = driver.find_element_by_name('postupdate').clear()
elem = driver.find_element_by_name('postupdate')
elem.send_keys('This is a testing update for automated testing')
posttext=driver.find_element_by_xpath("//input[@value='Post ']")
posttext.click()
time.sleep(1)
driver.get("http://omschool.herokuapp.com/teacher/home")
time.sleep(1)
try:
    coursestatus=driver.find_element_by_partial_link_text('Course2-9t')
    if coursestatus.is_displayed():
        print("course exist")
        coursestatus.click()
        posttext=driver.find_element_by_xpath("//input[@value='        View Schedule        ']")
        posttext.click()
        time.sleep(2)
        bk=driver.find_element_by_link_text('Back').click()
        posttext=driver.find_element_by_xpath("//input[@value='          View Syllabus           ']")
        posttext.click()
        time.sleep(2)
        bk=driver.find_element_by_link_text('Back').click()
        posttext=driver.find_element_by_xpath("//input[@value='   Make Announcement       ']")
        posttext.click()
        eleminput = driver.find_element_by_name('mailtext').clear()
        eleminput = driver.find_element_by_name('mailtext')
        eleminput.send_keys('This is a mail send test for automated testing')
        posttext=driver.find_element_by_css_selector('button.btn.btn-primary.btn-lg.btn-block')
        posttext.click()
        coursestatus=driver.find_element_by_partial_link_text('Course2-9t')
        coursestatus.click()
        posttext=driver.find_element_by_xpath("//input[@value='   Update Attendance       ']")
        posttext.click()
        posttext=driver.find_element_by_xpath("//input[@value='Go']")
        posttext.click()
        try:
            attendstatus=driver.find_element_by_xpath("//input[@value='Absent']")
            if attendstatus.is_displayed():
                attendstatus.click()
                bk=driver.find_element_by_link_text('Back').click()
        except:
            markstatus=driver.find_element_by_xpath("//input[@value='Present']")
            markstatus.click()
            bk=driver.find_element_by_link_text('Back').click()
            logout=driver.find_element_by_link_text('Logout').click()
            print("Teacher system testing is successful")
except:
    print("there are no courses available")
    logout=driver.find_element_by_link_text('Logout').click()
    print("Teacher system testing is successful")
logout=driver.find_element_by_link_text('Logout').click()
print("Teacher system testing is successful")


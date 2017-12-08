from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from builtins import print

driver= webdriver.Chrome('E:\\chromedriver.exe')
user = "pmadiraju@unomaha.edu"
pwd = "parent"
zipc = "68124"
driver.get("http://omschool.herokuapp.com/accounts/login")
elem = driver.find_element_by_id("id_username")
elem.send_keys(user)
elem = driver.find_element_by_id("id_password")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
time.sleep(3)
print("Logged In")
logi=driver.find_element_by_xpath("//input[@value=' Profile ']")
logi.click()
edit=driver.find_element_by_xpath("//input[@value=' Edit ']")
edit.click()
elem = driver.find_element_by_name('zipcode').clear()
elem = driver.find_element_by_name('zipcode')
elem.send_keys(zipc)
sub=driver.find_element_by_xpath("//input[@value='Submit']")
sub.click()
time.sleep(1)
bk=driver.find_element_by_link_text('Back').click()
phver=driver.find_element_by_name('name').click()
text="Phone Number already Verified"
text1="verification code is"
if (text in driver.page_source):
    print("phone number already verified")
    bk=driver.find_element_by_link_text('Back').click()    
elif (text1 in driver.page_source):
    time.sleep(15)
    print("phone number not verified")
    hm=driver.find_element_by_css_selector('a.nav-link').click()
try:
    chtest=driver.find_element_by_xpath("//input[@value='Course Records']")
    if chtest.is_displayed():
        print("child linked")
        chtest.click()
        cour=driver.find_element_by_partial_link_text('Course2-8th').click()
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
        bak=driver.find_element_by_link_text('Back').click()
        exa=driver.find_element_by_xpath("//input[@value='       Invoice       ']").click()
        print("invoice")
        textin="Due date"
        if (textin in driver.page_source):
            print("invoice exist")
            pay1=driver.find_element_by_xpath("//input[@value='Pay Now']").click()
            py2=driver.find_element_by_name('submit').click()
            print("Payment is not tested with script")
            print("Parent system testing is completed")
            driver.close()
        else:
            print("invoice yet to be generated")
            backd=driver.find_element_by_link_text('Back').click()
            logout=driver.find_element_by_link_text('Logout').click()
except:
    print("Please request admin to link the child")
    print("Parent system testing is completed")
    logout=driver.find_element_by_link_text('Logout').click()
    driver.close()
    
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

usernameStr = 'chauvanabhi@gmail.com'
passwordStr = 'abhishek@123'

other_browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
other_browser.get(('https://www.naukri.com/nlogin/logout'))

user_naukri = other_browser.find_element_by_id('usernameField')
user_naukri.send_keys(usernameStr)

password_naukri = other_browser.find_element_by_id('passwordField')
password_naukri.send_keys(passwordStr)

naukri_signin = other_browser.find_element_by_class_name('waves-effect')
naukri_signin.click()


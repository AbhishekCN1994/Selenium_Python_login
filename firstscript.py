
'''from bs4 import BeautifulSoup
import requests
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import urllib.request'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

usernameStr = 'chauvanabhi@gmail.com'
passwordStr = 'abhishek@123'

#other_browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
other_browser = webdriver.Chrome(executable_path='C:/Users/Abhishekan/Downloads/chromedriver_win32/chromedriver')
other_browser.maximize_window()
other_browser.get(('https://www.linkedin.com/'))

user_linkedin = other_browser.find_element_by_id('login-email')
user_linkedin.send_keys(usernameStr)

password_linkedin = other_browser.find_element_by_id('login-password')
password_linkedin.send_keys(passwordStr)

linkedin_signin = other_browser.find_element_by_id('login-submit')
linkedin_signin.click()

name = 'C,C++,Java,Bangalore,Karnataka'
linkedin_search = other_browser.find_element_by_tag_name('input')
linkedin_search.send_keys(name)

search_profile = other_browser.find_element_by_class_name('search-typeahead-v2__button')
search_profile.click()

other_browser.get('https://www.linkedin.com/search/results/all/?keywords='+name)

profile = other_browser.find_elements(By.CLASS_NAME,'search-result__result-link')
csvfile = open('profile_links.csv','w+',newline = '')
writer = csv.writer(csvfile)
writer.writerow(['Profile Links'])
for data in profile:
    link = data.get_attribute('href')
    print(link)
    writer.writerow([link])
csvfile.close()








import time
from selenium import webdriver
driver=webdriver.Chrome('/home/ankush/Desktop/python3_selenium/chromedriver')
driver.get('http://www.google.com/')
box=driver.find_element_by_name('q')
box.send_keys('iiit hyderabad')
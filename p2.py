import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome('/home/ankush/Desktop/python3_selenium/chromedriver')
driver.get('http://web.whatsapp.com/');
a = input("Press Enter to continue")
name = driver.find_element_by_css_selector('.2zCFw.copyable-text.selectable-text')
name.send_keys('Remaindes')
name.send_keys(Keys.ENTER)
time.sleep(2)

for i in range (0,5):
    msg=driver.find_element_by_css_selector('._3u228.copyable.text selectable.text')
    msg.send_keys('I am a bot'+str(i))
    msg.send_keys(Keys.ENTER)
    time.sleep(2)
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
chrome_options = webdriver.ChromeOptions()
browser = webdriver.Chrome('chromedriver.exe',options=chrome_options)
base_url = 'http://www.facebook.com'
browser.get(base_url)
username = browser.find_element_by_id("email")
password = browser.find_element_by_id("pass")
submit   = browser.find_element_by_id("loginbutton")
username.send_keys("Your Email ID")
password.send_keys("Your Password")
submit.click()


body = browser.find_element_by_tag_name('body')
        
for _ in range(20):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.3)

posts = browser.find_elements_by_css_selector('div[data-testid="post_message"]')

for post in posts:
    print(post.text)

from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_css_selector('[name="firstname"]')
input1.send_keys("Alex")

input2 = browser.find_element_by_css_selector('[name="lastname"]')
input2.send_keys("Semenov")

input3 = browser.find_element_by_css_selector('[name="email"]')
input3.send_keys("Alex@Semenov.com")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'les2_2_step7.txt')
element = browser.find_element_by_css_selector('#file[type="file"]')
element.send_keys(file_path)

button = browser.find_element_by_css_selector("button.btn")
button.click()
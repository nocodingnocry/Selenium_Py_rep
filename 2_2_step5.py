from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

x_value = browser.find_element_by_css_selector("#input_value")
x_value = x_value.text
x_value = calc(x_value)

browser.execute_script("window.scrollBy(0, 150);")

input1=browser.find_element_by_css_selector("#answer")
input1.send_keys(x_value)

option1 = browser.find_element_by_css_selector("#robotCheckbox")
option1.click()

option2 = browser.find_element_by_css_selector("#robotsRule")
option2.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_css_selector("button.btn")
button.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

value_x = browser.find_element_by_css_selector('#input_value')
value_x = value_x.text
x = calc(value_x)

input1=browser.find_element_by_css_selector("#answer") 
input1.send_keys(x)

button = browser.find_element_by_css_selector("button.btn")
button.click()
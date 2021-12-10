from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_css_selector("#treasure")

#found element 

x = x_element.get_attribute("valuex")

#used get_attribute

y = calc(x)

#calculated value

input1=browser.find_element_by_css_selector("#answer") 
input1.send_keys(y)
 
#writed value

option1 = browser.find_element_by_css_selector("#robotCheckbox")
option1.click()

#used checkbox

option2 = browser.find_element_by_css_selector("#robotsRule")
option2.click()

#used radiobutton

button = browser.find_element_by_css_selector("button.btn")
button.click()

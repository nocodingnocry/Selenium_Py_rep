from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

#num1

first_element = browser.find_element_by_css_selector("#num1")
first_element = first_element.text

#num2

second_element = browser.find_element_by_css_selector("#num2")
second_element = second_element.text

first_and_second = str(int(first_element) + int(second_element))


select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(first_and_second)

button = browser.find_element_by_css_selector("button.btn")
button.click()

#click button

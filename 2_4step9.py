from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()
browser.get(link)


WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

button = browser.find_element_by_css_selector("#book")
button.click()

browser.execute_script("window.scrollBy(0, 300);")

x_value = browser.find_element_by_css_selector("#input_value")
x_value = x_value.text
x_value = calc(x_value)

input1=browser.find_element_by_css_selector("#answer")
input1.send_keys(x_value)

button = browser.find_element_by_css_selector("#solve")
button.click()
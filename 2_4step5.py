from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

link = "http://suninjuly.github.io/cats.html"

browser = webdriver.Chrome()
browser.get(link)


button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price", "$95"))
    )
button.click()

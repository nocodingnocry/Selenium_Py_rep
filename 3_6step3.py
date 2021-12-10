from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
import pytest

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('number_of_page', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
#@pytest.mark.parametrize('number_of_page', ["236897", "236898"])
def test_see_right_answer(browser, number_of_page):
    link = f"https://stepik.org/lesson/{number_of_page}/step/1"
    browser.get(link)
    browser.implicitly_wait(10)
    input1 = browser.find_element_by_css_selector(".ember-text-area.ember-view")
    input1.send_keys(str(math.log(int(time.time())))) 
    
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))
    button.click()

    Correct1 = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint"))).text
    
    assert Correct1 == "Correct!", Correct1
    conftest.py

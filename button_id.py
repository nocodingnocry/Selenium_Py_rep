from selenium import webdriver
import time

#options = webdriver.ChromeOptions()
#options.add_experimental_option('excludeSwitches', ['enable-logging'])
#driver = webdriver.Chrome(options=options)

try:
    link = "http://suninjuly.github.io/simple_form_find_task.html"
    driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")  # <- Путь до файла хромдрайвера
    browser.get(link)


except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
    
finally:
    driver.close()
    time.sleep(2)
    driver.quit()


browser = webdriver.Chrome()
#browser.add_experimental_option('excludeSwitches', ['enable-logging'])
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
button = browser.find_element_by_id("submit_button")
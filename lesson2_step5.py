#неявное ожидание implicitly_wait  https://stepik.org/lesson/181384/step/5?unit=156009

from selenium import webdriver
try:
    browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/wait1.html")

    button = browser.find_element_by_id("verify")
    button.click()
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text

finally:
    browser.quit()
#устанавливаем явное ожидание пока цена не снизится до 100 https://stepik.org/lesson/181384/step/8?unit=156009
#
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд, пока цена за дом не станет равна 100
    button = WebDriverWait(browser, 12).until(
           EC.text_to_be_present_in_element((By.ID, "price"),"$100")
        )
#нажимаем кнопку Book
    button=browser.find_element_by_id("book").click()

#находим элемент, хранящий х. Вычисляем значение, сохраняем в переменную у
    x= int(browser.find_element_by_id("input_value").text)
    y = calc(x)

#выводим решение в текстовую строку
    browser.find_element_by_id("answer").send_keys(y)

#нажимаем кнопку Submit
    browser.find_element_by_id("solve").click()
    time.sleep(5)

#копируем результат для ДЗ из алерта в окно консоли
    print(browser.switch_to.alert.text)

finally:
    browser.quit()

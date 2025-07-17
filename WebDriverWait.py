# Основы явных ожиданий
# 	1.	Импорт необходимых модулей:

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 2.	Инициализация WebDriverWait:
# 	•	WebDriverWait(driver, timeout) создаёт объект ожидания с максимальным временем ожидания (timeout) в секундах.
# 	•	В сочетании с expected_conditions он проверяет выполнение условий через регулярные промежутки времени (по умолчанию каждые 0.5 секунды).
# 3.	Пример базового использования:

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "element_id"))
)
# В этом примере Selenium ждёт, пока на странице появится элемент с id="element_id". Если за 10 секунд элемент не появится, будет выброшено исключение TimeoutException.
#
# Часто используемые методы expected_conditions
#
# Вот список наиболее полезных условий из expected_conditions:
#
# 1. presence_of_element_located(locator)
# 	•	Проверяет наличие элемента в DOM (не обязательно видимого).
# 	•	Используется для элементов, которые могут загружаться асинхронно.

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".my-class"))
)

# 2. visibility_of_element_located(locator)
# 	•	Проверяет, что элемент есть в DOM и он видим (имеет ненулевые размеры и не скрыт).
# 	•	Используется для элементов, которые должны быть интерактивными.

element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@id='content']"))
)

# 3. element_to_be_clickable(locator)
# 	•	Проверяет, что элемент кликабельный (видим и активен).
# 	•	Полезно для кнопок или ссылок.

element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "submit"))
)

# 4. text_to_be_present_in_element(locator, text_)
# 	•	Ждёт, пока указанный текст появится внутри элемента.

WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "Welcome")
)

# 5. frame_to_be_available_and_switch_to_it(locator)
# 	•	Ждёт, пока iframe станет доступным, и переключается на него.

WebDriverWait(driver, 10).until(
    EC.frame_to_be_available_and_switch_to_it((By.ID, "frame_id"))
)

# 6. alert_is_present()
# 	•	Ждёт появления JavaScript-алерта.

alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
alert.accept()

# 7. staleness_of(element)
# 	•	Проверяет, что элемент устарел (удалён из DOM).

WebDriverWait(driver, 10).until(
    EC.staleness_of(driver.find_element(By.ID, "old_element"))
)

# 8. title_contains(text_)
# 	•	Проверяет, что заголовок страницы содержит указанный текст.

WebDriverWait(driver, 10).until(EC.title_contains("Dashboard"))

# Использование пользовательских условий
# Если встроенные условия не подходят, вы можете написать собственное условие:

from selenium.common.exceptions import TimeoutException

def custom_condition(driver):
    return "Success" in driver.page_source

try:
    WebDriverWait(driver, 10).until(custom_condition)
    print("Condition met!")
except TimeoutException:
    print("Condition not met within timeout.")

# Полный пример:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://example.com")

# Ждём появления элемента и взаимодействуем с ним
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "submit_button"))
)
element.click()

# Ждём, пока появится текст в заголовке
WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "Welcome")
)

driver.quit()

# Резюме:
# 	1.	Часто используемые методы:
# 	•	presence_of_element_located
# 	•	visibility_of_element_located
# 	•	element_to_be_clickable
# 	•	text_to_be_present_in_element
# 	•	frame_to_be_available_and_switch_to_it
# 	2.	Когда использовать WebDriverWait:
# 	•	Чтобы дождаться загрузки элементов на странице.
# 	•	Избежать проблем с time.sleep, который может замедлить тесты.
# 	3.	Преимущества WebDriverWait:
# 	•	Умный подход к ожиданию (проверяет через интервалы, вместо жёсткой задержки).
# 	•	Делает тесты более стабильными и надёжными.

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get('https://www.qa-practice.com/elements/new_tab/link')
driver.find_element(By.ID, 'new-page-link').click()
tabs = driver.window_handles # Сохраняем список вкладок
driver.switch_to.window(tabs[1]) # Переход на вкладку с индексом 1
result = driver.find_element(By.ID, 'result-text')
print(result.text)
driver.close() # Закрытие вкладки
driver.switch_to.window(tabs[0]) # Переход на вкладку с индексом 0, так как при закрытии вкладки, селениум не умеет автоматически переходить на предыдущую
new_button = driver.find_element(By.LINK_TEXT, 'New tab button')
print(new_button.get_attribute('href'))

driver.quit()

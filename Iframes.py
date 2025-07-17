from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get('https://www.qa-practice.com/elements/iframe/iframe_page')
iframe = driver.find_element(By.TAG_NAME, 'iframe')
driver.switch_to.frame(iframe) # Переходим для дальнейшей работы в iframe
button = driver.find_element(By.CLASS_NAME, 'btn-secondary')
print(button.text)
driver.switch_to.default_content() # Возвращаемся из iframe, чтобы продолжить работу на основной странице
tab = driver.find_element(By.LINK_TEXT, 'Iframe')
print(tab.get_attribute('href'))

driver.quit()
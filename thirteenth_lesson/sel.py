from selenium import webdriver
from selenium.webdriver.common.by import By
import time

wd = webdriver.Chrome()
wd.maximize_window()
wd.implicitly_wait(10)
name = 'qwerty'

wd.get('https://open-eshop.stqa.ru/oc-panel')

wd.find_element(By.CSS_SELECTOR, '#page [name="email"]').send_keys('demo@open-eshop.com')
wd.find_element(By.CSS_SELECTOR, '#page [name="password"]').send_keys('demo')
wd.find_element(By.CSS_SELECTOR, '#page div > button').click()

wd.find_element(By.CSS_SELECTOR, '[href="#collapseOne"]').click()
wd.find_element(By.CSS_SELECTOR, '[title="Coupons"]').click()
wd.find_element(By.CSS_SELECTOR, '#content > ul + a').click()

wd.find_element(By.CSS_SELECTOR, '#name').send_keys(name)
wd.find_element(By.CSS_SELECTOR, '[name="valid_date"]').click()
wd.find_elements(By.CSS_SELECTOR, '.datepicker.dropdown-menu .day')[9].click()
wd.find_element(By.CSS_SELECTOR, '#discount_amount').send_keys('12345')
wd.find_element(By.CSS_SELECTOR, '[name="submit"]').click()

wd.find_element(By.CSS_SELECTOR, '.form-control[name="name"]').send_keys(name)
wd.find_element(By.CSS_SELECTOR, '#content > form > button').click()
wd.find_element(By.CSS_SELECTOR, '[class="glyphicon glyphicon-trash"]').click()
wd.find_element(By.CSS_SELECTOR, '.sweet-alert.visible .confirm').click()
wd.find_element(By.CSS_SELECTOR, '.pull-right [data-toggle="dropdown"]').click()

wd.find_element(By.CSS_SELECTOR, '.dropdown-menu .glyphicon-off').click()

time.sleep(3)
wd.close()
from selenium.webdriver.common.by import By

def test_one(driver):
    driver.get('https://www.google.com/')
    seartch_field = driver.find_element(By.NAME, 'q')
    seartch_field.send_keys('cat')
    seartch_field.submit()

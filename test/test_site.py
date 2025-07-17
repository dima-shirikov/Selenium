from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
from Pages.homepages import HomePage
from Pages.product import ProductPage

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    driver.close()

def test_open_s6(driver):
    driver.get('https://demoblaze.com/index.html')
    galaxy_s6 = driver.find_element(By.XPATH, '//a[text()="Samsung galaxy s6"]')
    galaxy_s6.click()
    title = driver.find_element(By.CSS_SELECTOR, 'h2')
    assert title.text == 'Samsung galaxy s6'

    # homepages = HomePage(driver)
    # homepages.open()
    # homepages.click_galaxy_s6()
    # product_page = ProductPage(driver)
    # product_page.check_title_is('Samsung galaxy s6')

def test_monitors(driver):
    driver.get('https://demoblaze.com/index.html')
    monitors = driver.find_element(By.XPATH, '//a[text()="Monitors"]')
    monitors.click()
    time.sleep(2)
    count = driver.find_elements(By.CSS_SELECTOR, 'div.card')
    assert len(count) == 2

    # homepages = HomePage(driver)
    # homepages.open()
    # homepages.click_monitor()
    # time.sleep(2)
    # product_page = ProductPage(driver)
    # product_page.check_product_count(2)




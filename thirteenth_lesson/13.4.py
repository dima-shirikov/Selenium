from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get('https://litecart.stqa.ru/en/')

driver.find_element(By.CSS_SELECTOR, '#box-most-popular .campaign-price').click()
driver.find_element(By.CSS_SELECTOR, '[name="options[Size]"]').click()
driver.find_element(By.CSS_SELECTOR, '[value="Large"]').click()
driver.find_element(By.CSS_SELECTOR, '[name="add_cart_product"]').click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'a[class="content"][style=""]'))
).click()

# driver.find_element(By.CSS_SELECTOR, 'a[class="content"][style=""]').click()
driver.find_element(By.CSS_SELECTOR, '[value="Remove"]').click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#checkout-cart-wrapper p + p > a'))
).click()

# driver.find_element(By.CSS_SELECTOR, '#checkout-cart-wrapper p + p > a').click()
driver.close()




from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pytest
import time

class Helper:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def start_page(self):
        self.driver.get('http://litecart.stqa.ru/en/')

    def add_to_cart(self, number):
        self.driver.find_element(By.CSS_SELECTOR, '#box-most-popular .campaign-price').click()
        self.driver.find_element(By.CSS_SELECTOR, '[name="options[Size]"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '[value="Large"]').click()
        quantity = self.driver.find_element(By.CSS_SELECTOR, '[name = "quantity"]')
        quantity.clear()
        quantity.send_keys(number)
        self.driver.find_element(By.CSS_SELECTOR, '[name="add_cart_product"]').click()

    def check_add_to_cart(self):
        WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[class="content"][style=""]'))
        )
        return self.driver.find_element(By.CSS_SELECTOR, 'span.quantity')

    def cart_clear(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[class="content"][style=""]'))
        ).click()
        self.driver.find_element(By.CSS_SELECTOR, '[value="Remove"]').click()

    def back(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#checkout-cart-wrapper p + p > a'))
        ).click()

    def quit(self):
        self.driver.quit()

    def is_element_present(self, locator):
        try:
            self.driver.find_element(By.CSS_SELECTOR, locator)
            return True
        except NoSuchElementException:
            return False

    def is_not_element_present(self, locator):
        self.driver.implicitly_wait(0)
        try:
            self.driver.find_element(By.CSS_SELECTOR, locator)
            return False
        except NoSuchElementException:
            return True
        finally:
            self.driver.implicitly_wait(10)


fixture = None
@pytest.fixture(scope="session")
def app():
    global fixture
    if fixture is None:
        fixture = Helper()
        fixture.start_page()
    yield fixture
    fixture.quit()


@pytest.mark.parametrize('number', ['3', '7', '10'])
def test_duck(app, number):
    try:
        app.add_to_cart(number)
        assert number == app.check_add_to_cart().text
    finally:
        app.cart_clear()
        app.back()
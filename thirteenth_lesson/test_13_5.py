from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

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
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[class="content"][style=""]'))
        )
        return self.driver.find_element(By.CSS_SELECTOR, 'span.quantity')

    def cart_clear(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[class="content"][style=""]'))
        ).click()
        self.driver.find_element(By.CSS_SELECTOR, '[value="Remove"]').click()
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#checkout-cart-wrapper p + p > a'))
        ).click()

    def check_clear_cart(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'span.quantity')

    def quit(self):
        self.driver.quit()

@pytest.fixture(scope="session")
def app():
    fixture = Helper()
    fixture.start_page()
    yield fixture
    fixture.quit()

@pytest.mark.parametrize('number', ['3', '7', '10'])
def test_duck(app, number):
    try:
        app.add_to_cart(number)
        assert number == app.check_add_to_cart().text, f'Количество товара не соответствует {number}'
    finally:
        app.cart_clear()
        assert app.check_clear_cart().text == '0', f'Товары еще в корзине'

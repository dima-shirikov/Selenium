from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure_commons.types import AttachmentType
import allure

class Helper_allure:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def start_page(self):
        self.driver.get('http://litecart.stqa.ru/en/')

    def quantity_selection(self, number):
        self.driver.find_element(By.CSS_SELECTOR, '#box-most-popular .campaign-price').click()
        self.driver.find_element(By.CSS_SELECTOR, '[name="options[Size]"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '[value="Large"]').click()
        quantity = self.driver.find_element(By.CSS_SELECTOR, '[name = "quantity"]')
        quantity.clear()
        quantity.send_keys(number)

    def add_to_cart(self):
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

    def screen_shot(self, name):
        wait = WebDriverWait(self.driver, 5)
        wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)

    def screen_shot_add_to_cart(self, name):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[class="content"][style=""]'))
        )
        allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
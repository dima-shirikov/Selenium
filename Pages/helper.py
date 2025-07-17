from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import allure
from selenium.webdriver.support.wait import WebDriverWait
from allure_commons.types import AttachmentType

class Helper:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.maximize_window()
        self.wd.implicitly_wait(10)

    def login(self):
        self.wd.find_element(By.CSS_SELECTOR, '#page [name="email"]').send_keys('demo@open-eshop.com')
        self.wd.find_element(By.CSS_SELECTOR, '#page [name="password"]').send_keys('demo')
        self.wd.find_element(By.CSS_SELECTOR, '#page div > button').click()

    def create_coupon(self, name):
        if self.check_create_coupon_button_not_present():
            self.wd.find_element(By.CSS_SELECTOR, '[href="#collapseOne"]').click()
            self.wd.find_element(By.CSS_SELECTOR, '[title="Coupons"]').click()
        self.wd.find_element(By.CSS_SELECTOR, '#content > ul + a').click()
        self.wd.find_element(By.CSS_SELECTOR, '#name').send_keys(name)
        self.wd.find_element(By.CSS_SELECTOR, '[name="valid_date"]').click()
        self.wd.find_elements(By.CSS_SELECTOR, '.datepicker.dropdown-menu .day')[9].click()
        self.wd.find_element(By.CSS_SELECTOR, '#discount_amount').send_keys('12345')
        self.wd.find_element(By.CSS_SELECTOR, '[name="submit"]').click()

    def check_create_coupon_button_not_present(self):
        return self.is_not_element_present('#content > ul + a')

    def delete_coupon(self, name):
        self.wd.find_element(By.CSS_SELECTOR, '.form-control[name="name"]').send_keys(name)
        self.wd.find_element(By.CSS_SELECTOR, '#content > form > button').click()
        self.wd.find_element(By.CSS_SELECTOR, '[class="glyphicon glyphicon-trash"]').click()
        self.wd.find_element(By.CSS_SELECTOR, '.sweet-alert.visible .confirm').click()

    def logout(self):
        self.wd.find_element(By.CSS_SELECTOR, '.pull-right [data-toggle="dropdown"]').click()
        self.wd.find_element(By.CSS_SELECTOR, '.dropdown-menu .glyphicon-off').click()

    def open_start_page(self):
        # self.wd.delete_all_cookies()
        self.wd.get('https://open-eshop.stqa.ru/oc-panel')

    def quit(self):
        self.wd.quit()

    def is_logined(self):
        return self.is_element_present('.dropdown-menu .glyphglyphicon.glyphicon-off')

    def is_not_logined(self):
        return self.is_not_element_present('.dropdown-menu .glyphglyphicon.glyphicon-off')

    def is_element_present(self, locator):
        try:
            self.wd.find_element(By.CSS_SELECTOR, locator)
            return True
        except NoSuchElementException:
            return False

    def is_not_element_present(self, locator):
        self.wd.implicitly_wait(0)
        try:
            self.wd.find_element(By.CSS_SELECTOR, locator)
            return False
        except NoSuchElementException:
            return True
        finally:
            self.wd.implicitly_wait(10)

    def get_name_of_coupon_from_first_row(self):
        return self.wd.find_element(By.CSS_SELECTOR, '.table-striped td').text

    def check_that_coupon_deleted(self):
        return self.is_element_present('.table-striped tr[style="display: none;"]')

    def screen_shot(self, name):
        wait = WebDriverWait(self.wd, 5)
        wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        allure.attach(self.wd.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
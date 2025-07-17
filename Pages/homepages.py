from selenium.webdriver.common.by import By

class HomePage():
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://demoblaze.com/index.html')

    def click_galaxy_s6(self):
        galaxy_s6 = self.driver.find_element(By.XPATH, '//a[text()="Samsung galaxy s6"]')
        galaxy_s6.click()

    def click_monitor(self):
        monitors = self.driver.find_element(By.XPATH, '//a[text()="Monitors"]')
        monitors.click()
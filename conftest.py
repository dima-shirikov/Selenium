from selenium import webdriver
import pytest
from Pages.helper import Helper
from Pages.helper_allure import Helper_allure
# from selenium.webdriver.chrome.options import Options # Чтобы браузер не запускался визуально

@pytest.fixture()
def driver():
    # options = Options()         # Чтобы браузер не запускался визуально
    # options.add_argument('--headless')      # Чтобы браузер не запускался визуально
    driver = webdriver.Chrome()      # Чтобы браузер не запускался визуально нужно в скобки добавить (options=options)
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    driver.close()

fixture = None
@pytest.fixture(scope="session")
def app():
    global fixture
    if fixture is None:
        fixture = Helper()
    if fixture.is_not_logined():
        fixture.open_start_page()
        fixture.login()
    yield fixture
    if fixture is not None:
        if fixture.is_logined():
            fixture.logout()
        fixture.quit()

@pytest.fixture(scope="session")
def appli():
    fixture = Helper_allure()
    fixture.start_page()
    yield fixture
    fixture.quit()
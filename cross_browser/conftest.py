import pytest
from selenium import webdriver
from _pytest.fixtures import SubRequest

def pytest_addoption(parser):
    parser.addoption('--browser')

@pytest.fixture()
def driver(request: SubRequest):
    if request.config.getoption('--browser').lower() == 'safari':
        driver = webdriver.Safari()
    elif request.config.getoption('--browser').lower() == 'chrome':
        driver = webdriver.Chrome()
    yield driver
    driver.quit()
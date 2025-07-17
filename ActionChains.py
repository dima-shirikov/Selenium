from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver

def test_jackets(driver):
    driver.get('http://magento.softwaretestingboard.com/')
    womens = driver.find_element(By.ID, 'ui-id-4')
    tops = driver.find_element(By.ID, 'ui-id-9')
    jackets = driver.find_element(By.ID, 'ui-id-11')
    # ActionChains(driver).move_to_element(womens).move_to_element(tops).click(jackets).perform()
    action = ActionChains(driver)
    action.move_to_element(womens)
    action.move_to_element(tops)
    action.click(jackets)
    action.perform()
    driver.quit()

def test_d_n_d(driver):
    driver.get('https://www.qa-practice.com/elements/dragndrop/boxes')
    drag_me = driver.find_element(By.ID, 'rect-draggable')
    drop_here = driver.find_element(By.ID, 'rect-droppable')
    ActionChains(driver).drag_and_drop(drag_me, drop_here).perform()
    # actions = ActionChains(driver) # По шагам показывает как работает функция drag_and_drop
    # actions.click_and_hold(drag_me)
    # actions.move_to_element(drop_here)
    # actions.release()
    # actions.perform()
    driver.quit()

def test_open_new_tab(driver):
    driver.get('https://www.qa-practice.com/elements/dragndrop/boxes')
    inputs = driver.find_element(By.LINK_TEXT, 'Inputs')
    ActionChains(driver).key_down(Keys.COMMAND).click(inputs).key_up(Keys.COMMAND).perform()

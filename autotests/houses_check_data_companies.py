from selenium.webdriver.common.by import By
import allure
import pytest
from helpers.api.household_api import HouseholdAPI


@pytest.mark.tags("administrator", "companies")
@pytest.mark.xdist_group(name="companies")
@pytest.mark.preprod
@allure.title(
    "Отображение блока управляющей компании на странице дома"
)
def test_positive(houses):
    id_house = '11199'
    id_company = '142'
    houses.helpers.page_houses.open_house_by_id(id_house)
    houses.wd.find_element(By.XPATH, '//h3[text()="Управляющие компании"]').click()
    assert houses.wd.find_elements(
        By.XPATH, '//h3[text()="Управляющие компании"]/parent::*[contains(@class, "Mui-expanded")]'
    ), f'Список управляющих компаний не разворачивается'


    household_api = HouseholdAPI()
    company_data = household_api.get_company_by_id(id_company)


    company_id = houses.wd.find_element(By.XPATH, '//div[@data-field="id"]//div[@title]').text
    assert company_id == str(
        company_data['id']), f'ID "{company_id}" не соответствует значению id компании'

    company_name = houses.wd.find_element(By.XPATH, '//div[@data-field="name"]//div[@title]').text
    assert company_name == company_data[
        'name'], f'Название "{company_name}" не соответствует названию компании'

    company_email = houses.wd.find_element(By.XPATH, '//div[@data-field="ownerEmail"]//div[@title]').text
    assert company_email == company_data[
               'owner_email'], f'Электронный адрес "{company_email}" не соответствует email компании'

    company_plan_slug = houses.wd.find_element(By.XPATH, '//div[@data-field="planSlug"]//div[@title]').text
    assert company_plan_slug == company_data[
               'plan_slug'], f'Тариф "{company_plan_slug}" не соответствует тарифному плану компании'

    company_city = houses.wd.find_element(By.XPATH, '//div[@data-field="city"]//div[@title]').text
    assert company_city == company_data[
               'city'], f'Название "{company_city}" не соответствует городу компании'

    company_street = houses.wd.find_element(By.XPATH, '//div[@data-field="street"]//div[@title]').text
    assert company_street == company_data[
               'street'], f'Название "{company_street}" не соответствует улице компании'

    company_house = houses.wd.find_element(By.XPATH, '//div[@data-field="house"]//div[@title]').text
    assert company_house == company_data[
               'house'], f'Номер "{company_house}" не соответствует номеру дома компании'

    company_office = houses.wd.find_element(By.XPATH, '//div[@data-field="office"]//div[@title]').text
    assert company_office == company_data[
               'office'], f'Номер "{company_office}" не соответствует номеру офиса компании'

    company_vc_id = houses.wd.find_element(By.XPATH, '//div[@data-field="vcCompanyId"]//a').text
    assert company_vc_id == str(company_data[
               'vc_company_id']), f'ID "{company_vc_id}" не соответствует id видеоплатформы'


    vc = houses.wd.find_element(By.XPATH, '//div[@data-field="vcCompanyId"]/a')
    vc.click()
    current_link = vc.get_attribute("href")
    windows = houses.wd.window_handles
    houses.wd.switch_to.window(windows[-1])
    vn_url = houses.wd.current_url
    houses.wd.close()
    houses.wd.switch_to.window(windows[0])
    assert current_link == f'https://admin-b2c.camera-p1.cloud.rt.ru/admin/user_groups/{company_vc_id}', f'Ссылка {current_link} не валидна'
    assert vn_url == 'https://admin-b2c.camera-p1.cloud.rt.ru/', 'Переход в админку ВН не осуществился'


    houses.wd.find_element(By.XPATH, '//h3[text()="Управляющие компании"]').click()
    assert not houses.wd.find_elements(
        By.XPATH, '//h3[text()="Управляющие компании"]/parent::*[contains(@class, "Mui-expanded")]'
    ), f'Список управляющих компаний не сворачивается'
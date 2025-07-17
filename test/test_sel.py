import pytest
import allure

@pytest.mark.parametrize('name', ['qwerty', 'QWERTY', 'Русский'])
@allure.title('Создание и удаление купона')
def test_coupon(app, name):
    with allure.step('Создание купона'):
        app.create_coupon(name)
        app.screen_shot('Купон создан')
        assert name == app.get_name_of_coupon_from_first_row(), f'Ожидаемое имя купона {name} не соответствует реальному {app.get_name_of_coupon_from_first_row()}'

    with allure.step('Удаление купона'):
        app.delete_coupon(name)
        app.screen_shot('Купон удален')
        assert app.check_that_coupon_deleted(), f'Купон не удалился'
        app.screen_shot('Купона нет в таблице')

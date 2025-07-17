import allure
import pytest

@pytest.mark.parametrize('number', ['3', '7', '10'])
@allure.title('Добавление товара со скидкой в корзину и последующее его удаление')
def test_duck(appli, number):
    try:
        with allure.step('Заполнение поля Quantity'):
            appli.quantity_selection(number)
            appli.screen_shot(f'В поле quantity введено {number}')
        with allure.step('Добавление товара в корзину'):
            appli.add_to_cart()
            appli.screen_shot_add_to_cart('Выбранное количество товара отображается в корзине')
            assert number == appli.check_add_to_cart().text, f'Количество товара {appli.check_add_to_cart().text} не соответствует {number}'

    finally:
        with allure.step('Удаление товара из корзины'):
            appli.cart_clear()
            appli.screen_shot('Корзина пуста')
            assert appli.check_clear_cart().text == '0', f'Товары еще в корзине'
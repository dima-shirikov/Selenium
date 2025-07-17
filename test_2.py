import pytest

variable = None

# def setup_function():     # Пред и пост условия через setup и teardown
#     global variable
#     if variable is None:
#         variable = 1
#     print('Hi')
#
# def teardown_function():
#     global variable
#     variable += 1
#     print('By')
#
# def test_a(app):
#     assert variable == 1
#
# def test_b(app):
#     assert variable == 2

@pytest.fixture()       # Пред условие через декоратор fixture
def app():
    global variable
    if variable is None:
        variable = 1
    print('app')
    return variable

@pytest.fixture(autouse=True, scope='session')       # Пост условие через декоратор fixture; autouse означает что после каждого теста нужно запускать fixture; scope означает что fixture нужно запустить только после выполнения всех тестов в файле
def stop(request):
    def teardown_function():
        global variable
        variable += 1
        print('stop')
    request.addfinalizer(teardown_function)

def test_a(app):
    assert app == 1

def test_b(app):
    assert app == 1
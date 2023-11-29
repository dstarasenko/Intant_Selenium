import pytest


@pytest.fixture()
def set_up():  # Добавить этот метод в аргументы теста
    print(f"\nStart test\n")
    yield
    print("\nFinish Test\n")


@pytest.fixture(scope="module")  # Для всего файла
def set_group():
    print("Enter system")
    yield
    print("Exit System")

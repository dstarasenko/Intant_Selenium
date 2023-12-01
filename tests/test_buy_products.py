import time
import allure
import sys

from selenium import webdriver
from pages.catalog_page import CatalogPage
from pages.main_page import MainPage
from pages.filters_page import FiltersPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.delivery_page import DeliveryPage
from base.base_class import Base



@allure.description("Test buy product")
def test_buy_product(set_up):
    driver = webdriver.Chrome()

    # Авторизация на сайте
    try:
        mp = MainPage(driver)
        mp.authorization()
        time.sleep(1)
    except Exception as e:
        print("Authorization failed!")
        b = Base(driver)
        b.get_screenshot("fail_auth")
        sys.exit()

    # Переходим в каталог, выбираем раздел "Модули памяти"
    try:
        cat_p = CatalogPage(driver)
        cat_p.ram_in_catalog()
    except Exception as e:
        print("Open catalog failed!")
        b = Base(driver)
        b.get_screenshot("fail_open_catalog")
        sys.exit()

    # Активируем фильтры
    try:
        fp = FiltersPage(driver)
        fp.add_filters()
        time.sleep(1)
    except Exception as e:
        print("Filter settings failed")
        b = Base(driver)
        b.get_screenshot("fail_filter")
        sys.exit()


    # Выбираем оперативку, добавляем в корзину
    try:
        pp = ProductPage(driver)
        pp.add_product_to_cart()
        time.sleep(1)
    except Exception as e:
        print("Select RAM failed")
        b = Base(driver)
        b.get_screenshot("fail_select_RAM")
        sys.exit()


    # Начало оформления заказа
    try:
        cp = CartPage(driver)
        cp.checkout()
        time.sleep(1)
    except:
        print("Start checking failed")
        b = Base(driver)
        b.get_screenshot("fail_placing_order")
        sys.exit()

    # Заполнение данных получателя заказа
    try:
        dp = DeliveryPage(driver)
        dp.entering_delivery_data()
        time.sleep(1)
    except Exception as e:
        print("Entering delivery data failed")
        b = Base(driver)
        b.get_screenshot("fail_delivery_data")
        sys.exit()

    """
        На этом стоп, т.к. скорее всего, дальнейшие действия подтвердят заказ и запустят процесс оплаты.
    """
    b = Base(driver)
    b.get_screenshot("finish")


    time.sleep(5)
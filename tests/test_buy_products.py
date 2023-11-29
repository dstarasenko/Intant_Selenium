import time
from selenium import webdriver
from pages.catalog_page import Catalog_page
from pages.main_page import Main_page
from pages.filters_page import Filters_page
from pages.product_page import Product_page
from pages.cart_page import Cart_page
from pages.delivery_page import Delivery_page
from base.base_class import Base
import sys



def test_select_products(set_up):
    driver = webdriver.Chrome()

    # Авторизация на сайте
    try:
        mp = Main_page(driver)
        mp.authorization()
        time.sleep(1)
    except Exception as e:
        print("Authorization failed!")
        b = Base(driver)
        b.get_screenshot("fail_authorization")
        sys.exit()


    # Переходим в каталог, выбираем раздел "Модули памяти"
    try:
        cat_p = Catalog_page(driver)
        cat_p.ram_in_catalog()
    except Exception as e:
        print("Open catalog failed!")
        b = Base(driver)
        b.get_screenshot("open_catalog_fail")
        sys.exit()

    # Активируем фильтры
    try:
        fp = Filters_page(driver)
        fp.mountain_ski_filters()
        time.sleep(1)
    except Exception as e:
        print("Filter settings failed")
        b = Base(driver)
        b.get_screenshot("filter_settings_fail")
        sys.exit()


    # Выбираем оперативку, добавляем в корзину
    try:
        pp = Product_page(driver)
        pp.add_product_to_cart()
        time.sleep(1)
    except Exception as e:
        print("Select skies failed")
        b = Base(driver)
        b.get_screenshot("select_RAM_fail")
        sys.exit()


    # Выбираем лыжи, добавляем в корзину
    try:
        pp = Product_page(driver)
        pp.add_product_to_cart()
        time.sleep(1)
    except Exception as e:
        print("Select skies failed")
        b = Base(driver)
        b.get_screenshot("select_skies_fail")
        sys.exit()


    # Начало оформления заказа: выбираем город доставки и кликаем "оформить"
    try:
        cp = Cart_page(driver)
        cp.checkout()
        time.sleep(1)
    except:
        print("Start checking failed")
        b = Base(driver)
        b.get_screenshot("start_checking_fail")
        sys.exit()

    # Заполнение данных получателя заказа
    try:
        dp = Delivery_page(driver)
        dp.entering_delivery_data()
        time.sleep(1)
    except Exception as e:
        print("Entering delivery data failed")
        b = Base(driver)
        b.get_screenshot("delivery_data_fail")
        sys.exit()

    """
        На этом стоп, т.к. скорее всего, дальнейшие действия подтвердят заказ и запустят процесс оплаты.
    """

    time.sleep(5)
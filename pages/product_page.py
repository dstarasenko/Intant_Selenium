import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from base.base_class import Base
from utilities.logger import Logger

""" 
    Страница каталога горных лыж после фильтров.
    Открываем страничку товара.
    Добавляем в корзину.
    Переходим в корзину
"""


class Product_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Локаторы

    select_product_button = '//*[@id="sgoodscontainer"]/div/div[1]/a' # Локатор Corsair 2x8ГБ DDR4 SDRAM "Vengeance LPX" CMK16GX4M2B3200C16W
    add_to_cart_button = '/html/body/div[3]/div[2]/div[1]/div[1]/div[2]/div[2]/a/label' # Локатор добавления товара в корзину
    go_to_cart_button = '/html/body/div[1]/div[4]/div/div/div[2]/a[5]/div[2]' # Локатор кнопки перехода в корзину
    add_to_cart_repeat_button = '/html/body/div[4]/div[6]/div[11]/div[2]/div[2]/form/table[2]/tbody/tr/td[3]/div/div/input' # Локатор подтверждение добавления товара в корзину на всплывающем окне


    # Геттеры

    def get_select_product_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_button)))

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))

    def get_go_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart_button)))



    # Действия

    def click_select_product_button(self):
        self.get_select_product_button().click()
        print(f"Click select product button")

    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print(f"Click add to cart button")

    def click_go_to_cart_button(self):
        self.get_go_to_cart_button().click()
        print(f"Click go to cart button")


    # Методы

    def add_product_to_cart(self):
        Logger.add_start_step(method='add_product_to_cart')
        self.get_current_url()
        self.assert_url("https://e.intant.ru/catalog/hardware/memory?flt=Yzo1MDAwOzkwMDAsZjowXzQzOzFfMjczNjM7MV8zMDIwOzFfMzA1NDsxXzI5MzE1")
        self.click_select_product_button()
        self.click_add_to_cart_button()
        self.click_go_to_cart_button()
        Logger.add_end_step(url=self.driver.current_url, method='add_product_to_cart')





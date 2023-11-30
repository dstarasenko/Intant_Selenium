import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


from base.base_class import Base

""" 
    Страница корзины.
    Тут необходимо выбрать город доставки
    и прожать кнопку "оформить"
"""


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Локаторы


    select_quantity_field = '/html/body/div[3]/div[2]/div/div/div[1]/div[2]/div[1]/input' # Локатор поля ввода количества товара, ставим 3
    checkout_button = '//a[@class="u-f-right btn_yellow"]'  # Локатор кнопки "оформить заказ"

    check_name = '/html/body/div[3]/div[2]/div/div/div[1]/div[2]/a[1]/span[2]/span[1]' # Для проверки наименования товара в корзине
    check_price = '/html/body/div[3]/div[2]/div/div/div[2]/span[2]' # Для проверки стоимости товара в корзине


    # Геттеры


    def get_select_quantity_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_quantity_field)))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    def get_check_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_name)))

    def get_check_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_price)))



    # Действия с локаторами

    def input_select_quantity_field(self, text):
        self.get_select_quantity_field().send_keys(Keys.BACKSPACE*10)
        self.get_select_quantity_field().send_keys(text)
        print(f"Enter quantity = 3 ")

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print(f"Click checkout button")


    # Методы

    def checkout(self):
        self.get_current_url()
        self.driver.refresh()  # Т.к. кнопка "Оформить заказ" может становится не активной.
        self.input_select_quantity_field("3")
        time.sleep(3) # Потому что стоимость обновляется в течении 1-2сек
        self.assert_word(self.get_check_name(), 'Модуль памяти Corsair 2x8ГБ DDR4 SDRAM "Vengeance LPX" CMK16GX4M2B3200C16W')
        self.assert_word(self.get_check_price(), '22 017 ₽')
        self.click_checkout_button()





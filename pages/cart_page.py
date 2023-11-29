import time

from selenium.webdriver import ActionChains
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
    checkout_button = '/html/body/div[3]/div[2]/div/div/div[4]/a[2]'  # Локатор кнопки "оформить заказ"
    select_town_field = '//*[@id="frm"]/div/div[3]/table/tbody/tr[1]/td[3]/div[2]/input[1]' # Локатор поля ввода названия города
    select_tomsk_button = '//*[@id="frm"]/div/div[3]/table/tbody/tr[1]/td[3]/div[2]/div/span[1]'  # Локатор пункта "Томск, Томская обл." в выпадающем списке
    checkout_button = '//*[@id="frm"]/div/div[3]/table/tbody/tr[3]/td[5]/div/div/input'  # Локатор кнопки "оформить"


    # Геттеры


    def get_select_quantity_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_quantity_field)))

    def get_select_town_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_town_field)))

    def get_select_tomsk_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_tomsk_button)))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))


    # Действия с локаторами

    def input_select_quantity_field(self, text):
        self.get_select_quantity_field().send_keys(text)
        print(f"Enter quantity = 3 ")

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print(f"Click checkout button")


    # Методы

    def checkout(self):
        self.get_current_url()
        self.input_select_quantity_field("3")
        self.click_checkout_button()





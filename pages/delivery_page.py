import time
import allure


from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from base.base_class import Base
from utilities.logger import Logger

"""
    Страница заполнения данных получателя заказа
"""

@allure.epic(" Страница с данными получателя заказа ")
class DeliveryPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Локаторы

    telephone_field = '//*[@id="OrderPhone"]'  # Поле ввода номера телефона
    fullname_field = '//*[@id="OrderFio"]'  # Поле ввода ФИО получателя
    delivery_method_checkbox = '//*[@id="orderpartform"]/fieldset[2]/div[1]/div[1]/label[3]/span[1]' # Курьерская служба СДЭК
    town_button = '//*[@id="orderpartform"]/fieldset[2]/div[1]/div[2]/div/a' # Кнопка смены города
    select_town_button = '/html/body/div[1]/div[1]/div/div/div[3]/div[3]/a[147]' # Выбираем Северск
    address_field = '//*[@id="DeliveryAddress"]' # Поле адреса
    where_button = '//*[@id="select_dlvpvz"]' # Выпадающий список "Куда доставлять"
    postomat_button = '//*[@id="select_dlvpvz"]/option[3]' # Пункт "на Транспортную"
    card_checkbox = '//*[@id="orderpartform"]/fieldset[2]/div[3]/div/label[2]/span[1]' # Чекбокс "Оплата картой"
    comment_field = '//*[@id="OrderComment"]' # Поле ввода комментария
    agree_checkbox = '//*[@id="ConfirmPersonalDataOrder"]' # Чекбокс согласия
    continue_button = '//*[@id="utfield"]/form/div[3]/div/button' # Кнопка "Отправить заказ"


    # Геттеры

    def get_telephone_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.telephone_field)))

    def get_fullname_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.fullname_field)))

    def get_delivery_method_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery_method_checkbox)))

    def get_town_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.town_button)))

    def get_select_town_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_town_button)))

    def get_address_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.address_field)))

    def get_where_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.where_button)))

    def get_postomat_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.postomat_button)))

    def get_card_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.card_checkbox)))

    def get_comment_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.comment_field)))

    def get_agree_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.agree_checkbox)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))


    # Действия

    def input_telephone_field(self, text):
        self.get_telephone_field().send_keys(text)
        print(f"Input telephone number")

    def input_fullname_field(self, text):
        self.get_fullname_field().send_keys(text)
        print(f"Input full name")

    def click_delivery_method_checkbox(self):
        self.get_delivery_method_checkbox().click()
        print(f"Click delivery method checkbox")

    def click_town_button(self):
        self.get_town_button().click()
        print(f"Click town button")

    def click_select_town_button(self):
        self.get_select_town_button().click()
        print(f"Click select town Seversk button")

    def input_address_field(self, text):
        self.get_address_field().send_keys(text)
        print(f"Input mail")

    def click_where_button(self):
        self.get_where_button().click()
        print(f"Click where delivery button")

    def click_postomat_button(self):
        self.get_postomat_button().click()
        print(f"Click postomat button")

    def click_card_checkbox(self):
        self.get_card_checkbox().click()
        print(f"Click card checkbox")

    def input_comment_field(self, text):
        self.get_comment_field().send_keys(text)
        print(f"Input comment")

    def click_agree_checkbox(self):
        self.get_agree_checkbox().click()
        print(f"Click agree checkbox")

    def click_continue_button(self):
        self.get_continue_button().click()
        print(f"Click continue button")


    # Методы

    def entering_delivery_data(self):
        with allure.step("Entering delivery data"):
            Logger.add_start_step(method='entering_delivery_data')
            self.get_current_url()
            self.input_telephone_field("+7 (456) 456-45-66")
            self.input_fullname_field("Иванов Иван Иванович")
            self.click_delivery_method_checkbox()
            self.click_town_button()
            self.click_select_town_button()
            self.input_address_field("Северск, ул. Маяковского, д.6, кв.23")
            self.click_where_button()
            self.click_postomat_button()
            self.click_card_checkbox()
            self.input_comment_field("test")
            #self.click_agree_checkbox() # будет отжат этой командой, если пользователь залогинен в профиль

            # Так как заказ будет отправлен, клик по кнопке "отправить заказ" отключен
            #self.click_continue_button()
            Logger.add_end_step(url=self.driver.current_url, method='entering_delivery_data')





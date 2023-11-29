import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from base.base_class import Base
"""
    Страница заполнения данных получателя заказа
"""

class Delivery_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Локаторы


    telephone_field = '//*[@id="OrderPhone"]'  # Поле ввода номера телефона
    fullname_field = '//*[@id="OrderFio"]'  # Поле ввода ФИО получателя
    mail_field = '//*[@id="OrderEmail"]'  # Поле ввода эл.почты
    address_field = '//*[@id="DeliveryAddress"]' # Поле ввода индекса
    payment_method_checkbox = '//*[@id="orderpartform"]/fieldset[2]/div[2]/div[1]/label[1]/span[2]'
    comment_field = '//*[@id="OrderComment"]' # Поле ввода комментария
    agreement_checkbox = '//*[@id="ConfirmPersonalDataOrder"]' # Чекбокс необходимости звонка оператора (Ставим НЕТ)
    continue_button = '//*[@id="utfield"]/form/div[3]/div/button' # Кнопка "Отправить заказ"
    pvz_checkbox = '//*[@id="frm"]/div/div/div[2]/div[2]/label' # Чекбокс выбора способа доставки
    index_field = '//*[@id="for_delivery2"]/table/tbody/tr[3]/td[2]/div/input' # Поле ввода индекса
    street_field = '//*[@id="for_delivery2"]/table/tbody/tr[5]/td[2]/div/input' # Поле ввода улицы
    house_field = '//*[@id="for_delivery2"]/table/tbody/tr[7]/td[2]/div/input' # Поле ввода номера дома
    frame_field = '//*[@id="for_delivery2"]/table/tbody/tr[9]/td[2]/div/input' # Поле ввода номера корпуса
    apartment_field = '//*[@id="for_delivery2"]/table/tbody/tr[11]/td[2]/div/input' # Поле ввода номера квартиры
    fullname_field = '//*[@id="for_delivery2"]/table/tbody/tr[13]/td[2]/div/input' # Поле ввода ФИО получателя
    telephone_field = '//*[@id="for_delivery2"]/table/tbody/tr[15]/td[2]/div/input' # Поле ввода номера телефона
    disc_card_field = '//*[@id="for_delivery2"]/table/tbody/tr[17]/td[2]/div/input' # Поле ввода номера дисконтной карты
    comment_field = '//*[@id="for_delivery2"]/table/tbody/tr[19]/td[2]/div/textarea' # Поле ввода комментария
    operator_call_checkbox = '//label[text()[contains(.,"Нет")]]' # Чекбокс необходимости звонка оператора (Ставим НЕТ)
    continue_button = '//*[@id="frm"]/div/div/table[2]/tbody/tr/td[3]/div/div/input' # Кнопка продолжить



    # Геттеры

    def get_pvz_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pvz_checkbox)))

    def get_index_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.index_field)))

    def get_street_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.street_field)))

    def get_house_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.house_field)))

    def get_frame_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.frame_field)))

    def get_apartment_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.apartment_field)))

    def get_fullname_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.fullname_field)))

    def get_telephone_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.telephone_field)))

    def get_disc_card_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.disc_card_field)))

    def get_comment_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.comment_field)))

    def get_operator_call_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.operator_call_checkbox)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))


    # Действия

    def click_pvz_checkbox(self):
        self.get_pvz_checkbox().click()
        print(f"Click pvz checkbox")

    def input_index_field(self, text):
        self.get_index_field().send_keys(text)
        print(f"Input index")

    def input_street_field(self, text):
        self.get_street_field().send_keys(text)
        print(f"Input street")

    def input_house_field(self, text):
        self.get_house_field().send_keys(text)
        print(f"Input house number")

    def input_frame_field(self, text):
        self.get_frame_field().send_keys(text)
        print(f"Input frame number")

    def input_apartment_field(self, text):
        self.get_apartment_field().send_keys(text)
        print(f"Input apartment number")

    def input_fullname_field(self, text):
        self.get_fullname_field().send_keys(text)
        print(f"Input full name")

    def input_telephone_field(self, text):
        self.get_telephone_field().send_keys(text)
        print(f"Input telephone number")

    def input_disc_card_field(self, text):
        self.get_disc_card_field().send_keys(text)
        print(f"Input discount card number")

    def input_comment_field(self, text):
        self.get_comment_field().send_keys(text)
        print(f"Input comment")

    def click_operator_call_checkbox(self):
        self.get_operator_call_checkbox().click()
        print(f"Click operator call checkbox (No)")

    def click_continue_button(self):
        self.get_continue_button().click()
        print(f"Click continue button")


    # Методы

    def entering_delivery_data(self):
        self.get_current_url()
        #self.click_pvz_checkbox() # Отключил, т.к. нужный чекбокс выбран по-умолчанию.
        self.input_index_field("634003")
        self.input_street_field("Мичурина")
        self.input_house_field("2")
        self.input_frame_field("1")
        self.input_apartment_field("100")
        self.input_fullname_field("Иванов Иван Иванович")
        self.input_telephone_field("+7 (456) 456-45-66")
        self.input_disc_card_field("12345678")
        self.input_comment_field("test")
        self.click_operator_call_checkbox()
        self.click_continue_button()





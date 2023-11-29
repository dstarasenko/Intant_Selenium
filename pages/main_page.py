import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from base.base_class import Base

""" 
    Главная страница магазина https://e.intant.ru/.
    На этой же странице происходит логин в учетку
    через всплывающее окно.
    Логин - testqadst@rambler.ru
    Пароль - dst_testqa
"""


class Main_page(Base):
    main_url = "https://e.intant.ru/"  # Главная страница магазина

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Локаторы

    town_button = '//a[@class="js-choosecity-close"]'
    profile_button = '/html/body/div[1]/div[3]/div/div[1]/a[1]'  # Кнопка профиля
    user_name = '//*[@id="Login"]'  # Поле ввода логина
    password = '//*[@id="Password"]'  # Поле ввода пароля
    login_button = '//*[@id="loginContent"]/div[4]/input'  # Кнопка логина в профиль


    # Геттеры

    def get_town_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.town_button)))

    def get_profile_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.profile_button)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    # Действия

    def click_town_button(self):
        self.get_town_button().click()
        print("Click town button")

    def click_profile_button(self):
        self.get_profile_button().click()
        print("Click profile button")

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name ")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

    # Методы

    def authorization(self):
        self.driver.get(self.main_url)
        self.driver.maximize_window()
        self.get_current_url()
        time.sleep(3)
        self.click_town_button()
        time.sleep(3)
        self.click_profile_button()
        self.input_user_name("testqadst@rambler.ru")
        self.input_password("dst_testqa")
        self.click_login_button()

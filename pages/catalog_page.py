import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from base.base_class import Base
from utilities.logger import Logger

""" 
    Главная страница магазина.
    Делаем клик по пункту "Лыжи горные" в левом меню каталога.
    Далее клик по пункту "Лыжи горные" во всплывающем окне
    для перехода к фильтрам.
"""


class Catalog_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Локаторы

    catalog_button = '/html/body/div[1]/div[4]/div/a[2]'  # Кнопка каталога
    components_button = '/html/body/div[2]/div/div[2]/a[4]'  # Кнопка "комплектующие"
    ram_button = '/html/body/div[3]/div[2]/div[1]/div/div[4]/a' # Кнопка "модули памяти"


    # Геттеры

    def get_catalog_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_button)))

    def get_components_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.components_button)))

    def get_ram_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.ram_button)))

    # Действия

    def click_catalog_button(self):
        self.get_catalog_button().click()
        print("Click catalog button")

    def click_components_button(self):
        self.get_components_button().click()
        print("Select components button")

    def click_ram_button(self):
        self.get_ram_button().click()
        print("Select RAM")

    # Методы

    def ram_in_catalog(self):
        Logger.add_start_step(method='ram_in_catalog')
        self.get_current_url()
        self.click_catalog_button()
        time.sleep(1)
        self.click_components_button()
        self.click_ram_button()
        Logger.add_end_step(url=self.driver.current_url, method='ram_in_catalog')




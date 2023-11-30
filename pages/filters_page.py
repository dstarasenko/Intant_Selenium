import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from base.base_class import Base

""" 
    Страница каталога оперативной памяти.
    Настраиваем фильтры.
"""


class Filters_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Локаторы

    f_price_from = '//*[@id="minCost"]' # Поле ввода нижнего порога стоимости
    f_price_to = '//*[@id="maxCost"]' # Поле ввода верхнего порога стоимости
    f_brand = '/html/body/div[3]/div/div[2]/div/div[3]/div[1]/div/div/div[4]/div[2]/div[3]/label[1]/span[1]'    # Локатор бренда Corsair
    type_button = '/html/body/div[3]/div/div[2]/div/div[3]/div[1]/div/div/div[5]/div[1]/div' # Кнопка раскрытия выпадающего списка с типами RAM
    f_type = '/html/body/div[3]/div/div[2]/div/div[3]/div[1]/div/div/div[5]/div[2]/div[2]/label/span[2]'   # Локатор пункта фильтра DDR4
    volume_button = '/html/body/div[3]/div/div[2]/div/div[3]/div[1]/div/div/div[6]/div[1]/div' # Кнопка раскрытия выпадающего списка с объемом комплекта
    f_volume = '/html/body/div[3]/div/div[2]/div/div[3]/div[1]/div/div/div[6]/div[2]/div[4]/label'  # Локатор пункта фильтра 16гб
    quantity_button = '/html/body/div[3]/div/div[2]/div/div[3]/div[1]/div/div/div[7]/div[1]/div'  # Кнопка раскрытия выпадающего списка с кол-вом модулей в комплекте
    f_quantity = '/html/body/div[3]/div/div[2]/div/div[3]/div[1]/div/div/div[7]/div[2]/div[2]/label'  # Локатор пункта фильтра 2
    frequency_button = '/html/body/div[3]/div/div[2]/div/div[3]/div[1]/div/div/div[9]/div[1]/div'  # Кнопка раскрытия выпадающего списка с частотой RAM
    f_frequency = '/html/body/div[3]/div/div[2]/div/div[3]/div[1]/div/div/div[9]/div[2]/div[9]/label/span[2]'  # Локатор пункта фильтра 3200
    show_button = '//*[@id="applyFilter"]' # Кнопка "Показать", применяем фильтры

    # Геттеры

    def get_f_price_from(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.f_price_from)))

    def get_f_price_to(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.f_price_to)))

    def get_f_brand(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.f_brand)))

    def get_type_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.type_button)))

    def get_f_type(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.f_type)))

    def get_volume_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.volume_button)))

    def get_f_volume(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.f_volume)))

    def get_quantity_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.quantity_button)))

    def get_f_quantity(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.f_quantity)))

    def get_frequency_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.frequency_button)))

    def get_f_frequency(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.f_frequency)))

    def get_show_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.show_button)))


    # Действия

    def input_price_from(self, price_from):
        self.get_f_price_from().send_keys(price_from)
        print(f"Input price from {price_from}")

    def input_price_to(self, price_to):
        self.get_f_price_to().send_keys(price_to)
        print(f"Input price from {price_to}")

    def select_brand(self):
        self.get_f_brand().click()
        print(f"Select brand Corsair")

    def click_type_button(self):
        self.get_type_button().click()
        print(f"Click type button")

    def select_type(self):
        self.get_f_type().click()
        print(f"Select type DDR4")

    def click_volume_button(self):
        self.get_volume_button().click()
        print(f"Click volume button")

    def select_volume(self):
        self.get_f_volume().click()
        print(f"Select 16gb")

    def click_quantity_button(self):
        self.get_quantity_button().click()
        print(f"Click quantity button")

    def select_quantity(self):
        self.get_f_quantity().click()
        print(f"Select 2 pieces")

    def click_frequency_button(self):
        self.get_frequency_button().click()
        print(f"Click frequency button")

    def select_frequency(self):
        self.get_f_frequency().click()
        print(f"Select 3200 mhz")

    def click_show_button(self):
        self.get_show_button().click()
        print(f"Click show button")


    # Методы

    def add_filters(self):
        self.get_current_url()
        self.input_price_from("5000")
        self.input_price_to("9000")
        self.select_brand()
        self.click_type_button()
        self.select_type()
        self.click_volume_button()
        self.select_volume()
        self.driver.execute_script('window.scrollTo(0,400)')  # Скролл, чтобы увидеть настроенные фильтры
        self.click_quantity_button()
        self.select_quantity()
        self.click_frequency_button()
        self.select_frequency()
        self.driver.execute_script('window.scrollTo(0,1000)') # Скролл, чтобы увидеть настроенные фильтры
        time.sleep(1)
        self.click_show_button()





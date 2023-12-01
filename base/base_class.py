import datetime


class Base():

    def __init__(self, driver):
        self.driver = driver

    """ Получение текущей URL """
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current url {get_url}")


    """ Метод проверки соответствия наименования товара """
    def assert_word(self, received, expected):
        value_received = received.text
        assert value_received == expected
        print("Good value string")

    """ Метод проверки соответствия стоимости """
    def assert_price(self, received, expected):
        value_price = received.text[:-2].replace(" ", "")
        assert int(value_price) == expected
        print("Good value price")


    """ Создание скриншота """
    def get_screenshot(self, screen_name):
        now_date = datetime.datetime.now(datetime.UTC).strftime("%Y.%m.%d.%H.%M.%S")
        self.driver.save_screenshot(f"screenshots\\{screen_name}_{now_date}.png")


    """ Метод проверки URL """
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value URL")


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # Для автоматической установки chromedriver
import unittest
import time


class FlaskAppTest(unittest.TestCase):

    def setUp(self):
        # Использование webdriver_manager для автоматической установки chromedriver
        service = Service(ChromeDriverManager().install())  # Автоматически установит chromedriver
        self.driver = webdriver.Chrome(service=service)

    def tearDown(self):
        self.driver.quit()

    def test_home_page(self):
        self.driver.get("http://127.0.0.1:5000/")  # URL главной страницы
        time.sleep(1)
        title = self.driver.title
        self.assertIn("Главная", title)  # Проверяем, что на главной странице в заголовке содержится слово "Главная"

    def test_catalog_page(self):
        self.driver.get("http://127.0.0.1:5000/catalog")  # URL страницы каталога
        time.sleep(1)
        title = self.driver.title
        self.assertIn("Каталог товаров", title)  # Проверяем, что на странице каталога в заголовке содержится слово "Каталог"

        # Дополнительно проверяем, что на странице есть товары, если они есть в базе данных
        products = self.driver.find_elements(By.CSS_SELECTOR, ".product")
        self.assertGreater(len(products), 0)  # Убедимся, что товары отображаются на странице

    def test_about_page(self):
        self.driver.get("http://127.0.0.1:5000/about")  # URL страницы "О нас"
        time.sleep(1)
        title = self.driver.title
        self.assertIn("О нас", title)  # Проверяем, что на странице "О нас" в заголовке содержится слово "О нас"


if __name__ == "__main__":
    unittest.main()

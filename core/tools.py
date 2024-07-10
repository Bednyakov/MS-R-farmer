import time
import json
import requests
from core.loggers import logger
from selenium import webdriver
from config import proxies, headers
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class CookieMaker:
    
    def get_cookies_with_selenium(url: str, user_profile: str, pause: int = 5):
        """
        Получение coockies с помощью Selenium.
        """

        # Настройка параметров Chrome
        options = Options()
        options.add_argument(f"user-data-dir={user_profile}")

        # Указание пути к chromedriver
        # service = Service('chromedriver\chromedriver.exe')

        # Инициализация WebDriver с профилем пользователя
        driver = webdriver.Chrome(options=options)
        
        driver.get(url)
        
        time.sleep(pause)
        
        cookies = driver.get_cookies()
        driver.quit()
        logger.info('Куки получены.')
        return cookies


    def save_cookies_to_file(cookies, filename: str) -> None:
        """
        Сохранеие coockies в файл.
        """
        with open(filename, 'w') as file:
            json.dump(cookies, file)
            logger.info('Куки сохранены.')


class CookieRequests:

    def load_cookies_from_file(filename):
        """
        Загрузка куки из файла.
        """
        with open(filename, 'r') as file:
            cookies = json.load(file)
        return cookies

    def cookies_to_requests_format(cookies):
        """
        Перевод куки в формат под requests.
        """
        session_cookies = {}
        for cookie in cookies:
            session_cookies[cookie['name']] = cookie['value']
        return session_cookies

    def make_request_with_cookies(url: str, cookies, prox: bool):
        """
        Запрос с куки.
        """
        session = requests.Session()
        session.cookies.update(cookies)
        if prox:
            response = session.get(url, proxies=proxies)
            return response
        response = session.get(url)
        return response


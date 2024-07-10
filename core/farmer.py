from core.tools import CookieMaker, CookieRequests
from core.loggers import logger
from random import choice


class Farmer:
    def __init__(self, 
                 url_for_receiving_cookies: str,
                 user_profile: str, 
                 cookies_file: str, 
                 url_for_bing_requests: str):
        
        self.url_for_receiving_cookies = url_for_receiving_cookies 
        self.user_profile = user_profile
        self.cookies_file = cookies_file
        self.url_for_bing_requests = url_for_bing_requests


    def save_cookies(self) -> None:
        """
        Получаем куки и сохраняем их в файл.
        """
        cookies = CookieMaker.get_cookies_with_selenium(url=self.url_for_receiving_cookies,
                                                        user_profile=self.user_profile)
        CookieMaker.save_cookies_to_file(cookies, self.cookies_file)

    def farm_points(self, proxies: bool=False):
        """
        Загружаем куки из файла и используем их для запросов.
        """
        cookies = CookieRequests.load_cookies_from_file(self.cookies_file)
        requests_cookies = CookieRequests.cookies_to_requests_format(cookies)

        search_query = self.url_for_bing_requests + self.get_search_query()

        response = CookieRequests.make_request_with_cookies(search_query, requests_cookies, proxies)
        return response

    def get_search_query(self):
        with open('words.txt', 'r') as file:
            text = file.read()
            word = choice(text.split())
            logger.info(f'Запрос: {word}')

            return f'search?q={word}'



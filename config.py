url_for_receiving_cookies = 'https://rewards.bing.com/'  # Стартовая страница Rewards
url_for_bing_requests = 'https://www.bing.com/'  # Страница поисковика
user_profile = "C:/Users/Артем/AppData/Local/Google/Chrome/User Data"  # Замените на путь к профилю вашего установленного Chrome
cookies_file = 'cookies.json'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'ru,en-US;q=0.9,en;q=0.8',
    'Content-Type': 'application/json',
    'Referer': 'https://www.bing.com/?form=ML2PCO',
    'Priority': 'u=1, i',
}

proxies = {
    'http': 'http://login:password@ip:port',
    'https': 'http://login:password@ip:port'
}

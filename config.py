url_for_receiving_cookies = 'https://rewards.bing.com/'  # Стартовая страница Rewards
url_for_bing_requests = 'https://www.bing.com/'  # Страница поисковика
user_profile = "C:/Users/Артем/AppData/Local/Google/Chrome/User Data"  # Замените на путь к профилю вашего установленного Chrome
cookies_file = 'cookies.json'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}

proxies = {
    'http': 'http://login:password@ip:port',
    'https': 'http://login:password@ip:port'
}
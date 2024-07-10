import time
from core.farmer import Farmer
from random import randint
from core.parser import get_ballance, get_title
from config import url_for_bing_requests, url_for_receiving_cookies, user_profile, cookies_file


def main():
    rewards_farmer.save_cookies()

    while True:
        responce = rewards_farmer.farm_points(proxies=True)
        get_title(responce)
        get_ballance(responce)
        time.sleep(randint(3500, 3650) * 2)
        



if __name__ == "__main__":
    rewards_farmer = Farmer(url_for_bing_requests=url_for_bing_requests,
                            url_for_receiving_cookies=url_for_receiving_cookies,
                            user_profile=user_profile,
                            cookies_file=cookies_file)
    main()
    
from bs4 import BeautifulSoup         
from core.loggers import logger  


def get_title(response) -> None:

    if response.status_code == 200:
        logger.info(f'Код: {response.status_code}')

        soup = BeautifulSoup(response.content, 'html.parser')

        h2_tags = soup.find_all('h2')

        result = []

        for tag in h2_tags:
            result.append(tag.text)
        logger.info(f'Кол-во заголовков на странице: {len(result)}')
    else:
        logger.error(f"Не удалось загрузить страницу. Статус код: {response.status_code}")


def get_ballance(response) -> None:

    soup = BeautifulSoup(response.content, 'html.parser')

    span_element = soup.find('span', class_='serp', attrs={'data-priority': '', 'id': 'id_rc'})

    if span_element:
        logger.info(f"Ballance: {span_element.text}")
    else:
        logger.error('Балланс не найден')


def save_html(response) -> None:
    with open('page.html', 'w', encoding='utf-8') as file:
        file.write(response.text)
    logger.info("Страница успешно сохранена в 'page.html'")
from selenium import webdriver
import os
import time
import logging


def make_screenshot(link, index):
    """Загружаем страницу и делаем скриншот. """

    driver = webdriver.Chrome()
    driver.get(link)
    driver.maximize_window()
    time.sleep(3)
    driver.save_screenshot(f'scrins/{index}.png')

    # Закрываем браузер
    driver.quit()


if __name__ == '__main__':
    # Открываем файл со списком ссылок
    with open('urls.txt', 'r') as f:
        links = f.readlines()

    # Создаем директорию для сохранения скриншотов
    if not os.path.exists('scrins'):
        os.makedirs('scrins')

    # Настройка логирования
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s'
    )

    # Проходим по каждой ссылке из списка
    for i, link in enumerate(links):
        # Удаляем символ переноса строки в конце строки
        link = link.strip()

        # Записываем в лог от какой ссылки начали искать скриншоты
        logging.info(f"Ссылка № {i + 1}: {link}")

        try:
            make_screenshot(link, i+1)
            logging.info(f"Скриншот для ссылки № {i + 1} успешно сохранен")
        except Exception as e:
            logging.error(f"Ошибка при обработке ссылки № {i+1}: {e}")

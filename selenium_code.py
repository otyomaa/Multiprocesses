import random
import time
from datetime import datetime

from sql import connection, cursor

from request import url, arr_links

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def collect_profile(profile_id):
    """ Создаем объект драйвера для браузера """
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    print(f"Начало сессии для профиля")

    """ Получаем случайную ссылку из массива и прокручиваем страницу с задержкой """
    random_link = random.choice(arr_links())
    driver.get(url + random_link)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

    """ Собираем куки со страницы """
    cookies = driver.get_cookies()

    """ Добавляем значение куки в базу данных """
    if cookies is not None:
        iters = 0
        for cookie in cookies:
            print(f"Добавление cookie для id {iters} в cookie_value")
            cookie_value = cookie['value']
            datetime_now = datetime.now()
            cursor.execute('update Cookie_Profile SET last_launch = created_at, cookie_value = ?, created_at = ?, '
                           'total_launch = total_launch + 1 WHERE main.Cookie_Profile.id = ?',
                           (cookie_value, datetime_now, iters))
            iters += 1
            connection.commit()

    driver.quit()
    print("Конец сессии")
    print("Данные обновлены")

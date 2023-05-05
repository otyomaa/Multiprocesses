from multiprocessing import Pool
from sql import connection
from selenium_code import collect_profile


if __name__ == '__main__':
    """ Собираем профиль из таблицы Cookie Profile и запускаем процессы """
    profile_id = range(1, 6)     # список идентификаторов профилей
    with Pool(len(profile_id)) as pool:
        pool.map(collect_profile, profile_id)

    connection.close()
    print("Деактивация базы данных")

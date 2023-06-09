# Multiprocesses

Проект Multiprocesses - это инструмент для сбора cookie-файлов с веб-страниц при помощи мультипроцессинга. Данный проект предоставляет возможность собирать cookie-файлы с использованием нескольких профилей и сохранять их в базе данных SQLite. В проекте реализовано несколько функций, которые облегчают сбор cookie-файлов и хранение их в базе данных.

## Установка

Программа написана на языке Python 3. Для установки необходимо скачать файлы из репозитория:

`git clone https://github.com/otyomaa/Multiprocesses.git`

и установить зависимости, выполнив следующую команду:

`pip install -r requirements.txt`

## Использование

Затем можно запустить сбор cookie-файлов, указав идентификаторы профилей в файле multiprocesses.py. Для этого нужно выполнить следующую команду:

`python multiprocesses.py`

## Конфигурация

Конфигурация программы осуществляется через файл config.py. В этом файле можно задать следующие параметры:

PROFILE_ID - количество процессов, которые будут использоваться для сбора cookie-файлов.

## Результаты

Результаты сбора cookie-файлов сохраняются в базу данных SQLite. Для просмотра результатов можно использовать любой SQL-клиент, например, [DB Browser for SQLite](https://sqlitebrowser.org/).

## Лицензия

Программа распространяется под лицензией MIT. Подробную информацию о лицензии можно найти в файле LICENSE.

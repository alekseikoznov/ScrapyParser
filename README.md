# Проект ScrapyParser

## Описание проекта:

Проект **ScrapyParser** является парсером, который предназначен для сбора актуальной информации о стандартах PEP (Python Enhancement Proposals) с помощью фреймворка Scrapy.<br>
Он позволяет получить данные о статусе, названии и номере каждого PEP.

### Принцип работы проекта:

Сбор данных ведется с сайта: [Стандарты PEP (Python Enhancement Proposals)](https://peps.python.org/).<br>
После первого запуска парсера создается директория `results/`. В нее будут сохраняться результаты работы парсера.<br>
По завершению работы парсера создаются два csv файла:
- В первом собраны все PEP с номером, названием и статусом;
- Во втором собрано количество каждого статуса и общее количество PEP.

## Технологии проекта:

- Python 3.9
- Scrapy 2.5.1

## Установка:

Для установки проекта на локальной машине необходимо:

1. Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:alekseikoznov/ScrapyParser.git
```
```
cd ScrapyParser
```
2. Cоздать и активировать виртуальное окружение:
```
python -m venv venv
```
* Если у вас Linux/macOS
    ```
    source venv/bin/activate
    ```
* Если у вас Windows
    ```
    source venv/scripts/activate
    ```
3. Обновить менеджер пакетов pip:
```
python -m pip install --upgrade pip
```
4. Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
5. Запустить парсер:
```
scrapy crawl pep
```

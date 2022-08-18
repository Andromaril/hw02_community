# backend_community_homework

[![CI](https://github.com/yandex-praktikum/hw02_community/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/yandex-praktikum/hw02_community/actions/workflows/python-app.yml)

Учебный проект yatube, репозиторий для сдачи на ревью

Создано и зарегистрировано приложение Posts.

Подключена база данных.

Десять последних записей выводятся на главную страницу.

В админ-зоне доступно управление объектами модели Post: можно публиковать новые записи или редактировать/удалять существующие.

Пользователь может перейти на страницу любого сообщества, где отображаются десять последних публикаций из этой группы.

<h2>Как запустить проект:</h2>
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Andromaril/hw02_community.git
```

Cоздать и активировать виртуальное окружение:

```
1. python3 -m venv env
2. source env/bin/activate
```

Установить зависимости из файла requirements.txt:*

```
1.python3 -m pip install --upgrade pip
2. pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

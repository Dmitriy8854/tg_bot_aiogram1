# tg_bot_aiogram1
source venv/Scripts/activate
Проект Yatube
Yatube - социальная сеть для публикации личных дневников.

Авторы:
Морозов Дмитрий
С помощью этого проекта можно:
Публиковать посты и личные дневники
Создать свою страницу, если на нее зайти, то можно посмотреть все записи автора.
Заходить на чужие страницы, подписываться на авторов и комментировать их записи
Модерировать записи и блокировать пользователей, если начнут присылать спам
Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

git clone git@github.com:Dmitriy8854/hw05_final.git
cd hw05_final
Cоздать и активировать виртуальное окружение:

python -m venv venv
source venv/bin/activate
Установить зависимости из файла requirements.txt:

python -m pip install --upgrade pip
pip install -r requirements.txt
Создать и выполнить миграции:

python3 manage.py makemigrations
python3 manage.py migrate
Заполнить базу тестовой информацией:

python manage.py closereviews
Запустить проект:

python3 manage.py runserver
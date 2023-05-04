# tg_bot_aiogram1

Проект еще не закончен, находится на стадии разработки

```
Телеграм-бот на Aiogram

```
Что может может Телеграм-бот на данный момент:
Отпралять рандомные фото котов по команде "кот"
Отправлять погоду в разных городах по команде - название города, например "Moscow" 
Создавать опросник по команде "srart1"

```
Как запустить проект:

```
Клонировать репозиторий и перейти в него в командной строке:

```
git@github.com:Dmitriy8854/tg_bot_aiogram1.git
cd tg_bot_aiogram1
Cоздать и активировать виртуальное окружение:

```
python -m venv venv
source venv/bin/activate

```
Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
pip install -r requirements.txt

```
Создать и выполнить миграции:

```
python3 manage.py makemigrations
python3 manage.py migrate

```
Запустить проект:

```
python3 manage.py runserver

```
### **Автор:**
- [Морозов Дмитрий]
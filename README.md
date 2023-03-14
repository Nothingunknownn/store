# Django Store 

Ознакомительный проект. Акцент сделан на back-end.

#### Stack:

- [Python](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/)
- [Redis](https://redis.io/)
- [Celery](https://docs.celeryq.dev/en/stable/index.html)

## Local Developing

Все действия должны выполняться из исходного каталога проекта и только после установки всех требований.

1. Во-первых, создать и активировать виртуальное окружение:
   ```bash
   python3 -m venv ../venv
   source ../venv/bin/activate
   ```
   
2. Установить пакеты:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
   
3. Создать .env файл со своими переменными
   
4. Запустите зависимости проекта, миграции, заполните базу данных необходимыми данными и т.д.(Для этого в проекте предусмотрены фикстуры):
   ```bash
   ./manage.py migrate
   ./manage.py loaddata <path_to_fixture_files>
   ./manage.py runserver 
   ```
   
5. Запустите [Redis Server](https://redis.io/docs/getting-started/installation/):
   ```bash
   redis-server
   ```
   
6. Запустите Celery:
   ```bash
   celery -A store worker --loglevel=INFO
   ```
   
## Реализовано
- Регистрация/Аутентификация
- Email верификация
- Возможность регистрации через GitHub
- Возможность оплаты через платежную систему Stripe
- Реализована корзина в профиле пользователя

## Планируется
- Добавить способы регистрации через: Google, VK, Facebook
- Перенести корзину из профиля пользователя на отдельную страницу
- Покрыть код большим колличеством тестов

## Задеплоенная версия 
http://80.249.144.11/

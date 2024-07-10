# City Shop API

## Описание проекта

### Подготовительные действия

1. Клонируйте репозиторий.
2. Установите зависимости:
    ```bash
    pip install django djangorestframework
    ```

3. Создание БД:
    ```bash
    К примеру через Pgadmin4 city_shop_bd
    django-admin startproject city_shop
    cd city_shop
    python manage.py startapp api
    ```

4. Настройка базы данных в settings.py:
   ```python
   # Открыть файл settings.py и настроить соединение с PostgreSQL:
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'city_shop_db',     # Имя вашей базы данных
           'USER': 'postgres',         # Имя пользователя, по умолчанию postgres
           'PASSWORD': 'your_password',# Ваш пароль
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }

# city_shop
# City Shop API

## Описание проекта
## Подготовительные действия

1. Клонируйте репозиторий.
2. Установите зависимости:
    ```bash
   pip install django djangorestframework
    ```
3. Создание БД:
    К примеру через Pgadmin4 city_shop_bd
   django-admin startproject city_shop
   cd city_shop
   python manage.py startapp api

4. Настройка базы данных в settings.py:
Открыть файл settings.py и настроить соединение с PostgreSQL:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'city_shop_db',  # Имя вашей базы данных
        'USER': 'postgres',  # Имя пользователя, по умолчанию postgres
        'PASSWORD': 'your_password',  # Ваш пароль
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

5. Добавление приложений в INSTALLED_APPS:
    INSTALLED_APPS = [.....,'rest_framework','api',]
   
6. Создание моделей и миграций:
    python manage.py makemigrations
    python manage.py migrate
    
7. Создайте суперпользователя:
    
    python manage.py createsuperuser
    
8. Запуск сервера:
    
    python manage.py runserver
   
## Информация о доступах

Для доступа к административной панели использовать созданного суперпользователя.



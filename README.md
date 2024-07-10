# City Shop API
Реализовать сервис, который принимает и отвечает на НТТР запросы №2 
## Описание проекта
Функционал: 
1. В случае успешной обработки сервис должен 
отвечать статусом 200, в случае любой ошибки статус 400. 
2. Сохранение всех объектов в базе данных. 
3. Запросы: 
GET /city/ — получение всех городов из базы; 
GET /city//street/ — получение всех улиц города; 
(city_id - идентификатор города) 
• РОЅT/shop/ — создание магазина; Данный метод 
получает json с объектом магазина, в ответ 
возвращает id созданной записи. 
GET/shop/?street=&city=&open=0/1 - получение 
списка магазинов; 

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
5. Создание моделей и миграций:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
6. Создайте суперпользователя:
    ```bash
    python manage.py createsuperuser
    ``` 
7. Запуск сервера:
    ```bash
    python manage.py runserver
    ```

   

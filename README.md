# Проект university_storaging

## Проектная работа на тему "Университет Синергия. Складские операции"


### запуск приложения

Создаем файл окружения по примеру environment.example
```
ln -s environment.example environment
```

```
docker-compose up --build
```

Создаем пользователя

```
docker-compose run --rm backend ./manage.py createsuperuser
```
### Приложение доступно по адресу: http://localhost:8000/warehouses/


### админка доступна по адресу: http://localhost:8000/admin/


```
python manage.py makemigrations
docker-compose run --rm backend  sh -c "python manage.py migrate"
```

В приложении можно создавать, удалять и редактировать склады, типы хранения и грузы.

Создана таска get_the_quote_of_the_day, которая запускается через celery/celery-beat.
Задача запускается по расписанию через каждую минуту и забирает из открытого апи рандомную цитату,
и кладет в БД. А потом отдается в статический шаблон страницы index через функцию quote_of_the_day.

# DRAFT: Тестирование на проекте


### тесты
```
docker-compose run --rm  backend pytest
```
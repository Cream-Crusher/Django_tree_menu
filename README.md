# Tree menu

[Задание](https://drive.google.com/file/d/1Gr2j5_CmCtxdYaJEy4wW4cB1jGlREpQD/view?usp=drive_link)

## Стэк
* Python 3.10
* Django 4.2.4
* PostgreSQL 15.2
* django-silk 5.0.4

## Запуск

### Clone repo
```git clone git@github.com:Cream-Crusher/Django_tree_menu.git```
### Install dependencies
A. Linux:
  1. ```pip install -r requirements.txt```

B. Windows:
  1. Replace ```psycopg2-binary==2.9.7``` with ```psycopg2==2.9.7``` in **requirements.txt**
  2. ```pip install -r requirements.txt```
### Connect PostgreSQL database
1. Create new database ```%db_name%```
2. Create new file **.env**
3. Edit **.env**:
```
DB_HOST=localhost # default: localhost
DB_NAME=%db_name%
DB_USER=username
DB_PASS=password
```


### Apply migrations
```python3 manage.py migrate```

```python3 manage.py makemigrations```

### Run server
```python3 manage.py runserver```

### Добавление новых веток дерева.

- Создать супер пользователся 
```
python3 manage.py createsuperuser
```
- [Зайти в админку](http://127.0.0.1:8000/admin).
- ```http://127.0.0.1:8000/admin```
Важно: сайт должен быть запущен(См выше)

- отредактировать данные в модели TreeNode

- Ваши изменения перекочуют на меню дерева

Реализована расширенная CMS на основе
админ-панели Django.


## Особенности реализации
### Сущностные классы:
* TreeNode

### Функционал:
Древидное меню: Реализовано древидное меню где каждый *GET*-запрос ```/{id}/``` отвечате за свою ветку.

## Оптимизации
1. Подключен silk для профилирования запросов.
2. Для оптимизации количества запросов они вызываются напрямую (Чистый SQL) к БД.

# Tree menu

[Задание](https://drive.google.com/file/d/1Gr2j5_CmCtxdYaJEy4wW4cB1jGlREpQD/view?usp=drive_link)

## Стэк
* Python 3.10
* Django 4.2.4
* PostgreSQL 15.2

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

## Особенности реализации
### Сущностные классы:
* TreeNode

### Функционал:
Древидное меню: Реализовано древидное меню где каждый *GET*-запрос ```/{id}/``` отвечате за свою ветку.

## Оптимизации
1. Повторные запросы к БД оптимизированы через базовый функционал django+python(плоский функционал), а именно: **prefetch_related**, **select_related**. Для дальнейшей оптимизации необходимо использовать более гибкие  инструменты за рамками ТЗ.
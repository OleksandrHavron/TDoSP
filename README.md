# TDoSP

### Python
    Версія Python == 3.9.1  

[Посилання на завантаження](https://www.python.org/downloads/release/python-391/)  

*При встановленні поставте галочку біля пункта 'Add Python 3.9.1 to PATH'.
Для того, щоб ви могли запускати скрипти використовуючи слово "python",
якщо не поставите прийдеться вказувать повний шлях до інтерпретатора.

### Django
    Версія Django == 3.1.7

###### Встановлення:
В командній строці Windows виконати команду:  
    
    pip install Django==3.1.7

###### Запуск сервера:
В папці де знаходиться файл manage.py виконати команду:  
    
    python manage.py runserver

якщо при встановленні не поставили галочку біля пункта Add Python 3.9.1 to PATH
тоді замість 'python' вказується повний шлях до інтерпретатора Python:  

    /шлях_до_папки_Python/python.exe manage.py runserver

### MySQL:
- MySQL version >= 5.6
- MySQL Connector/Python
  
###### Створення БД: 

	create database tdosp
###### Створення користувача:

    create user 'django'@'localhost' identified by 'djangopswd';
    grant all privileges on tdosp.* to 'django'@'localhost';
    flush privileges;


###### Python:
	pip install mysqlclient==2.0.3
####
    python manage.py makemigrations
    python manage.py migrate
            



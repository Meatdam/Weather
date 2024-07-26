# Приложение "Weather" прогноз погоды
_____

Данное приложение служит для просмотра погоды в любом городе, который вводит пользователь.<br>
Чтобы пользоваться приложением, необходимо зарагестрироваться, авторизироваться и начать пользоваться приложением.<br>
Довольно простой интерфейс, пользователь вводит в форму город, в котором хочет узнать погоду, и она отображаеется с боку формы.<br>
Данные хранятся в БД PostgreSQL, пользователь в любое время может удалить данные у себя на странице.<br>
Отображение погоды отображаются только владельцам запросов и все запросы отображаются у суперпользователя.<br>
Так же пользователь может запросить API (json файл) со всеми пользователями, которые запрашивали когда либо погоду.<br>
Можно обратиться к документации, перед этим запустить проект 
```
python manage.py runserver
```
Затем в адресе 
```
http://127.0.0.1:8000
```
добавить 
```
http://127.0.0.1:8000/swagger/
```
После, вас перебросит на документацию по запросам к Json файлам. 
_____

Приложение выполнено на Django и Django REST framework<br>
## Стек:<br>
- Django;
- Django REST framework;
- Django-filter;
- psycopg2 (ORM);
- Unittest;
- Swagger;
- redoc.
_____
Данное приложение работает на взаимодействие через внешний API-погоды `https://openweathermap.org/`.<br>
____
Приложение протестировано через встроеную библиотеку `Unittest`
_____
Для запуска проекта у себя локально без Docker необходимо:
1. git clone репозитория
```
git@github.com:Meatdam/Weather.git
```
2. Установить виртуальное окружение `venv`
```
python3 -m venv venv для MacOS и Linux систем
python -m venv venv для windows
```
3. Активировать виртуальное окружение
```
source venv/bin/activate для MasOs и Linux систем
venv\Scripts\activate.bat для windows
```
4. установить файл с зависимостями
```
pip install -r requirements.txt
```
4. Создать базу данных в ```PgAdmin```, либо через терминал. Необходимо дать название в файле settings.py в каталоге 'base' в константе (словаре) 'DATABASES'
5. Заполнить своими данными файл .env в корне вашего проекта. Образец файла лежит в корне .env.example
### Я оставил свой API, в случае если вы не захотите регестрироваться на сайте https://openweathermap.org/. Можете воспользоваться моим.
6. Для запуска проекта использовать команду
```
python manage.py runserver
```
7. Для создания суперпользователя, необходимо выполнить команду в консоле
```
python manage.py csu
```
Но при этом не забудьте добавить в .env файл АDMIN_EMAIL, любой email для суперпользователя, чтоб заходить могли по заданному email.<br>
____
Для запуска проекта с принимением Docker:
1. Повторит шаги 1-3;
2. Запустить Docker у себя локально;
3. Выполнить команду в терминале
```
docker compose up -d --build
```
4. Для удаления контейнеров выполните команду
```
docker compose down
```
____

Автор проекта:<br>
[Кузькин Илья](https://github.com/Meatdam)

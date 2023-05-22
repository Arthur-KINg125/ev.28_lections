# postgreSQL - система управления БД(СУБД/DBMS)
# Это ряд программ и инструментов позволяюших соэдавать БД, управлять ею и манипулировать данными 
# внутри(CRUD)

# Postgres - сама база данных, она объектно-реляционная, то есть данные хранятся в виде таблиц и 
# таблицы имеют связи мужду собой

# SQL(Structured Query Language) - декларированный язык структурированных запросов, он применяктся 
# для создания и получения данных при помощи БД 



# ----------------
# команда для входа в бд через юзера postgres:
# sudo -u postgres psql

# команда для входа
# exit

# команда для входа в своего юзера
# psql

# команда для выхода
# \q

# команда для Суперюзера
# CREATE ROLE 'username' SUPERUSER LOGIN PASSWORD '1';

# команда для Суперюзера
# ALTER USER 'username' WITH PASSWORD '1'

# create DATABASE 'name'; #создание бд

# \l - список всех бд

# \du - все юзеры

# \dt - все таблицы (нужно подключиться к бд заранее)

# \d 'name' - подробная инфо. про таблицу(нужно подключиться к БД)

# \c 'name' - # команда для подключения к бд
# 
# psql -U <username> -d <dbname> -подключаемся под выбранным username к dbname 

# -------------------------------------------
#Типы полей в Postgres

# Numeric types(Числовые типы):

    # a. smallint(2 bytes) -> -32767 to 32767
    # b. integer(4 bytes) -> -2.147... to 2.147...
    # c. bigint(8 bytes) -> ... to ...
    # d. real(4 bytes) -> число с плавающей точкой, вещественное число
    # e. double precsion(8 bytes) -> тот же реал, но с двойной точностью
    # f. serial(4 bytes) -> integer, auto-increment

# Character types(Строковые типы):


    # a. varchar(кол-во символов) -> если мы укажем 50 символов, а заполним, только 10, то остальные будут свобоными. Макс 255
    # char(кол-во символов) -> если мы укажем 50 символов, а заполним, только 10, то остальные будут заполнены пробелом. Макс 255
    # 'john'
    # 'john_____'

# Boolen Type
    # a. boolean(1 bytes) -> True/False

# date -> календарная дата(Год.Месяц.День)

# location -> координатная точка(x, y) - (245, -12)

# enumerate Types:
    # ('a', 'b', 'c')
    # CREATE Type <any name> AS ENUM('Happy', 'Sad', 'Mad')

# -----------------------------------
# Команда для создания таблицы  
# Create TABLE <TableName> (
    # films_db=# CREATE TABLE films (
    # code char(5),
    # title varchar(100),
    # date date,
    # genre varchar(50),
    # budget integer,
    # country varchar(50),
    # id serial
    # );

# Комадна для добавления данных в таблицу
# INSERT INTO <tablename> [(columns)] Values (data), (data);

# INSERT INTO films (code, title, date, genre, budget, country) VALUES
# ('AU56', 'Game of Thrones', '2015-05-31', 'Fantasy', '1000000', 'USA')

# Команда для получения данных

# SELECT (columns)* FROM <table>;

# Команда для обновления данных 
# UPDATE <table> SET <column> = <new_value> WHERE <column> = <value>;

# Команда для удаления данных 
# DELETE FROM <table> WHERE <column> = <value>;

# ORDER BY: Позволяет нам сортировать выдящие данные по убыванию или возрастанию.  ASC(по возрастанию) и DESC(По убыванию)
# Синтаксис: SELECT <row> FROM <tablename> ORDER BY <row> [ASC/DESC];

# WHERE: используется для филтрации по полям. Будут выводится только те данные, которые будут соответствовать условию оператора WHERE.
# Синтаксис: SELECT <row> FROM <tablename> WHERE <row> = 'чему либо'

# BETWEEN; условие между
# SELECT * FROM products WHERE id BETWEEN 3 and 8

# LIKE: выводит результат, который соответсвует введенному шаблону для строк. Чувствителен к регистру
# ILIKE: тоже самое только не зависит от регистра
# Синтаксис: SELECT <row> FROM <tablename> WHERE <row> LIKE/ILIKE 'чему либо';

# AND оператор и, для множетвенных условий 
# IN: WHERE <row> in (1, 2, 3, 4);

# LIMIT: ставит ограничение в кол-во получаемых данных

# Экспорт базы данных(Дамп):
# pg_dump -U <username> -d 'dbname' > 'file.sql'

# Импорт:
# psql -U <username> -d <dbname> -f <filename>

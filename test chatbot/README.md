Учебный проект создание бота для тестирования пользователей.

https://t.me/HermeusMoraBot для просмотра команд введите /start

### Запуск проекта

Внесите при необходимости корректировки в переменные окружения (config.py).

TOKEN_TG - телеграм токен

NAME_BOT = имя бота

DATABASE_NAME = файл бд

### Создание и активация виртуального окружения

```bash
sudo apt install python3-venv
python3 -m venv env-name
source env-name/bin/activate
```

### Дополнительные библиотеки

Дополнительные бибилотеки указаны в requirements.txt

```bash
pip install -r requirements.txt 
```

### Инициализация проекта

Обычный режим
```bash
python main.py
```
Фоновой режим
```bash
nohup python -u main.py > name-log.log 2 >&1 &
```

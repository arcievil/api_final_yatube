<<<<<<< HEAD

=======
# API_Yatube

REST API для социальной сети блогеров, созданной в рамках учебного курса Яндекс.Практикум

Аутентификация по JWT-токену Работает со всеми модулями социальной сети Yatube: постами, 

комментариями, группами, подписчиками. Поддерживает методы GET, POST, PUT, PATCH, DELETE

Предоставляет данные в формате JSON


## Последовательность шагов по запуску проекта:

### Клонировать репозиторий:
```
git clone git@github.com:arcievil/api_final_yatube.git
```
### Перейти на репозиторий в командной строке:
```
cd api_final_yatube
```
### Cоздать  виртуальное окружение:
```
python3 -m venv venv
```
### Активировать виртуальное окружение:
```
venv/Scripts/activate
```
### Установить пакетный менеджер для языка программирования Python:
```
python -m pip install --upgrade pip
```
### Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
### При необходимиоста создать миграции:
```
python manage.py makemigrations
```
### Выполнить миграции:
```
python manage.py migrate
```
### Запустить проект:
```
python manage.py runserver
```

### После запуска проекта можно приступать к работе:

## Пару Примеров работы с API_Yatube:

### Пример POST-запроса: добавление нового поста в приложении postman:

### POST .../api/v1/posts/

```
{
    "text": "текст текст",
    "group": 1
} 
```

### Ответ API_Yatube:

```
{
    "id": 14,
    "text": "текст текст",
    "author": "<author username>",
    "image": null,
    "group": 1,
    "pub_date": "2021-06-01T08:47:11.084589Z"
} 
```
### Пример GET-запроса: получаем информацию о группе. в приложении postman:

```
GET .../api/v1/groups/2/
```
### Ответ API_Yatube:
```
{
    "id": 2,
    "title": "Математика",
    "slug": "math",
    "description": "Посты на тему математики"
}
```

## Использованные технологии:

```
python 3.7
django 2.2.16
django rest framework 3.12.4
django-filter 21.1
djoser 2.1.0
```


## Автор:
### Владимир Наумчук
email: arcievil@gmail.com



>>>>>>> 967b0a1ac17bb38ffb8cfec993c08319cec9f7ab

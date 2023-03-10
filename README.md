# Проект API_yatube

## Описание проекта:
Данный проект - это реализация API частичного функционала для социальной сети, включающий в себя создание постов, групп, комментариев к постам. Также частично реализован функционал подписки на других пользователей.

## Как запустить проект:
- Клонируем репозиторий: 
```
git clone git@github.com:Kapshtak/api_final_yatube.git
```
- Переходим в папку с проектом:
```
cd api_final_yatube
```
- Создаем и активируем виртуальное окружение:
``` 
python3 -m venv venv
source venv/bin/activate
```
- Устанавливаем необходимые зависимости:
```
pip install -r requirements.txt
```
- Переходим в следующую папку:
```
cd yatube_api
```
- Создаем таблицы в базе данных:
```
python3 manage.py migrate
```
- Запускаем проект:
```
python3 manage.py runserver
```
## Список эндпойнтов:
- http://127.0.0.1:8000/api/v1/posts/
- http://127.0.0.1:8000/api/v1/groups/
- http://127.0.0.1:8000/api/v1/follow/
- http://127.0.0.1:8000/api/jwt

## Примеры запросов и ответов API:
### POST-запрос на создание поста:
- Запрос:
```
{
    "text": "new post"
}
```
- Ответ:
```
{
    "id": 1,
    "author": "admin",
    "text": "new post",
    "pub_date": "2023-03-10T19:44:51.360599Z",
    "image": null,
    "group": null
}
```
### POST-запрос на создание комментария:
- Запрос:
```
{
    "text": "new post"
}
```
- Ответ:
```
{
    "id": 1,
    "author": "admin",
    "text": "new comment",
    "created": "2023-03-10T19:48:09.068035Z",
    "post": 1
}
```
### POST-запрос на подписку на другого пользователя:
- Запрос:
```
{
    "following": "user"
}
```
- Ответ:
```
{
    "user": "admin",
    "following": "user"
}
```
## Автор проекта

Арсений Капштык
- [Github](https://github.com/Kapshtak) 
- [LinkedIn](https://www.linkedin.com/in/arseniiy-kapshtyk-408a1a253/)
# Project API_yatube

## Project description:
This project is an API implementation of partial functionality for a social network, including creating posts, groups, comments on posts. The functionality of subscribing to other users is also partially implemented.

## How to start a project:
- Clone the repository: 
```
git clone git@github.com:Kapshtyk/api_final_yatube.git
```
- Go to the project folder:
```
cd api_final_yatube
```
- Create and activate the virtual environment:
``` 
python3 -m venv venv
source venv/bin/activate
```
- Install the necessary dependencies:
```
pip install -r requirements.txt
```
- Go to the following folder:
```
cd yatube_api
```
- Create tables in the database:
```
python3 manage.py migrate
```
- Run the project:
```
python3 manage.py runserver
```
## List of endpoints:
- http://127.0.0.1:8000/api/v1/posts/
- http://127.0.0.1:8000/api/v1/groups/
- http://127.0.0.1:8000/api/v1/follow/
- http://127.0.0.1:8000/api/jwt

### Examples of API requests and responses:
### POST request to create a post:
- Request:
```
{
    "text": "new post"
}
```
- Response:
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
### POST request to create a comment:
- Request:
```
{
    "text": "new post"
}
```
- Response:
```
{
    }"id": 1,
    "author": "admin",
    "text": "new comment",
    "created": "2023-03-10T19:48:09.068035Z",
    "post": 1
}
```
### POST request to subscribe to another user:
- Request:
```
{
    "following": "user"
}
```
- Response:
```
{
    "user": "admin",
    "following": "user"
}
```
## Project author

Arseniy Kapshtyk
- [Github](https://github.com/Kapshtyk) 
- [LinkedIn](https://www.linkedin.com/in/kapshtyk)

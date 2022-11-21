# flaskBookAPI
A simple flask REST API which allows us to get , add , update and delete book (books).

## Technologies Used :

- HTML
- CSS
- Python3
- Flask framework
- SQLAlchemy
- SQLITE database

## Operating System

- Linux centos 7

## Dependencies 

- Flask
```
pip install flask
```
- flask_sqlalchemy
```
pip flask_sqlalchemy
```
- functools
```
pip install functools
```

## How To Run The App

1- Get the repository from github :
```
git clone https://github.com/youssefixox/flaskBookAPI.git
```
2- get into the folder and Run the flask application

```
python3 app.py
```

3- If you are using centos 7 in a vm make sure to expose the port of the application for external connections

```
sudo firewall-cmd --add-port=5000/tcp
```

4- Now you can access the documentation of the API via http://<ip>:5000/ .
  
 Note: The API documentation is protected using Basic Authentication . the credentials are admin:admin
  

# Persona API
The Persona API is a fake RESTful API that delivers made up data on a few endpoints.

## Setup
Requires Python 3

#### Create Virtual Environment
```
virtualenv .env
source ./env/bin/active
```

#### Install Dependencies

```
pip install -r requirements.txt
```

#### Run app

```
python3 app.py
```
Test the following endpoints via the Swagger UI at http://127.0.0.1:5000/swagger

GET    http://127.0.0.1:5000/people  

GET    http://127.0.0.1:5000/people/{page}

GET    http://127.0.0.1:5000/search/{username}

DELETE http://127.0.0.1:5000/search/{username}



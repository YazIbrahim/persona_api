# Persona API
The Persona API is a fake RESTful API that delivers made up data on a few endpoints.


## Setup
Requires Python 3


#### Install Dependencies

```
pip install -r requirements.txt
```

#### Run app

During first run the profile data will be unzipped and loaded into the database.
```
python3 app.py
```
Test the following endpoints via the Swagger UI at http://127.0.0.1:5000/swagger

GET    http://127.0.0.1:5000/people  

GET    http://127.0.0.1:5000/people/{page}

GET    http://127.0.0.1:5000/search/{username}

DELETE http://127.0.0.1:5000/search/{username}


#### Run Automated Tests for APIs

```
python3 tests/tests.py
```



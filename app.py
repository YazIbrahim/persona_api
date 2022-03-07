from flask import Flask, json, jsonify
from flask_restful import Api, Resource
import json
import sqlite3
from flask_sqlalchemy import SQLAlchemy
import os.path
from models import populate_db, retrieve_user, delete_person, get_all
from flask_swagger_ui import get_swaggerui_blueprint

persona_app =  Flask(__name__)
persona_api = Api(persona_app)

persona_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Personas.db'

db = SQLAlchemy(persona_app)

# swagger config
swagger_url = '/swagger'
api_url = '/static/swagger.json'

swagger_blueprint = get_swaggerui_blueprint(
    swagger_url,
    api_url,
    config={
        'app_name': "Personas-Flask-REST"
    }
)
persona_app.register_blueprint(swagger_blueprint, url_prefix=swagger_url)


class PersonasModel(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    job = db.Column(db.String(100))
    company = db.Column(db.String(100))
    ssn = db.Column(db.String(20))
    residence = db.Column(db.String(100))
    current_location = db.Column((db.String(100)))
    blood_group = db.Column(db.String(100))
    website = db.Column(db.String(100))
    username = db.Column(db.String(50))
    name = db.Column(db.String(100))
    sex = db.Column(db.String(6))
    address = db.Column(db.String(100))
    mail =  db.Column(db.String(100))
    birthdate = db.Column(db.String(20))

    def __init__(self, job, company, ssn, residence, current_location, blood_group, website, username, name, sex, address, mail, birthdate):
        self.job = job
        self.company = company
        self.ssn = ssn
        self.residence = residence
        self.current_location = current_location
        self.blood_group = blood_group
        self.website= website
        self.username = username
        self.name = name
        self.sex = sex
        self.address = address
        self.mail = mail
        self.birthdate = birthdate
        

class Names(Resource):
    def get(self, username):
        
        username_record = retrieve_user(username, PersonasModel)

        # Return 404 if no record with that usename
        if username_record is None:

                response = jsonify({"Error": "USERNAME NOT"})
                response.status_code = 404
                return response

        response = jsonify(username_record)
        response.status_code = 200
    
        return response
        

    def delete(self, username):

        response_status = delete_person(username, PersonasModel, db)
        
        print(response_status)
        if response_status == 404 :
            response = jsonify({"Error": "Username not found"})
            response.status_code = 404
            return response

        response = jsonify({"Msg": "Profile deleted"})
        response.status_code = 200
        
        return response


class People(Resource):
    def get(self, pages=1):

        total_records = get_all(pages, PersonasModel, db)
        
        # Retrun 404 if no record with that username
        if total_records is None:

                response = jsonify({"error": "Username not found"})
                response.status_code = 404
                return response


        response = jsonify(total_records)
        response.status_code = 200
    
        return response

persona_api.add_resource(Names, "/search/<string:username>")
persona_api.add_resource(People, "/people", "/people/<int:pages>")

if __name__ == "__main__":
    # Create and  populate the database if it does not exist
    if not os.path.isfile('Personas.db'):
        db.create_all()
        print("Loading Database")
        populate_db(db, PersonasModel)
       
    persona_app.run(debug=False)
import zipfile
import json


def populate_db(db, PersonasModel):
        '''Unzips fake profiles and inserts every record into Personas database'''

        #Unzip fake profiles 
        zip = zipfile.ZipFile('fake_profiles.zip')
        zip.extractall('')

        with open('fake_profiles.json') as fake_profiles:
            profiles = json.load(fake_profiles)
            store_profiles = []
            for i in profiles:
                user_entry = PersonasModel(
                    i['job'],
                    i['company'], 
                    i['ssn'], 
                    i['residence'], 
                    " ".join(str(x) for x in i['current_location']), 
                    i['blood_group'],
                    " ".join(str(x) for x in i['website']),
                    i['username'],
                    i['name'],
                    i['sex'],
                    i['address'],
                    i['mail'],
                    i['birthdate'])

                store_profiles.append(user_entry)

            db.session.add_all(store_profiles)
            db.session.commit()


def retrieve_user(username, PersonasModel):
    ''' Retruns data for a single profile based on the username'''
    
    username_data = PersonasModel.query.filter_by(username=username).first()
    if username_data is None:
        return None
    username_dict = username_data.__dict__

    del username_dict['_sa_instance_state']

    return username_dict



def delete_person(username, PersonasModel, db):
    '''Deltes profile for a single person based on the username'''

    x = PersonasModel.query.filter_by(username = username).delete()
    db.session.commit()

    if x  == 0:
        return 404
    

    return None


def get_all(page, PersonasModel, db):

    '''Returns a specified page with 10 records per page'''

    total_records = PersonasModel.query.paginate(page, per_page = 10).items

    if total_records is None:
        return None

    
    

    record_list = []
    for r in total_records:
        record = r.__dict__
        del record['_sa_instance_state']
        record_list.append(record)



    return record_list

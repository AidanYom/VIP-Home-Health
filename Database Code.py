#!/usr/bin/env python
# coding: utf-8

pip install --upgrade firebase-admin
pip install virtualenv

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pandas as pd

if not firebase_admin._apps:
    cred = credentials.Certificate(r'C:\Users\jackk\OneDrive - purdue.edu\Spring 2022\VIP\vip-home-health-1bded1962895.json') 
    default_app = firebase_admin.initialize_app(cred)

# Use a service account
#cred = credentials.Certificate(r'C:\Users\jackk\OneDrive - purdue.edu\Spring 2022\VIP\vip-home-health-1bded1962895.json')
#firebase_admin.initialize_app(cred)

db = firestore.client()

def does_exist(test,request):
    if test == False:
        test = input(f"{request}:")
    return(test)

def Available_dict(Availability):
    av = {}
    if Availability == False:
        week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        for day in week:
            in1 = input(f"Availability on {day} (Seperate times with space and comma)")
            in2 = in1.split(", ")
            av[day] = in2
    return av
    
## ADD FUNCTIONS ##
def add_to_patients(Name = False,Address = False,Zone = False,Specializations = False,Availability = False):
    Name = does_exist(Name,"Patient Name")
    Address = does_exist(Address,"Address")
    Zone = does_exist(Zone,"Zone Location")
    Specializations = does_exist(Specializations,"Speciliazation (Seperate by comma and space)")
    Specializations.split(", ")
    Availability = Available_dict(Availability)
    # Availability input is a dict, not available for input yet
    doc_ref = db.collection(u'Patients').document(Name)    
    doc_ref.set({
    u'Name': Name,
    u'Zone': Zone,
    u'Address' : Address,
    u'Specializations' : Specializations,
    u'Availability' : Availability,
    })

def add_to_nurses(Name = False,Address = False,Zone = False,Health_History = False,Seen = False):
    Name = does_exist(Name,"Nurse Name")
    Address = does_exist(Address,"Address")
    Zone = does_exist(Zone,"Zone Location")
    Health_History = does_exist(Health_History,"Health History (Seperate by comma and space)")
    Health_History.split(", ")
    Seen = does_exist(Seen,"Reason for being seen")
    # Availability input is a dict, not available for input yet
    doc_ref = db.collection(u'Nurses').document(Name)    
    doc_ref.set({
    u'Name': Name,
    u'Zone': Zone,
    u'Address' : Address,
    u'Health History' : Health_History,
    u'Seen' : Seen,
    })
    
def add_to_admins(Name = False,Nurses = False):
    Name = does_exist(Name,"Admin Name")
    Nurses = does_exist(Nurses,"Nurses under Jurisdiction (Separate by comma and a space)")
    Nurses = Nurses.split(", ")
    doc_ref = db.collection(u'Admin').document(Name)    
    doc_ref.set({
    u'Name': Name,
    u'Nurses': Nurses,
    })
        
## REMOVE FUNCTIONS ##
def remove_patient(name) :
    db.collection('patient').document(name).delete()
    print("completed")
    
def remove_nurse(name) :
    db.collection('nurse').document(name).delete()
    print('completed')
    
def remove_admin(name) :
    db.collection('admin').document(name).delete()
    print('completed')
   
## GET FUNCTIONS ##
def get_patients():
    patients = list(db.collection(u'Patients').stream())
    patients_dict = list(map(lambda x: x.to_dict(), patients))
    df = pd.DataFrame(patients_dict)
    return df

def get_nurses():
    patients = list(db.collection(u'Nurses').stream())
    patients_dict = list(map(lambda x: x.to_dict(), patients))
    df = pd.DataFrame(patients_dict)
    return df

def get_admins():
    patients = list(db.collection(u'Admins').stream())
    patients_dict = list(map(lambda x: x.to_dict(), patients))
    df = pd.DataFrame(patients_dict)
    return df

def get_admin(name) :
    result = db.collection('admin').document(name).get()
    if result.exists:
        print(result.to_dict())
    else:
        print("admin doesn't exist")
    
def get_patient(name) :
    result = db.collection('patient').document(name).get()
    if result.exists:
        print(result.to_dict())
    else:
        print("patient doesn't exist")

def get_nurse(name) :
    result = db.collection('nurse').document(name).get()
    if result.exists:
        print(result.to_dict())
    else:
        print("nurse doesn't exist")
        
## EDIT FUNCTIONS ##
def edit_patient(Name = False,Address = False,Zone = False,Health_History = False,HH_Needs = False):
#     Name = does_exist(Name,"Patient Name")
#     Address = does_exist(Address,"Address")
#     Zone = does_exist(Zone,"Zone Location")
#     Specializations = does_exist(Specializations,"Speciliazation (Seperate by comma and space)")
#     Specializations.split(", ")
#     Availability = Available_dict(Availability)
    # Availability input is a dict, not available for input yet
    doc_ref = db.collection(u'Patients').document(Name)
    updates = {}
    if Name:
        updates['Name'] = Name
    
    if Address:
        updates['Address'] = Address
        
    if Zone:
        updates['Zone'] = Zone
    
    if Health_History:
        updates['Health History'] = Health_History
    
    if HH_Needs:
        updates['HH Needs'] = HH_Needs
    
#     return updates
    doc_ref.update(updates)
    
def edit_nurse(Name = False,Address = False,Zone = False,Specializations = False,Availability = False):
#     Name = does_exist(Name,"Nurse Name")
#     Address = does_exist(Address,"Address")
#     Zone = does_exist(Zone,"Zone Location")
#     Health_History = does_exist(Health_History,"Health History (Seperate by comma and space)")
#     Health_History.split(", ")
#     Seen = does_exist(Seen,"Reason for being seen")
    # Availability input is a dict, not available for input yet
    doc_ref = db.collection(u'Patients').document(Name)
    updates = {}
    if Name:
        updates['Name'] = Name
    
    if Address:
        updates['Address'] = Address
        
    if Zone:
        updates['Zone'] = Zone
    
    if Availability:
        updates['Availability'] = Availability
    
    if Specializations:
        updates['Specializations'] = Specializations
    
    doc_ref.update(updates)
    
def edit_admin(Name = False,Nurses=False):
#     Name = does_exist(Name,"Admin Name")
#     Nurses = does_exist(Nurses,"Nurses under Jurisdiction (Separate by comma and a space)")
#     Nurses = Nurses.split(", ")
    doc_ref = db.collection(u'Patients').document(Name)
    updates = {}
    if Name:
        updates['Name'] = Name
    
    if Nurses:
        updates['Nurses'] = Nurses

    doc_ref.update(updates)

    
### PYREBASE AUTHENTICATION ###
import pyrebase

# setting up config for pyrebase initialization
config = {
  'apiKey': "AIzaSyDKl1yhFUxiRUiH0BkJFKhmBfVnIIEyPhU",
  'authDomain': "fir-practice-17cce.firebaseapp.com",
  'databaseURL': "fir-practice-17cce.firebaseio.com",
  'projectId': "fir-practice-17cce",
  'storageBucket': "fir-practice-17cce.appspot.com",
  'messagingSenderId': "527924317355",
  'appId': "1:527924317355:web:a28159a1f040fd311f7bee",
  'measurementId': "G-D6W9MBQEK8"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

class InvalidPasswordException(Exception):
    pass

class InvalidEmailException(Exception):
    pass

class InvalidAdminException(Exception):
    pass

class InvalidNurseException(Exception):
    pass

class InvalidPatientException(Exception):
    pass

# checks username and password to see if valid login
# returns user object if correct, and an error string if not
# error string come in the format such as "INVALID_PASSWORD", "INVALID_EMAIL", etc.
# check out https://firebase.google.com/docs/auth/admin/errors for more error messages
def check_login(emuser, pwd):
    try:
        user = auth.sign_in_with_email_and_password(emuser, pwd)
        return user
    except Exception as e:
        error_json = e.args[1]
        error = json.loads(error_json)['error']['message']
        if error == 'INVALID_PASSWORD':
            raise InvalidPasswordException()
        elif error == 'INVALID_EMAIL':
            raise InvalidEmailException()
        else:
            raise Exception(error)

# creates new user with email and password
# returns user object if correct, and an error string if not
# error string come in the format such as "PASSWORD_TOO_WEAK", "EMAIL_ALREADY_EXISTS", etc.
# check out https://firebase.google.com/docs/auth/admin/errors for more error messages
def make_user(emuser, pwd):
    try:
        user = auth.create_user_with_email_and_password(emuser, pwd)
        return user
    except Exception as e:
        error_json = e.args[1]
        error = json.loads(error_json)['error']['message']
        if error == 'INVALID_PASSWORD':
            raise InvalidPasswordException()
        elif error == 'INVALID_EMAIL':
            raise InvalidEmailException()
        else:
            raise Exception(error)

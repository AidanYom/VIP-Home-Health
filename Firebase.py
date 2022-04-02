import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

if not firebase_admin._apps:
    cred = credentials.Certificate(r'C:\Users\jackk\OneDrive - purdue.edu\Spring 2022\VIP\vip-home-health-1bded1962895.json') 
    default_app = firebase_admin.initialize_app(cred)

# Use a service account
#cred = credentials.Certificate(r'C:\Users\jackk\OneDrive - purdue.edu\Spring 2022\VIP\vip-home-health-1bded1962895.json')
#firebase_admin.initialize_app(cred)

db = firestore.client()
# Create collection containing nurse names, along with first nurses info
doc_ref = db.collection(u'Nurses').document(u'Nurse 1')
doc_ref.set({
    u'first': u'Jack',
    u'middle': u'E',
    u'last': u'Knox',
    u'born': 2001
})

def add_to_nurse():
    Name  = input("Nuse Name: ")
    doc_ref = db.collection(u'Nurses').document(Name)
    Name = Name.split(" ")
    BirthDate = input("Date of Birth (DD/MM/YYYY): ")
    doc_ref.set({
    u'first': Name[0],
    u'last': Name[1],
    u'born': BirthDate
    })
    
def add_to_patients():
    Name  = input("Patient Name: ")
    doc_ref = db.collection(u'Patients').document(Name)
    Name = Name.split(" ")
    BirthDate = input("Date of Birth (DD/MM/YYYY): ")
    Other = []
    i = 'x'
    while i != 'NA':
        i = input("Other Fields for Designated Patient (Enter NA if none/no more): ")
        if i != 'NA':
            y = input("Field Inputs: ")
            Other.append([i,y])
    
    doc_ref.set({
    u'first': Name[0]
    })
    if len(Name) > 2:
        doc_ref.set({
            u'middle': ' '.join(Name[1:(len(Name) - 1)])
        },merge=True)
    doc_ref.set({
    u'last': Name[len(Name)-1],
    u'born': BirthDate
    },merge=True)
    for x in Other:
        doc_ref.set({
            x[0] : x[1]
        },merge=True)
    
       
# add_to_patients()

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

# checks username and password to see if valid login
# returns user object if correct, and an error string if not
# error string come in the format such as "INVALID_PASSWORD", "INVALID_EMAIL", etc.
# check out https://firebase.google.com/docs/auth/admin/errors for more error messages
def check_login(emuser, pwd):
    try:
        user = auth.sign_in_with_email_and_password(emuser, pwd)
    except Exception as e:
        error_json = e.args[1]
        error = json.loads(error_json)['error']
        print(error['message'])
        user = error['message']
    
    return user

# creates new user with email and password
# returns user object if correct, and an error string if not
# error string come in the format such as "PASSWORD_TOO_WEAK", "EMAIL_ALREADY_EXISTS", etc.
# check out https://firebase.google.com/docs/auth/admin/errors for more error messages
def make_user(emuser, pwd):
    try:
        user = auth.create_user_with_email_and_password(emuser, pwd)
    except Exception as e:
        error_json = e.args[1]
        error = json.loads(error_json)['error']
        user = error['message']
    
    return user

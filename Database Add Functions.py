#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install --upgrade firebase-admin


# In[1]:


pip install virtualenv


# In[2]:


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


# In[22]:


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

def add_to_nurse(Name = False,Address = False,Zone = False,Health_History = False,Seen = False):
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
    
def add_to_admin(Name = False,Nurses = False):
    Name = does_exist(Name,"Admin Name")
    Nurses = does_exist(Nurses,"Nurses under Jurisdiction (Separate by comma and a space)")
    Nurses = Nurses.split(", ")
    doc_ref = db.collection(u'Admin').document(Name)    
    doc_ref.set({
    u'Name': Name,
    u'Nurses': Nurses,
    })
        


# In[18]:


add_to_patients()


# In[19]:


add_to_nurse()


# In[21]:


add_to_admin()


# In[ ]:





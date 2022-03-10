#!/usr/bin/env python
# coding: utf-8

# In[6]:


pip install --upgrade firebase-admin


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


# In[25]:


# Create collection containing nurse names, along with first nurses info
doc_ref = db.collection(u'Nurses').document(u'Nurse 1')
doc_ref.set({
    u'first': u'Jack',
    u'middle': u'E',
    u'last': u'Knox',
    u'born': 2001
})


# In[7]:


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


# In[22]:


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
    u'first': Name[0],
    u'last': Name[1],
    u'born': BirthDate
    })
    for x in Other:
        doc_ref.set({
            x[0] : x[1]
        },merge=True)
    
        


# In[24]:


add_to_patients()


# In[ ]:





# In[ ]:





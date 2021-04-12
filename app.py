# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 16:39:02 2021

@author: CarlosCaste
"""


import pyrebase
firebaseConfing= {    "apiKey": "AIzaSyDf672QHogx74CC1GEtASzw7fqBJt5-X0o",
    "authDomain": "fir-tutorial-4b86a.firebaseapp.com",
    "databaseURL": "https://fir-tutorial-4b86a-default-rtdb.firebaseio.com",
    "projectId": "fir-tutorial-4b86a",
    "storageBucket": "fir-tutorial-4b86a.appspot.com",
    "messagingSenderId": "715795541585",
    "appId": "1:715795541585:web:64d9fb455c19d7496a1270",
    "measurementId": "G-8WD2TY33E0"
    
    }
firebase  = pyrebase.pyrebase.initialize_app(firebaseConfing)
db = firebase.database()


from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    sepalLength = db.child("iris").child("sepalLength").get()

    return sepalLength.val()

app.run(debug=True)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__)

db = SQLAlchemy(app)

class appointments(db.Model):
    sno = db.Column(db.Integer, primary_key=True) 
    firstname= db.Column(db.String(80), nullable=False)
    lastname=  db.Column(db.String(80), nullable=False)
    email=  db.Column(db.String(20), nullable=False)
    phonenumber= db.Column(db.String(12), nullable=False)
    issue= db.Column(db.String(200), nullable=False)
    date = db.Column(db.String(12), nullable=True)


class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(200))
    email = db.Column(db.String(200))
    password = db.Column(db.String(200))
    gen=db.Column(db.String(200))
    image=db.Column(db.String(200))


class Doctor(UserMixin,db.Model):
   
    doctorid = db.Column(db.String(200),primary_key=True)
    doctorpwd = db.Column(db.String(200))
    doctorname = db.Column(db.String(200))
    doctorimg = db.Column(db.String(200))
    doctorgen = db.Column(db.String(200))
    doctordesc = db.Column(db.String(200))
    id=db.Column(db.Integer,autoincrement=True)
    
class Contact_us(db.Model):
    sno = db.Column(db.Integer, primary_key=True) 
    email=  db.Column(db.String(20), nullable=False)
    message= db.Column(db.String(200), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    

class Pricing(UserMixin,db.Model):

    pid = db.Column(db.Integer,primary_key=True)
    pname = db.Column(db.String(200))
    pprice= db.Column(db.String(200))
    pvalid= db.Column(db.String(200))



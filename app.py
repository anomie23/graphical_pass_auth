from os import system
from flask import Flask, render_template, session, redirect, request, url_for
from functools import wraps
from passlib.hash import pbkdf2_sha256
import pymongo
import pyrebase
from pymongo import MongoClient




# Database

client = MongoClient("mongodb+srv://Shantha-7:masha2001@shantha-7.hec4h0m.mongodb.net/?retryWrites=true&w=majority")
db = client.passwordlogin


app = Flask(__name__)
app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'

# Decorators
def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return f(*args, **kwargs)
    else:
      return redirect('/')
  
  return wrap

# Routes
from user import routes

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/emosignup/')
@login_required
def emosignup():
  return render_template('emosignup.html')

@app.route('/emologin/')
def emologin():
  return render_template('emologin.html')

@app.route('/flipkart')
def flipkart():
  return redirect("https://www.flipkart.com/")


config = {
    'apiKey': "AIzaSyBu4TRNZNZIYUOdga43shHPqYJ5sOHIoQk",
    'authDomain': "graphauth-c41e0.firebaseapp.com",
    'projectId': "graphauth-c41e0",
    'storageBucket': "graphauth-c41e0.appspot.com",
    'messagingSenderId': "96712945377",
    'appId': "1:96712945377:web:1ffca8ce0a2268e9edd1a0",
    'measurementId': "G-4HBD6BNPCF",
    'databaseURL':"https://graphauth-c41e0-default-rtdb.firebaseio.com/"
}

#initialize firebase
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
dbs = firebase.database()

#Initialze person as dictionary
person = {"is_logged_in": False, "name": "", "email": "", "uid": ""}


#If someone clicks on login, they are redirected to /result
@app.route("/result", methods = ["POST", "GET"])
def result():
    if request.method == "POST":        #Only if data has been posted
        result = request.form           #Get the data
        email = result["email"]
        password = result["pass"]
        try:
            #Try signing in the user with the given information
            user = auth.sign_in_with_email_and_password(email, password)
            #Insert the user data in the global person
            global person
            person["is_logged_in"] = True
            person["email"] = user["email"]
            person["uid"] = user["localId"]
            #Get the name of the user
            data = dbs.child("users").get()
            person["name"] = data.val()[person["uid"]]["name"]
            #Redirect to welcome page
            return redirect("/flipkart")
        except:
            #If there is any error, redirect back to login
            return render_template('emologin.html')


#If someone clicks on register, they are redirected to /register
@app.route("/register", methods = ["POST", "GET"])
def register():
    if request.method == "POST":        #Only listen to POST
        result = request.form           #Get the data submitted
        email = result["email"]
        password = result["pass"]
        name = result["name"]
        try:
            #Try creating the user account using the provided data
            auth.create_user_with_email_and_password(email, password)
            #Login the user
            user = auth.sign_in_with_email_and_password(email, password)
            #Add data to global person
            global person
            person["is_logged_in"] = True
            person["email"] = user["email"]
            person["uid"] = user["localId"]
            person["name"] = name
            #Append data to the firebase realtime database
            data = {"name": name, "email": email}
            dbs.child("users").child(person["uid"]).set(data)
            #Go to welcome page
            return render_template('emologin.html')
        except:
            #If there is any error, redirect to register
            return render_template('emosignup.html')

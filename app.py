from flask import Flask, render_template, request,url_for,flash,redirect,session;
from flask_session import Session
import ibm_db

app=Flask(__name__)

app.config["SESSION_PERMANENT"]=False 
app.config["SESSION_TYPE"]="filesystem"
Session(app)
app.secret_key = "789764532"

conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=19af6446-6171-4641-8aba-9dcff8e1b6ff.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=30699;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=prr47494;PWD=ggtIQb5SN8tno7qc",'','')


@app.route("/")
def signin():
    return render_template('signin.html')

@app.route("/signup")
def signup():
    return render_template('signup.html')  
    
@app.route('/create/',methods=('GET','POST'))
def create():
    if request.method=="POST":
        email=request.form['email']
        password=request.form['password']
        repassword=request.form['repassword']

        if not email:
            flash('Email required')

        elif not password:
            flash('Password is required')
        
        elif not repassword:
            flash('Password is required')

        elif password!=repassword:
            flash('Password did not match')

        else:
            session['email']=email
            session['password']=password
            print(session['email'],session['password'])
            return redirect(url_for("profile"))
            
    return  redirect(url_for("signup"))

@app.route("/profile")
def profile():
    print(session['email'],session['password'])
    return render_template('profile.html')

@app.route("/home")
def home():
    return render_template("home.html")


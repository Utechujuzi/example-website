from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signup')
def signup():
    return render_template('registration.html')

@app.route('/signin')
def signin():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html') 

    app.run(debug=True)
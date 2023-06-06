from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/upload')
def upload():
    redirect('upload_assignment.html')

    app.run(debug=True)
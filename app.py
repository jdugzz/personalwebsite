from flask import Flask, request, render_template, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdfasdf'

@app.route('/')
def go_home():
    return redirect('/home')

@app.route('/home')
def show_home():
    return render_template('homepage.html')

@app.route('/contact')
def show_contact():
    return render_template('contact.html')

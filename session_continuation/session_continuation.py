from flask import Flask, make_response, request, session, g, redirect, url_for, abort, \
     render_template, flash
app = Flask(__name__)

@app.route('/')
def index():
# renders the html index page
   return render_template('index.html')

@app.route('/enter_form')
def enter_form():
# renders the html file
   return render_template('enter_form.html')


@app.route('/save_form', methods = ['POST', 'GET'])
def save_form():
#renders the html file
   return render_template('save_form.html')

@app.route('/reciept')
def reciept():
#renders the html file
   return render_template('reciept.html')

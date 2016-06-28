from flask import Flask, make_response, request, session, g, redirect, url_for, abort, \
     render_template, flash
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/enter_form')
def enter_form():
   return render_template('enter_form.html')


@app.route('/save_form', methods = ['POST', 'GET'])
def save_form():
   if request.method == 'POST':  
      the_username = request.form['user_name']
      the_surname = request.form['user_surname']
      the_card = request.form['card']
      the_address = request.form['address']

      resp = make_response(render_template('save_form.html'))
      resp.set_cookie('username', the_username)
      resp.set_cookie('surname', the_surname)
      resp.set_cookie('card', the_card)
      resp.set_cookie('address', the_address)

      return resp
 
   else:
      return render_template('save_form.html')

@app.route('/reciept')
def reciept():
   username = request.cookies.get('username')
   surname = request.cookies.get('surname')
   card = request.cookies.get('card')
   address = request.cookies.get('address')
   return '<table><tr><td>Name: </td><td> '+username+' </td></tr><tr><td>Surname: </td><td> '+surname+' </td></tr><tr><td> Card Details: </td><td> '+card+'</td></tr><tr><td> Address: </td><td> '+address+' </td></tr></table>'


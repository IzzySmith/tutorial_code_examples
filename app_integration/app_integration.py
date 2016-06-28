from flask import Flask, request, make_response, render_template
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/start')
def start():
   return render_template('start.html')

@app.route('/join')
def join():
   return render_template('join.html')



from flask import Flask, request, make_response, render_template
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/session_id')
def session_id():
   return render_template('session_id.html')


import datetime,pymysql
from flask import Flask, redirect
from flask.templating import render_template
from flask.globals import request

app = Flask(__name__)

@app.route('/')
def init():
    return 'inicio'

@app.route('/home/', methods=['GET'])
def render_template_html():
    return render_template('/home/home.html')



if __name__== '__main__':
    app.run(debug=True)
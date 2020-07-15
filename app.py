import datetime,pymysql
from flask import Flask, redirect
from flask.templating import render_template
from flask.globals import request

from flask.helpers import url_for
app = Flask(__name__)

conexao = pymysql.connect(host='localhost', user='root', password='', db='dbsistema_python')
conexao_cursor = conexao.cursor()

print(conexao_cursor)

@app.route('/')
def init():
    return 'inicio'

@app.route('/home/', methods=['GET'])
def render_template_html():
    return render_template('/home/home.html')

@app.route('/home/cadastrar', methods=['POST'])
def cadastrar_dados():
    return 'Página de Cadastrar'



if __name__== '__main__':
    app.run(debug=True)
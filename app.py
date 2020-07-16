import datetime,pymysql
from flask import Flask, redirect
from flask.templating import render_template
from flask.globals import request

from flask.helpers import url_for
app = Flask(__name__)

conexao = pymysql.connect(host='localhost', user='root', password='', db='dbsistema_python')
conexao_cursor = conexao.cursor()


@app.route('/')
def init():
    return 'Página de login'

@app.route('/home/', methods=['GET'])
def render_template_html():
    return render_template('/home/home.html')

@app.route('/home/cadastrar', methods=['POST'])
def cadastrar_dados():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        senha     = request.form['senha']
        data_criacao = datetime.datetime.now()

        sql_insert = "INSERT INTO usuario(nome, email, telefone, senha,data_criacao) VALUES ('{}','{}','{}','{}','{}')".format(nome, email, telefone, senha, data_criacao)
        conexao_cursor.execute(sql_insert)
        conexao.commit()

    return 'Cadastrado com sucesso'



if __name__== '__main__':
    app.run(debug=True)
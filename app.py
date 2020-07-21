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
"""
@app.route('/home/cadastrar', methods=['POST'])
def cadastrar_usuarios():
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
"""

@app.route('/usuarios/', methods=['GET'])
def formulario_cadastro():
    return render_template('usuarios/cadastrar_usuario.html')

@app.route('/usuarios/criar_usuario', methods=['POST'])
def cadastrar_usuario():

    if request.method == 'POST':
        matricula  = request.form['matricula']
        nome       = request.form['nome']
        cidade     = request.form['cidade']
        cargo      = request.form['cargo']
        email      = request.form['email']
        telefone   = request.form['telefone']
        senha      = request.form['senha']

        sql = """
            INSERT INTO func_user(matricula, nome, cidade, cargo, email, telefone, senha)
            VALUES ('{}','{}','{}','{}','{}','{}','{}')
            """.format(matricula, nome, cidade, cargo, email, telefone, senha)
        row = conexao_cursor.execute(sql)
        conexao.commit()
        if row > 0:
            dados = {'mensagem': 'Cadastro efetuado com sucesso.'}
        else:
            dados = {'mensagem': 'Não foi possível efetuar o cadastro.'}

    return render_template('usuarios/cadastrar_usuario.html', dados=dados)

@app.route("/usuarios/listar", methods=['GET'])
def listar_usuarios():
    select_usuarios = """
      SELECT * FROM usuario
    """
    conexao_cursor.execute(select_usuarios)
    usuarios = conexao_cursor.fetchall()
    #print(usuarios)
    return render_template('usuarios/listar_usuarios.html', usuarios=usuarios)

if __name__== '__main__':
    app.run(debug=True)
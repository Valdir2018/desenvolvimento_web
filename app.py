import datetime,pymysql
from flask import Flask, redirect, json
from flask.templating import render_template
from flask.globals import request
from werkzeug.security import generate_password_hash, check_password_hash
from contextlib import closing
from flaskext.mysql import MySQL
from flask.helpers import url_for



mysql = MySQL()
app = Flask(__name__)


# Config 
app.config['MYSQL_DATABASE_USER'] = 'root';
app.config['MYSQL_DATABASE_PASSWORD'] = '';
app.config['MYSQL_DATABASE_DB'] = 'dbsistema_python';
app.config['MYSQL_DATABASE_HOST'] = 'localhost';
mysql.init_app(app)

with app.app_context():
    cursor = mysql.connect()
    conn = cursor.cursor()   
        

@app.route('/')
def main():
    return render_template('home/index.html')


@app.route('/', methods=['POST'])
def autenticate():
    if request.method == 'POST':
            username  = request.form['login']
            password  = request.form['senha']

            conn.execute("SELECT * FROM func_user WHERE matricula='" + username + " 'and senha='" + password + " ' ")            
            data = conn.fetchone()
            
            if data is None:
                msg = {'error':'Usuario ou senha invalida'}
    
                return msg
            else:
                return render_template('/home/dashboard.html')


        
@app.route('/home/', methods=['GET'])
def render_template_html():
    return render_template('/home/index.html')



@app.route('/usuarios/', methods=['GET'])
def formulario_cadastro():
     return render_template('usuarios/cadastrar_usuario.html')



@app.route('/solicitacao/')
def formulario_solicitacao():
    return render_template('/solicitacao/criar_solicitacao.html')     


@app.route('/solicitacao/criar_solicitacao', methods=['POST','GET'])      
def criar_solicitacao():
    if request.method == 'POST':
        matricula = request.form['matricula']
        print(matricula)
    return 'pagina vazia'



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

        password   = generate_password_hash(senha)

        sql = """
            INSERT INTO func_user(matricula, nome, cidade, cargo, email, telefone, senha)
            VALUES ('{}','{}','{}','{}','{}','{}','{}') 
            """.format(matricula, nome, cidade, cargo, email, telefone, password)
        row = conn.execute(sql)
        cursor.commit()
        if row > 0:
            dados = {'mensagem': 'Cadastro efetuado com sucesso.'}
        else:
            dados = {'mensagem': 'Não foi possível efetuar o cadastro.'}

    return render_template('usuarios/cadastrar_usuario.html', dados=dados)


        
@app.route("/usuarios/listar", methods=['GET'])
def listar_usuarios():
     
     conn.execute("SELECT * FROM func_user")
     usuarios = conn.fetchall()
     return render_template('usuarios/listar_usuarios.html', usuarios=usuarios)
    
        

if __name__ == '__main__':
    app.run(debug=True, port=8000)



    
    
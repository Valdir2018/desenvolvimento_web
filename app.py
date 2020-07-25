import datetime,pymysql
from flask import Flask, redirect, json
from flask.templating import render_template
from flask.globals import request

# from Werkzeug.security import generate_password_hash, check_password_hash
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
    conexao_cursor = mysql.connect().cursor()  
        



# conexao = pymysql.connect(host='localhost', user='root', password='', db='dbsistema_python')
# conexao_cursor = conexao.cursor()

@app.route('/')
def main():
    return render_template('home/index.html')


@app.route('/', methods=['POST'])
def autenticate():
    if request.method == 'POST':
            username  = request.form['login']
            password  = request.form['senha']
            conexao_cursor.execute("SELECT * FROM func_user WHERE matricula='" + username + " 'and senha='" + password + " ' ")
            
            data = conexao_cursor.fetchone()
            print(data.nome)

            if data is None:
                msg = {'error':'Usuario ou senha invalida'}
                print(msg)
                return msg
            else:
                return render_template('/home/dashboard.html')


        
@app.route('/home/', methods=['GET'])
def render_template_html():
    return render_template('/home/index.html')



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
        #conn = conexao_cursor.connect().cursor()    
        row = conn.execute(sql)
        conexao_cursor.commit()
        if row > 0:
            dados = {'mensagem': 'Cadastro efetuado com sucesso.'}
        else:
            dados = {'mensagem': 'Não foi possível efetuar o cadastro.'}

    return render_template('usuarios/cadastrar_usuario.html', dados=dados)


        
@app.route("/usuarios/listar", methods=['GET'])
def listar_usuarios():
     
     conexao_cursor.execute("SELECT * FROM func_user")
     usuarios = conexao_cursor.fetchall()
     return render_template('usuarios/listar_usuarios.html', usuarios=usuarios)
    
        

if __name__ == '__main__':
    app.run(debug=True, port=8000)



    
    
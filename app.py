
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def ola_route():
    nome = 'Abigail'
    techs = ['Python','Html','Css']
    return render_template('index.html',nome_usuario = nome, tecnologias= techs)

@app.route('/sobre/<username>')
def  perfil(username):
    return f'<h2>Perfil de Username {username}</h2>'
    

@app.route('/post/<int:id_user>')
def id_user(id_user):
    return f'<h1>Pegando o ID {id_user}<h1/>'

if __name__ == ('__main__'):
    app.run(debug=True)
    

    

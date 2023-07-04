from flask import Flask, request
from services.empregados import Empregado
from flask_restful import Resource, Api
import json
import os



app = Flask(__name__)
api = Api(app)

# Classe para manipular os dados dos empregados


@app.route('/', methods=['GET'])
def inicial():
    home = Empregado.inicial()
    return home

@app.route('/empregados', methods=['GET'])
def lista_empregados():
    empregados = Empregado.lista_empregados()
    return empregados

@app.route('/create', methods=['POST'])
def novo_empregado():
    novo_empregado = Empregado.create_empregado()
    return novo_empregado


@app.route('/altera/<int:id>', methods=['POST'])
def edita_empregado(id):
    data = request.get_json()
    edita_empregado = Empregado.altera_empregado(id, data)
    return edita_empregado


@app.route('/deleta/<int:id>', methods=['POST'])
def deleta_empregado(id):
    deleta_empregado = Empregado.delete_empregado(id)
    return deleta_empregado


if __name__ == '__main__':
    app.run(debug=True)

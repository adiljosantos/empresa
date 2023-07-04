from flask import Flask, request
import json
import os
import requests


# Classe para manipular os dados dos empregados

class Empregado():


    def inicial():
        saudacao = "Olá"
        return saudacao
    
    @staticmethod
    def status_code():
        url = "http://127.0.0.1:5000"
        response = requests.get(url)
        status = response.status_code
        return status
  

    def lista_empregados():
        # Abre o arquivo empregados.json e retorna os dados como resposta
        with open('./data/empregados.json', 'r') as f:
            empregados = json.load(f)
        return empregados
    
    @staticmethod
    def lista_empregados_paraTeste():
        # Abre o arquivo empregados.json e retorna os dados como resposta
        with open('../data/empregados.json', 'r') as f:
            empregados = json.load(f)
        return empregados
     
    def create_empregado():
        # Lê os dados enviados na requisição
        data = request.get_json()

        # Obtém as informações do empregado
        id = int(data['id'])
        nome = str(data['nome'])
        cargo = str(data['cargo'])
        idade = int(data['idade'])
        salario = float(data['salario'])

        # Verifica se o arquivo empregados.json existe
        if os.path.exists("./data/empregados.json"):
            try:
                # Carrega os dados existentes do arquivo empregados.json
                with open("./data/empregados.json", "r") as arquivo:
                    empregados = json.load(arquivo)
            except json.decoder.JSONDecodeError:
                empregados = {"empregados": []}
        else:
            empregados = {"empregados": []}

        # Adiciona o novo empregado à lista
        novo_empregado = {
            "id": id,
            "nome": nome,
            "cargo": cargo,
            "idade": idade,
            "salario": salario
        }
        empregados["empregados"].append(novo_empregado)

        # Salva os dados no arquivo
        with open("./data/empregados.json", "w") as arquivo:
            json.dump(empregados, arquivo, indent=4) 
        return {'message': 'Empregado adicionado com sucesso'}
    
    @staticmethod
    def create_empregado_paraTeste():
        # Lê os dados enviados na requisição
        data = request.get_json()

        # Obtém as informações do empregado
        id = int(data['id'])
        nome = str(data['nome'])
        cargo = str(data['cargo'])
        idade = int(data['idade'])
        salario = float(data['salario'])

        # Verifica se o arquivo empregados.json existe
        if os.path.exists("../data/empregados.json"):
            try:
                # Carrega os dados existentes do arquivo empregados.json
                with open("../data/empregados.json", "r") as arquivo:
                    empregados = json.load(arquivo)
            except json.decoder.JSONDecodeError:
                empregados = {"empregados": []}
        else:
            empregados = {"empregados": []}

        # Adiciona o novo empregado à lista
        novo_empregado = {
            "id": id,
            "nome": nome,
            "cargo": cargo,
            "idade": idade,
            "salario": salario
        }
        empregados["empregados"].append(novo_empregado)

        # Salva os dados no arquivo
        with open("../data/empregados.json", "w") as arquivo:
            json.dump(empregados, arquivo, indent=4)
        return {'message': 'Empregado adicionado com sucesso'}

    def altera_empregado(empregado_id, empregado_data):
        # Abre o arquivo empregados.json e atualiza os dados do empregado com base no ID fornecido
        with open('../data/empregados.json', 'r') as f:
            empregados = json.load(f)

            # Procura o empregado pelo ID fornecido
            for empregado in empregados['empregados']:
                if empregado['id'] == empregado_id:
                    empregado.update(empregado_data)
                    break

        # Salva os dados atualizados no arquivo
        with open('../data/empregados.json', 'w') as f:
            json.dump(empregados, f, indent=4)

        return {'message': 'Empregado atualizado com sucesso'}

    def altera_empregado(empregado_id, empregado_data):
        # Abre o arquivo empregados.json e atualiza os dados do empregado com base no ID fornecido
        with open('./data/empregados.json', 'r') as f:
            empregados = json.load(f)

            # Procura o empregado pelo ID fornecido
            for empregado in empregados['empregados']:
                if empregado['id'] == empregado_id:
                    empregado.update(empregado_data)
                    break

        # Salva os dados atualizados no arquivo
        with open('./data/empregados.json', 'w') as f:
            json.dump(empregados, f, indent=4)

        return {'message': 'Empregado atualizado com sucesso'}
    
    @staticmethod
    def altera_empregado_paraTeste(empregado_id, empregado_data):
        # Abre o arquivo empregados.json e atualiza os dados do empregado com base no ID fornecido
        with open('../data/empregados.json', 'r') as f:
            empregados = json.load(f)

            # Procura o empregado pelo ID fornecido
            for empregado in empregados['empregados']:
                if empregado['id'] == empregado_id:
                    empregado.update(empregado_data)
                    break

        # Salva os dados atualizados no arquivo
        with open('../data/empregados.json', 'w') as f:
            json.dump(empregados, f, indent=4)

        return {'message': 'Empregado atualizado com sucesso'}    
        
    def delete_empregado(empregado_id):
        # Abre o arquivo empregados.json e remove o empregado com base no ID fornecido
        with open('./data/empregados.json', 'r') as f:
            empregados = json.load(f)

            # Procura o empregado pelo ID fornecido e o remove
            empregados["empregados"] = [empregado for empregado in empregados["empregados"] if empregado['id'] != empregado_id]

        # Salva os dados atualizados no arquivo
        with open('./data/empregados.json', 'w') as f:
            json.dump(empregados, f, indent=4)

        return {'message': 'Empregado excluído com sucesso'}
    
    @staticmethod
    def delete_empregado_paraTeste(empregado_id):
        # Abre o arquivo empregados.json e remove o empregado com base no ID fornecido
        with open('../data/empregados.json', 'r') as f:
            empregados = json.load(f)

            # Procura o empregado pelo ID fornecido e o remove
            empregados["empregados"] = [empregado for empregado in empregados["empregados"] if empregado['id'] != empregado_id]

        # Salva os dados atualizados no arquivo
        with open('../data/empregados.json', 'w') as f:
            json.dump(empregados, f, indent=4)

        return {'message': 'Empregado excluído com sucesso'}
    

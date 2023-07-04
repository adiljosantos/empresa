import unittest
import json
from os.path import dirname, abspath
import sys
import xmlrunner
from unittest.mock import MagicMock

# Obtém o diretório raiz do projeto
diretorio_raiz = dirname(dirname(abspath(__file__)))

# Adiciona o diretório raiz ao caminho de pesquisa de módulos
sys.path.insert(0, diretorio_raiz)

from services.empregados import Empregado




class TestEmpresa(unittest.TestCase):
    """Description of your test cases"""
        
    def test_url_status_code(self):
        response = Empregado.status_code()        
        self.assertEqual(response, 200)        

    def test_retorno_lista(self):
        resultado = Empregado.lista_empregados_paraTeste()
        self.assertIsInstance(resultado, dict, "O retorno não é uma lista")
               
    def test_delete_empregado(self):
        # Chama a função delete_empregado para excluir um empregado
        Empregado.delete_empregado_paraTeste(2)

        # Abre o arquivo empregados.json e verifica se o empregado foi excluído
        with open('../data/empregados.json', 'r') as f:
            empregados = json.load(f)
            empregados_list = empregados["empregados"]

            # Verifica se o empregado com ID 2 foi excluído
            for empregado in empregados_list:
                self.assertNotEqual(empregado["id"], 2)

        # Verifica a mensagem de retorno da função
        expected_message = {'message': 'Empregado excluído com sucesso'}
        self.assertEqual(Empregado.delete_empregado_paraTeste(2), expected_message)
        
    def test_altera_empregado(self):
        # Chama a função altera_empregado_paraTeste para atualizar um empregado
        empregado_id = 3
        empregado_data = {"salario": 3500}
        Empregado.altera_empregado_paraTeste(empregado_id, empregado_data)

        # Abre o arquivo empregados.json e verifica se os dados do empregado foram atualizados
        with open('../data/empregados.json', 'r') as f:
            empregados = json.load(f)
            empregados_list = empregados["empregados"]

            # Verifica se o salário do empregado com ID 2 foi atualizado corretamente
            for empregado in empregados_list:
                if empregado["id"] == empregado_id:
                    self.assertEqual(empregado["salario"], 3500)
                    break

        # Verifica a mensagem de retorno da função
        expected_message = {'message': 'Empregado atualizado com sucesso'}
        self.assertEqual(Empregado.altera_empregado_paraTeste(empregado_id, empregado_data), expected_message)


if __name__ == '__main__':
    # Defina o diretório de saída para o arquivo results.xml
    output_dir = 'test-results'

    # Crie um objeto de descoberta de testes
    test_loader = unittest.TestLoader()

    # Carregue os casos de teste
    test_suite = test_loader.discover('.', pattern='test*.py')

    # Crie o runner XML com o diretório de saída especificado
    runner = xmlrunner.XMLTestRunner(output=output_dir)

    # Execute os testes e gere o arquivo results.xml
    runner.run(test_suite)
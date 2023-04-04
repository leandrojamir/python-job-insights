# 11 - Implemente um teste para a função read_brazilian_file
# A empresa cliente analisa relatórios em inglês, porém agora ela quer
# expandir seus negócios aqui para o Brasil e deseja analisar relatórios em
# português também. No entanto, as chaves do dict que usamos pra organizar os
# dados devem continuar em inglês. Ou seja: para gerar o relatório, deveremos
# ler as chaves em português e traduzi-las para inglês para povoar os nossos
# dados.

# Nossa equipe já implementou essa função, a read_brazilian_file, na qual
# adotamos a estratégia de chamar o método original read, que implementamos no
# requisito 1, e depois traduzimos as chaves para o inglês.
# Agora precisamos criar testes para ter certeza que esta tudo certo!
from src.pre_built.brazilian_jobs import read_brazilian_file


# O nome deste teste deve ser test_brazilian_jobs, e ele deve garantir
# que atenda as seguintes especificações:
def test_brazilian_jobs():
    # Chamar a função read_brazilian_file e ela deve receber um parâmetro:
    # path que é uma string com o caminho do arquivo csv em português
    # (tests/mocks/brazilians_jobs.csv);
    read = read_brazilian_file(path="tests/mocks/brazilians_jobs.csv")

    # Retorna uma lista de dicionários com as chaves em inglês
    # memoExemplo
    # O dicionário:
    # {"titulo": "Maquinista", "salario": "2000", "tipo": "trainee"}
    # Deve ser traduzido para:
    # {"title": "Maquinista", "salary": "2000", "type": "trainee"}
    dict_list = read
    assert "title" and "salary" and "type" in dict_list[-1]
    assert "title" and "salary" and "type" in dict_list[0]


# (.venv) jamir@jamir-X550CA:~/Projetos/computer-science/
# sd-023-b-project-job-insights$ python3 -i src/insights/jobs.py
# >>> local_teste_read_brazilian_file("tests/mocks/brazilians_jobs.csv")
# [{'title': 'Maquinista', 'salary': '2000', 'type': 'trainee'},
# {'title': 'Motorista', 'salary': '3000', 'type': 'full time'},
# {'title': 'Analista de Software', 'salary': '4000', 'type': 'full time'},
# {'title': 'Assistente administrativo', 'salary': '1700',
#  'type': ' full time'},
# {'title': 'Auxiliar administrativo', 'salary': '1400', 'type': ' full time'},
# {'title': 'Auxiliar usinagem', 'salary': '1400', 'type': ' full time'},
# {'title': 'Auxiliar de padaria', 'salary': '1400', 'type': ' full time'},
# {'title': 'Analista Contábil', 'salary': '1400', 'type': ' full time'},
# {'title': 'Gerente comercial', 'salary': '5000', 'type': ' full time'},
# {'title': 'Analista de Departamento Pessoal', 'salary': '4000',
#  'type': ' full time'},
# {'title': 'Esportista de Futebol profissional', 'salary': '50000',
#  'type': ' full time'},
# {'title': 'Analista de crédito', 'salary': '4000', 'type': ' full time'},
# {'title': 'Pessoa Programadora', 'salary': '3000', 'type': ' full time'},
# {'title': 'Ux Designer', 'salary': '3000', 'type': ' full time'},
# {'title': 'Auxiliar de manutenção', 'salary': ' 1400', 'type': ' full time'}]

# tests/brazilian/test_brazilian_jobs.py::test_brazilian_jobs
# [read_brazilian_file] PASSED

# 12 - Implemente um teste para a função sort_by
# Por fim, espera-se que a pessoa usuária possa escolher um critério de
# ordenação para exibir os empregos. Já temos uma implementação para essa
# ordenação em src/pre_built/sorting.py, mas queremos ter certeza de que ela
# funciona e, principalmente, que não deixará de funcionar conforme vamos
# implementando novos recursos. Precisamos então escrever um teste!


# A ordenação para min_salary deve ser crescente, mas para
# max_salary ou date_posted devem ser decrescentes.
# Os empregos que não apresentarem um valor válido no campo escolhido para
# ordenação devem aparecer no final da lista.
# De olho na dica: sort_by opera modificando (e ordenando) a lista jobs
# recebida, ou seja, não retorna uma cópia ordenada!
from src.pre_built.sorting import sort_by


# Esse teste deve se chamar test_sort_by_criteria e garantir que a função
# funciona segundo esta especificação:
def test_sort_by_criteria():
    # A função sort_by recebe dois parâmetros:
    # jobs uma lista de dicionários com os detalhes de cada emprego;
    brazilians_jobs_list = [
        {"title": "Maquinista", "min_salary": "2000"},
        {"title": "Motorista", "min_salary": "3000"},
        {"title": "Analista de Software", "min_salary": "4000"},
        {"title": "Assistente administrativo", "min_salary": "1700"},
        {"title": "Auxiliar administrativo", "min_salary": "1400"},
        {"title": "Auxiliar usinagem", "min_salary": "1400"},
        {"title": "Auxiliar de padaria", "min_salary": "1400"},
        {"title": "Analista Contábil", "min_salary": "1400"},
        {"title": "Gerente comercial", "min_salary": "5000"},
        {"title": "Analista de Departamento Pessoal", "min_salary": "4000"},
        {"title": "Esportista de Futebol profissional", "min_salary": "50000"},
        {"title": "Analista de crédito", "min_salary": "4000"},
        {"title": "Pessoa Programadora", "min_salary": "3000"},
        {"title": "Ux Designer", "min_salary": "3000"},
        {"title": "Auxiliar de manutenção", "min_salary": " 1400"},
    ]
    jobs = brazilians_jobs_list
    # criteria uma string com uma chave para ser usada como critério de
    # ordenação.
    # O parâmetro criteria deve ter um destes valores:
    # min_salary, max_salary, date_posted
    sort_by(jobs, "min_salary")
    assert [info["title"] for info in jobs] == [
        "Auxiliar administrativo",
        "Auxiliar usinagem",
        "Auxiliar de padaria",
        "Analista Contábil",
        "Auxiliar de manutenção",
        "Assistente administrativo",
        "Maquinista",
        "Motorista",
        "Pessoa Programadora",
        "Ux Designer",
        "Analista de Software",
        "Analista de Departamento Pessoal",
        "Analista de crédito",
        "Gerente comercial",
        "Esportista de Futebol profissional",
    ]


# >>> sort_by(brazilians_jobs_list, "min_salary")
# >>> brazilians_jobs_list
# [{'title': 'Auxiliar administrativo', 'min_salary': '1400'},
# {'title': 'Auxiliar usinagem', 'min_salary': '1400'},
# {'title': 'Auxiliar de padaria', 'min_salary': '1400'},
# {'title': 'Analista Contábil', 'min_salary': '1400'},
# {'title': 'Auxiliar de manutenção', 'min_salary': ' 1400'},
# {'title': 'Assistente administrativo', 'min_salary': '1700'},
# {'title': 'Maquinista', 'min_salary': '2000'},
# {'title': 'Motorista', 'min_salary': '3000'},
# {'title': 'Pessoa Programadora', 'min_salary': '3000'},
# {'title': 'Ux Designer', 'min_salary': '3000'},
# {'title': 'Analista de Software', 'min_salary': '4000'},
# {'title': 'Analista de Departamento Pessoal', 'min_salary': '4000'},
# {'title': 'Analista de crédito', 'min_salary': '4000'},
# {'title': 'Gerente comercial', 'min_salary': '5000'},
# {'title': 'Esportista de Futebol profissional', 'min_salary': '50000'}]
# >>>

# tests/sorting/test_sorting.py::test_sort_by_criteria[sort_by] PASSED

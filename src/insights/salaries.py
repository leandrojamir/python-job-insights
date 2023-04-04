from typing import Union, List, Dict

# 4 - Implemente a função get_max_salary
# Os dados apresentam faixas salariais para cada emprego exibido.
# Vamos agora encontrar o maior valor de todas as faixas.
from src.insights import jobs


def get_max_salary(path: str) -> int:
    # A função deve obter os dados da mesma forma que o requisito 2.
    info_file = jobs.read(path)
    # A função deve retornar um valor inteiro com o maior salário presente
    # na coluna "max_salary".
    salary_list = []
    for info in info_file:
        salary = info["max_salary"]
        # A função deve ignorar os valores ausentes.
        # https://acervolima.com/metodo-python-string-isdigit-1/
        if salary.isdigit():
            salary_list.append(int(salary))
    # print(max(salary_list))
    # print(type(salary_list))
    # print(type(salary))
    return max(salary_list)


# tests/test_salaries.py::test_get_max_salary 99860
# <class 'list'>
# <class 'str'>
# FAILED
# o maior pelo excell é 383416
# job_title
# Commodities Quantitative Analyst - Executive Director
# company	state	city	min_salary	max_salary
# JPMorgan Chase &amp;amp; Co	TX	Houston	195818	383416


# 5 - Implemente a função get_min_salary
# Os dados apresentam faixas salariais para cada emprego exibido.
# Vamos agora encontrar o menor valor de todas as faixas.
def get_min_salary(path: str) -> int:
    # A função deve obter os dados da mesma forma que o requisito 2.
    info_file = jobs.read(path)
    # A função deve retornar um valor inteiro com o menor salário presente
    # na coluna min_salary.
    salary_list = []
    for info in info_file:
        salary = info["min_salary"]
        # A função deve ignorar os valores ausentes.
        if salary.isdigit():
            salary_list.append(int(salary))
    return min(salary_list)


# tests/test_salaries.py::test_get_max_salary PASSED
# tests/test_salaries.py::test_get_min_salary PASSED


# 8 - Implemente a função matches_salary_range
# O aplicativo vai precisar filtrar os empregos por salário também. Como uma
# função auxiliar, implemente matches_salary_range para conferir que o salário
# procurado está dentro da faixa salarial daquele emprego. Vamos aproveitar
# também para conferir se a faixa salarial faz sentido -- isto é, se o valor
# mínimo é menor que o valor máximo.

# 'matches_salary_range' is too complex (6)Flake8(C901)
def min_max_salary_doesnt(job):
    # A função deve lançar um erro ValueError nos seguintes casos:
    # alguma das chaves min_salary ou max_salary estão ausentes no dicionário;
    if ("min_salary" not in job) or ("max_salary" not in job):
        raise ValueError("min/max_salary doesn't exists")


# A função deve receber um dicionário job como primeiro parâmetro,
# com as chaves min_salary e max_salary, que podem ser números ou strings que
# representem números.
# A função deve receber um número ou string que represente o número salary
# como segundo parâmetro.
def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    min_max_salary_doesnt(job)
    # A função deve lançar um erro ValueError nos seguintes casos:
    # alguma das chaves min_salary ou max_salary tem valores não-numéricos;
    # o parâmetro salary tem valores não numéricos;
    try:
        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])
        # o valor de min_salary é maior que o valor de max_salary;
        if min_salary > max_salary:
            raise ValueError("min_salary is greather than max_salary")
        salary = int(salary)
        # A função deve retornar True se o salário procurado estiver dentro da
        # faixa salarial ou False se não estiver.
        if min_salary <= salary <= max_salary:
            return True
        else:
            return False
    except (ValueError, TypeError, KeyError):
        raise ValueError("min/max_salary or salary aren't valid integers")

    # tests/test_salaries.py::test_matches_salary_range PASSED


# 9 - Implemente a função filter_by_salary_range
# Agora vamos implementar o filtro propriamente dito.
# Para esta filtragem, podemos usar a função auxiliar implementada no
# requisito anterior -- tomando o cuidado de descartar os empregos que
# apresentarem faixas salariais inválidas.

# A função deve receber uma lista de dicionários jobs como primeiro parâmetro.
# A função deve receber um número ou string salary como segundo parâmetro.
def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    # A função deve retornar uma lista com todos os empregos
    all_jobs_list = []
    # descartar os empregos que apresentarem faixas salariais inválidas
    # 'filter_by_salary_range' is too complex (6)Flake8(C901)
    if salary is None or not (str(salary).isnumeric()):
        return []
    for info in jobs:
        # A função deve ignorar os empregos com valores inválidos para
        # min_salary ou max_salary.
        if info["min_salary"] != "" and info["max_salary"] != "":
            # A função deve retornar uma lista com todos os empregos
            # onde o salário "salary" estiver entre os valores da coluna
            # min_salary e max_salary.
            if (
                int(info["min_salary"])
                <= int(salary)
                <= int(info["max_salary"])
            ):
                all_jobs_list.append(info)
    return all_jobs_list


# tests/test_salaries.py::test_matches_salary_range PASSED
# tests/test_salaries.py::test_filter_by_salary_range PASSED

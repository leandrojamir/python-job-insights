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


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    raise NotImplementedError


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError

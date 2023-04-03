from functools import lru_cache
from typing import List, Dict

# 1 - Implemente a função read
# Para começarmos a processar os dados, devemos antes carregá-los em
# nossa aplicação. Esta função será responsável por abrir o arquivo
# CSV e retornar os dados no formato de uma lista de dicionários.
import csv


@lru_cache
# A função deve receber um path (uma string com o caminho para um arquivo).
def read(path: str) -> List[Dict]:
    # A função deve abrir o arquivo e ler seus conteúdos.
    with open(path) as file:
        # A função deve tratar o arquivo como CSV.
        file = csv.DictReader(file)
        # A função deve retornar uma lista de dicionários, onde as chaves são
        # os cabeçalhos de cada coluna e os valores correspondem a cada linha.
        list = []
        for row in file:
            list.append(row)
    return list


# (.venv) jamir@jamir-X550CA:~/Projetos/computer-science/
# sd-023-b-project-job-insights$ python3 -i src/insights/jobs.py
# >>> read("data/jobs.csv") OK
# tests/test_jobs.py::test_read_jobs PASSED


# 2 - Implemente a função get_unique_job_types
# Agora que temos como carregar os dados, podemos começar a extrair informação
# deles. Primeiro, vamos identificar quais tipos de empregos existem.
# A função deve receber o path do arquivo csv com os dados.
def get_unique_job_types(path: str) -> List[str]:
    # Deve invocar a função jobs.read com o path recebido para obter os dados.
    info_file = read(path)
    # Deve retornar uma lista de valores únicos presentes na coluna job_type.
    types_of_jobs_list = []
    for info in info_file:
        if info["job_type"] not in types_of_jobs_list:
            types_of_jobs_list.append(info["job_type"])
    return types_of_jobs_list


# (.venv) jamir@jamir-X550CA:~/Projetos/computer-science/
# sd-023-b-project-job-insights$ python3 -i src/insights/jobs.py
# >>> get_unique_job_types("data/jobs.csv")
# ['FULL_TIME', 'PART_TIME', 'OTHER', 'INTERN', 'CONTRACTOR', 'TEMPORARY']
# >>>
# tests/test_jobs.py::test_get_unique_job_types PASSED


# 6 - Implemente a função filter_by_job_type
# Os empregos estão listados em um aplicativo web. Para permitir que a pessoa
# usuária possa filtrar os empregos por tipo de emprego, vamos precisar
# implementar esse filtro.

# A função deve receber uma lista de dicionários jobs como primeiro parâmetro.
# A função deve receber uma string job_type como segundo parâmetro.
def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    # A função deve retornar uma lista com todos os empregos onde a coluna
    # job_type corresponde ao parâmetro job_type.
    all_jobs_list = []
    for info in jobs:
        if info["job_type"] == job_type:
            all_jobs_list.append(info)
    return all_jobs_list


# tests/test_jobs.py::test_filter_by_job_type PASSED

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


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    raise NotImplementedError


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError

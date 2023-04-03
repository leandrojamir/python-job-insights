from typing import List, Dict

# 3 - Implemente a função get_unique_industries
# Da mesma forma, agora iremos identificar quais indústrias estão
# representadas nesse conjunto de dados.
from src.insights import jobs


def get_unique_industries(path: str) -> List[str]:
    # A função deve obter os dados da mesma forma que o requisito 2.
    info_file = jobs.read(path)
    # Deve retornar uma lista de valores únicos presentes na coluna "industry".
    industry_list = []
    for info in info_file:
        if (
            info["industry"] not in industry_list
            # A função desconsidera valores vazios
            and info["industry"] != ""
        ):
            industry_list.append(info["industry"])
    # print(industry_list)
    # nota: estava printando todas com espaço " "
    # tests/test_industries.py::test_get_unique_industries
    # ['Finance', '', 'Health Care', 'Construction, Repair & Maintenance',
    # 'Information Technology', 'Telecommunications', 'Biotech &
    # Pharmaceuticals', 'Business Services', 'Retail', 'Government',
    # 'Oil, Gas, Energy & Utilities', 'Real Estate', 'Manufacturing',
    # 'Insurance', 'Media', 'Consumer Services', 'Arts, Entertainment
    # & Recreation', 'Transportation & Logistics', 'Education',
    # 'Accounting & Legal', 'Non-Profit', 'Restaurants, Bars & Food Services',
    #  'Agriculture & Forestry', 'Aerospace & Defense']FAILED
    return industry_list


# tests/test_industries.py::test_get_unique_industries PASSED


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError

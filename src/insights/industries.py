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


# 7 - Implemente a função filter_by_industry
# Do mesmo modo, o aplicativo precisa permitir uma filtragem por indústria.
# Vamos precisar implementar esse filtro também.

# A função deve receber uma lista de dicionários jobs como primeiro parâmetro.
# A função deve receber uma string industry como segundo parâmetro.
def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    # A função deve retornar uma lista de dicionários com todos os empregos
    # onde a coluna industry corresponde ao parâmetro "industry".
    all_jobs_list = []
    for info in jobs:
        if info["industry"] == industry:
            all_jobs_list.append(info)
    return all_jobs_list


# tests/test_industries.py::test_filter_by_industry PASSED

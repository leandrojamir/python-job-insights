# 10 - Implemente um teste para a função count_ocurrences
# A empresa cliente contratou um relatório que informa a quantidade de
# ocorrências das palavra Python e Javascript nos dados e, para isso, temos
# uma implementação pronta em src/pre_built/counter.py. Durante o
# desenvolvimento, sofremos com alguns bugs, que já foram resolvidos. Para
# termos certeza e confiança da nossa entrega, no entanto, e não corrermos
# riscos, precisaremos de testes automatizados que garantam isso!
from src.pre_built.counter import count_ocurrences

# def count_ocurrences(path: str, word: str) -> int:
#     file = open(path, "r")
#     read_data = file.read()
#     word_count = read_data.lower().count(word.lower())
#     return word_count


# O nome deste teste deve ser test_counter,
def test_counter():
    # e ele deve garantir que atenda estas especificações:
    # Chamar a função count_ocurrences passando dois parâmetros:
    # path uma string com o caminho do arquivo (data/jobs.csv);
    # word uma string com a palavra a ser contabilizada.
    leandro = count_ocurrences(path="data/jobs.csv", word="LeAnDrO")
    trybe = count_ocurrences(path="data/jobs.csv", word="Trybe")
    java = count_ocurrences(path="data/jobs.csv", word="jAvA")

    # Garantir que a função retorna corretamente a quantidade de ocorrências da
    # palavra solicitada
    # A contagem de palavras deve ser case insentitive, ou seja, não
    # diferenciar letras maiúsculas de minúsculas
    assert leandro == 4
    assert trybe == 0
    assert java == 676


# (.venv) jamir@jamir-X550CA:~/Projetos/computer-science/
# sd-023-b-project-job-insights$ python3 -i src/pre_built/counter.py
# >>> count_ocurrences("data/jobs.csv", "Leandro")
# 4
# >>> count_ocurrences("data/jobs.csv", "LeAnDrO")
# 4
# >>> count_ocurrences("data/jobs.csv", "Trybe")
# 0
# >>> count_ocurrences("data/jobs.csv", "TryBe")
# 0
# >>> count_ocurrences("data/jobs.csv", "Java")
# 676
# >>> count_ocurrences("data/jobs.csv", "jAvA")
# 676
# >>>

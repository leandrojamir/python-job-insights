# Boas-vindas ao repositório do Job Insights!

<details>
  <summary><strong>👨‍💻 O que deverá ser desenvolvido</strong></summary><br />
  <p align="center">
    <img src="/.images/job.png" alt="Logo Aplicação" width="300"/>
  </p>
  
  Neste projeto você implementará análises a partir de um conjunto de dados sobre empregos. Suas implementações serão incorporadas a um aplicativo Web desenvolvido com Flask (um framework web muito popular na comunidade Python). Você também terá a oportunidade de escrever testes para a implementação de uma análise de dados. Por fim, como bônus, você terá o desafio de escrever uma rota e view para um recurso novo usando Flask!

  Os dados foram extraídos do site [Glassdoor](https://www.glassdoor.com.br/) e obtidos através do [Kaggle](https://www.kaggle.com/atharvap329/glassdoor-data-science-job-data), uma plataforma disponiblizando conjuntos de dados para cientistas de dados.

  🚵 Habilidades a serem trabalhadas:
  <ul>
    <li>Utilizar o terminal interativo do Python.</li>
    <li>Utilizar estruturas condicionais e de repetição.</li>
    <li>Utilizar funções built-in do Python.</li>
    <li>Utilizar tratamento de exceções.</li>
    <li>Realizar a manipulação de arquivos.</li>
    <li>Escrever funções.</li>
    <li>Escrever testes com Pytest.</li>
    <li>Escrever seus próprios módulos e importá-los em outros códigos.</li>
  </ul>
</details>

<details>
  <summary><strong>🧱 Estrutura do Projeto</strong></summary><br />
  Este repositório já contém um template com a estrutura de diretórios e arquivos, tanto de código quanto de teste criados. Veja abaixo:

  ```
  Legenda:
  🔸Arquivos que não podem ser alterados
  🔹Arquivos a serem alterados para realizar os requisitos.
  .
  ├──🔸README.md
  ├──🔸Dockerfile
  ├──🔸docker-compose.yml
  ├──🔸dev-requirements.txt
  ├──🔸requirements.txt
  ├── data
  │   └──🔸jobs.csv
  ├── src
  │   ├── flask_app
  │   │   ├── templates
  │   │   │   ├── includes
  │   │   │   │   └──🔸nav.jinja2
  │   │   │   ├──🔸base.jinja2
  │   │   │   ├──🔸index.jinja2
  │   │   │   ├──🔸job.jinja2
  │   │   │   └──🔸list_jobs.jinja2
  │   │   ├──🔸app.py
  │   │   ├──🔸more_insights.py
  │   │   └──🔹routes_and_views.py
  │   ├── insights
  │   │   ├──🔹industries.py
  │   │   ├──🔹jobs.py
  │   │   └──🔹salaries.py
  │   ├── pre_built
  │   │   ├──🔸brazilian_jobs.py
  │   │   ├──🔸counter.py
  │   │   └──🔸sorting.py
  ├── tests
  │   ├──🔸__init__.py
  │   ├──🔸conftest.py
  │   ├──🔸marker.py
  │   ├── brazilian
  │   │   ├──🔸__init__.py
  │   │   ├──🔸conftest.py
  │   │   ├──🔸mocks.py
  │   │   ├──🔹test_brazilian_jobs.py
  │   ├── counter
  │   │   ├──🔸__init__.py
  │   │   ├──🔸conftest.py
  │   │   ├──🔸mocks.py
  │   │   ├──🔹test_counter.py
  │   ├── mocks
  │   │   ├──🔸job_1.html
  │   │   ├──🔸jobs.csv
  │   │   ├──🔸jobs_with_industries.csv
  │   │   ├──🔸jobs_with_salaries.csv
  │   │   └──🔸jobs_with_types.csv
  │   ├── sorting
  │   │   ├──🔸__init__.py
  │   │   ├──🔸conftest.py
  │   │   ├──🔸mocks.py
  │   │   └──🔹test_sorting.py
  │   ├──🔸test_flask_app.py
  │   ├──🔸test_industries.py
  │   ├──🔸test_jobs.py
  │   ├──🔸test_salaries.py
  │   ├──🔸test_more_insights.py
  │   └──🔸test_routes_and_views.py
  ```

  Na estrutura deste _template_, você deve implementar as funções necessárias. Novos arquivos e funções podem ser criados conforme a necessidade da sua implementação, porém não remova arquivos já existentes.

</details>

<details>
  <summary><strong>🎛 Linter</strong></summary><br />

  Para garantir a qualidade do código, vamos utilizar neste projeto o linter `Flake8`.
  Assim o código estará alinhado com as boas práticas de desenvolvimento, sendo mais legível
  e de fácil manutenção! Para rodá-lo localmente no projeto, execute o comandos abaixo:

  ```bash
  python3 -m flake8
  ```

  ⚠️ **PULL REQUESTS COM ISSUES DE LINTER NÃO SERÃO AVALIADAS.
  ATENTE-SE PARA RESOLVÊ-LAS ANTES DE FINALIZAR O DESENVOLVIMENTO!** ⚠️
</details>

<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary><br />
  O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
  $ python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
  $ source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
  $ python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  Quando precisar desativar o ambiente virtual, execute o comando "deactivate". Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

  O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.
</details>

# Requisitos Obrigatórios

## 1 - Implemente a função `read`
> **Implemente em:** src/insights/jobs.py

Para começarmos a processar os dados, devemos antes carregá-los em nossa aplicação. Esta função será responsável por abrir o arquivo CSV e retornar os dados no formato de uma lista de dicionários.

- A função deve receber um _path_ (uma string com o caminho para um arquivo).
- A função deve abrir o arquivo e ler seus conteúdos.
- A função deve tratar o arquivo como CSV.
- A função deve retornar uma lista de dicionários, onde as chaves são os cabeçalhos de cada coluna e os valores correspondem a cada linha.

<details>
  <summary>
    <b>📝Exemplo</b>
  </summary>
  Se o conteúdo do arquivo for:
  
```
nome,cidade,telefone
Ana,Curitiba,1111111
Bernardo,Santos,999999
```

  O retorno da função deverá ser: 
  
```python
  [
    {"nome": "Ana", "cidade": "Curitiba", "telefone": "1111111"},
    {"nome": "Bernardo", "cidade": "Santos", "telefone": "999999"}
  ]
```
</details> 


## 2 - Implemente a função `get_unique_job_types`
> **Implemente em:** `src/insights/jobs.py`

Agora que temos como carregar os dados, podemos começar a extrair informação deles. Primeiro, vamos identificar quais tipos de empregos existem.

- A função deve receber o _path_ do arquivo csv com os dados.
- A função deve invocar a função `jobs.read` com o _path_ recebido para obter os dados.
- A função deve retornar uma lista de valores únicos presentes na coluna `job_type`.


## 3 - Implemente a função `get_unique_industries`
> **Implemente em:** `src/insights/industries.py`

Da mesma forma, agora iremos identificar quais indústrias estão representadas nesse conjunto de dados.

- A função deve obter os dados da mesma forma que o requisito 2.
- A função deve retornar uma lista de valores únicos presentes na coluna `industry`.
- A função desconsidera valores vazios


## 4 - Implemente a função `get_max_salary`
> **Implemente em:** `src/insights/salaries.py`

Os dados apresentam faixas salariais para cada emprego exibido. Vamos agora encontrar o maior valor de todas as faixas.

- A função deve obter os dados da mesma forma que o requisito 2.
- A função deve ignorar os valores ausentes.
- A função deve retornar *um valor inteiro* com o maior salário presente na coluna `max_salary`.


## 5 - Implemente a função `get_min_salary`
> **Implemente em:** `src/insights/salaries.py`

Os dados apresentam faixas salariais para cada emprego exibido. Vamos agora encontrar o menor valor de todas as faixas.

- A função deve obter os dados da mesma forma que o requisito 2.
- A função deve ignorar os valores ausentes.
- A função deve retornar *um valor inteiro* com o menor salário presente na coluna `min_salary`.


## 6 - Implemente a função `filter_by_job_type`
<p align="center">
  <img src="/.images/filter.png" alt="Contagem" width="400"/>
</p>

> **Implemente em:** `src/insights/jobs.py`

Os empregos estão listados em um aplicativo web. Para permitir que a pessoa usuária possa filtrar os empregos por tipo de emprego, vamos precisar implementar esse filtro.

- A função deve receber uma lista de dicionários `jobs` como primeiro parâmetro.
- A função deve receber uma string `job_type` como segundo parâmetro.
- A função deve retornar uma lista com todos os empregos onde a coluna `job_type` corresponde ao parâmetro `job_type`.


## 7 - Implemente a função `filter_by_industry`
> **Implemente em:** `src/insights/industries.py`

Do mesmo modo, o aplicativo precisa permitir uma filtragem por indústria. Vamos precisar implementar esse filtro também.

- A função deve receber uma lista de dicionários `jobs` como primeiro parâmetro.
- A função deve receber uma string `industry` como segundo parâmetro.
- A função deve retornar uma lista de dicionários com todos os empregos onde a coluna `industry` corresponde ao parâmetro `industry`.


## 8 - Implemente a função `matches_salary_range`
> **Implemente em:** `src/insights/salaries.py`

O aplicativo vai precisar filtrar os empregos por salário também. Como uma função auxiliar, implemente `matches_salary_range` para conferir que o salário procurado está dentro da faixa salarial daquele emprego. Vamos aproveitar também para conferir se a faixa salarial faz sentido -- isto é, se o valor mínimo é menor que o valor máximo.

- A função deve receber um dicionário `job` como primeiro parâmetro, com as chaves `min_salary` e `max_salary`, que podem ser números ou strings que representem números.
- A função deve receber um número ou string que represente o número `salary` como segundo parâmetro.
- A função deve lançar um erro `ValueError` nos seguintes casos:
  - alguma das chaves `min_salary` ou `max_salary` estão *ausentes* no dicionário;
  - alguma das chaves `min_salary` ou `max_salary` tem valores não-numéricos;
  - o valor de `min_salary` é maior que o valor de `max_salary`;
  - o parâmetro `salary` tem valores não numéricos;
- A função deve retornar `True` se o salário procurado estiver dentro da faixa salarial ou `False` se não estiver.


## 9 - Implemente a função `filter_by_salary_range`
> **Implemente em:** `src/insights/salaries.py`

Agora vamos implementar o filtro propriamente dito. Para esta filtragem, podemos usar a função auxiliar implementada no requisito anterior -- tomando o cuidado de descartar os empregos que apresentarem faixas salariais inválidas.

- A função deve receber uma lista de dicionários `jobs` como primeiro parâmetro.
- A função deve receber um número ou string `salary` como segundo parâmetro.
- A função deve ignorar os empregos com valores inválidos para `min_salary` ou `max_salary`.
  - Observação: strings que representem números são valores **válidos** para `min_salary` ou `max_salary`.
- A função deve retornar uma lista com todos os empregos onde o salário `salary` estiver entre os valores da coluna `min_salary` e `max_salary`.


## 10 - Implemente um teste para a função `count_ocurrences`
> **Implemente em:** `tests/counter/test_counter.py`

  <p align="center">
    <img src="/.images/flask.png" alt="Imagem sobre contar ocorrências" width="600"/>
  </p>

A empresa cliente contratou um relatório que informa a quantidade de ocorrências das palavra *Python* e *Javascript* nos dados e, para isso, temos uma implementação pronta em `src/pre_built/counter.py`. Durante o desenvolvimento, sofremos com alguns `bugs`, que já foram resolvidos. Para termos certeza e confiança da nossa entrega, no entanto, e não corrermos riscos, precisaremos de *testes automatizados* que garantam isso!

O nome deste teste **deve** ser `test_counter`, e ele deve garantir que atenda estas especificações:

- **Chamar** a função `count_ocurrences` passando dois parâmetros:
  - `path` uma string com o caminho do arquivo (`data/jobs.csv`);
  - `word` uma string com a palavra a ser contabilizada.
- Garantir que a função retorna corretamente a quantidade de ocorrências da palavra solicitada 
  - A contagem de palavras deve ser _case insentitive_, ou seja, não diferenciar letras maiúsculas de minúsculas


## 11 - Implemente um teste para a função `read_brazilian_file`
> **Implemente em:** `tests/brazilian/test_brazilian_jobs.py`

A empresa cliente analisa relatórios em inglês, porém agora ela quer expandir seus negócios aqui para o Brasil e deseja analisar relatórios em português também. No entanto, as chaves do `dict` que usamos pra organizar os dados **devem** continuar em inglês. Ou seja: para gerar o relatório, deveremos ler as chaves em português e traduzi-las para inglês para povoar os nossos dados.

Nossa equipe já implementou essa função, a `read_brazilian_file`, na qual adotamos a estratégia de chamar o método original `read`, que implementamos no `requisito 1`, e depois traduzimos as chaves para o inglês. Agora precisamos criar testes para ter certeza que esta tudo certo!

O nome deste teste **deve** ser `test_brazilian_jobs`, e ele deve garantir que atenda as seguintes especificações:

- **Chamar** a função `read_brazilian_file` e ela deve receber um parâmetro:
  - `path` que é uma string com o caminho do arquivo csv em português (`tests/mocks/brazilians_jobs.csv`);
  - Retorna uma lista de dicionários com as chaves em inglês

<details>
  <summary>
    <b>📝Exemplo</b>
  </summary>
  O dicionário: <code>{"titulo": "Maquinista", "salario": "2000", "tipo": "trainee"}</code>

  Deve ser traduzido para: <code>{"title": "Maquinista", "salary": "2000", "type": "trainee"}</code>
</details>  


## 12 - Implemente um teste para a função `sort_by`
> **Implemente em:** `tests/sorting/test_sorting.py`

Por fim, espera-se que a pessoa usuária possa escolher um critério de ordenação para exibir os empregos. Já temos uma implementação para essa ordenação em `src/pre_built/sorting.py`, mas queremos ter certeza de que ela funciona e, principalmente, que não deixará de funcionar conforme vamos implementando novos recursos. Precisamos então escrever um *teste*!

Esse teste deve se chamar `test_sort_by_criteria` e garantir que a função funciona segundo esta especificação:

- A função `sort_by` recebe dois parâmetros:
  - `jobs` uma lista de dicionários com os detalhes de cada emprego;
  - `criteria` uma string com uma chave para ser usada como critério de ordenação.
- O parâmetro `criteria` deve ter um destes valores: `min_salary`, `max_salary`, `date_posted`
- A ordenação para `min_salary` deve ser crescente, mas para `max_salary` ou `date_posted` devem ser decrescentes.
- Os empregos que não apresentarem um valor válido no campo escolhido para ordenação devem aparecer no final da lista.

👀 De olho na dica: `sort_by` opera modificando (e ordenando) a lista `jobs` recebida, ou seja, não retorna uma cópia ordenada!


---

# Requisitos Bônus

## 13 - (`Bônus`) Implemente a página de um job
> **Implemente em:** `src/flask_app/routes_and_views.py`

Para fechar com chave de ouro, que tal testar o quanto você consegue aprender de Flask apenas vendo como fizemos as páginas de `index` e de `jobs`, e tentar criar uma página que irá exibir todas as informações de um job em específico?

- A função deve se chamar `job`.
- A função deve ser decorada com a rota `/job/<index>`.
- A função deve receber um parâmetro `index`.
- A função deve chamar a `read` para ter uma lista com todos os jobs.
- A função deve chamar a `get_job`, declarada no arquivo `src/flask_app/more_insights.py`, para selecionar um job específico pelo `index`.
- A função deve renderizar o template `job.jinja2`, passando um parâmetro `job` contendo o job retornado pela `get_job`.

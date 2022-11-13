![TRYBE_JOB_INSIGHTS](https://user-images.githubusercontent.com/20843662/201546059-e28e3a47-0623-4440-98ff-3c98e625c919.png)

![GitHub top language](https://img.shields.io/github/languages/top/tcorrea/trybe-tech-news)
[![LinkedIn Badge](https://img.shields.io/badge/LinkedIn-Profile-informational?style=flat-square&logo=linkedin&logoColor=white&color=ffb86c)](https://www.linkedin.com/in/thiago-de-carvalho-correa/)

# Descrição

Esse projeto tem como objetivo manipular arquivos json, csv e xml, aplicando alguns filtros.

# Estrutura do projeto

Estrutura do projeto e descrição dos arquivos que foram desenvolvidos por mim e pela Trybe.

```
  Legenda:
  🔸Arquivos desenvolvidos pela Trybe (não foram alterados).
  🔹Arquivos desenvolvidos por mim.
  .
  ├──🔹README.md
  ├──🔸Dockerfile
  ├──🔸docker-compose.yml
  ├──🔸dev-requirements.txt
  ├──🔸requirements.txt
  ├── src
  │   ├──🔸app.py
  │   ├──🔸brazilian_jobs.py
  │   ├──🔸counter.py
  │   ├──🔹insights.py
  │   ├──🔸jobs.csv
  │   ├──🔹jobs.py
  │   ├──🔸more_insights.py
  │   ├──🔹routes_and_views.py
  │   ├──🔸sorting.py
  │   └── templates
  │       ├──🔸base.jinja2
  │       ├── includes
  │       │   └──🔸nav.jinja2
  │       ├──🔸index.jinja2
  │       ├──🔸job.jinja2
  │       └──🔸list_jobs.jinja2
  ├── tests
  │   ├──🔸__init__.py
  │   ├──🔸conftest.py
  │   ├──🔸marker.py
  │   ├── brazilian
  │   │   ├──🔸__init__.py
  │   │   ├──🔸conftest.py
  │   │   ├──🔸mocks.py
  │   │   ├──🔹test_brazilian_jobs.py
  │   ├── counter
  │   │   ├──🔸__init__.py
  │   │   ├──🔸conftest.py
  │   │   ├──🔸mocks.py
  │   │   ├──🔹test_counter.py
  │   ├── mocks
  │   │   ├──🔸job_1.html
  │   │   ├──🔸jobs.csv
  │   │   ├──🔸jobs_with_industries.csv
  │   │   ├──🔸jobs_with_salaries.csv
  │   │   └──🔸jobs_with_types.csv
  │   ├── sorting
  │   │   ├──🔸__init__.py
  │   │   ├──🔸conftest.py
  │   │   ├──🔸mocks.py
  │   │   └──🔹test_sorting.py
  │   ├──🔸test_flask_app.py
  │   ├──🔸test_insights.py
  │   ├──🔸test_jobs.py
  │   ├──🔸test_more_insights.py
  │   └──🔸test_routes_and_views.py
```

# Instalação

1. Clone o repositório

- Use o comando:
  ```
  git clone https://github.com/tcorrea/trybe-job-insights
  ```
- Entre na pasta do repositório que você acabou de clonar:
  ```
  cd trybe-job-insights
  ```

2. Crie o ambiente virtual para o projeto

   ```
   python3 -m venv .venv && source .venv/bin/activate
   ```

3. Instale as dependências
   ```
   python3 -m pip install -r dev-requirements.txt
   ```

# Requisitos e soluções

## 1 - Implemente a função `read`

> **Implemente em:** [`src/jobs.py`](https://github.com/tcorrea/trybe-job-insights/blob/main/src/jobs.py)

<details>
  <summary>Expandir</summary>

Para começarmos a processar os dados, devemos antes carregá-los em nossa aplicação. Esta função será responsável por abrir o arquivo CSV e retornar os dados no formato de uma lista de dicionários.

- A função deve receber um path (uma string com o caminho para um arquivo).

- A função deve abrir o arquivo e ler seus conteúdos.

- A função deve tratar o arquivo como CSV.

- A função deve retornar uma lista de dicionários, onde as chaves são os cabeçalhos de cada coluna e os valores correspondem a cada linha.

### _Solução_

![carbon (3)](https://user-images.githubusercontent.com/20843662/201547114-9dbb1a32-405d-4247-8e5e-bb1d3643e584.png)

</details>

## 2 - Implemente a função `get_unique_job_types`

> **Implemente em:** [`src/insights.py`](https://github.com/tcorrea/trybe-job-insights/blob/main/src/insights.py)

<details>
  <summary>Expandir</summary>
Agora que temos como carregar os dados, podemos começar a extrair informação deles. Primeiro, vamos identificar quais tipos de empregos existem.

- A função deve receber o path do arquivo csv com os dados.

- A função deve invocar a função `jobs.read` com o path recebido para obter os dados.

- A função deve retornar uma lista de valores únicos presentes na coluna `job_type`.

### _Solução_

![carbon (4)](https://user-images.githubusercontent.com/20843662/201547346-ff01e4a4-9ec5-415b-96f9-c1010d489295.png)

</details>

## 3 - Implemente a função `get_unique_industries`

> **Implemente em:** [`src/insights.py`](https://github.com/tcorrea/trybe-job-insights/blob/main/src/insights.py)

<details>
  <summary>Expandir</summary>
Da mesma forma, agora iremos identificar quais indústrias estão representadas nesse conjunto de dados.

- A função deve obter os dados da mesma forma que o requisito 2.
- A função deve retornar uma lista de valores únicos presentes na coluna `industry`.
- A função desconsidera valores vazios

### _Solução_

![carbon (5)](https://user-images.githubusercontent.com/20843662/201547684-9751b514-1064-4d6d-b773-a20260495ce0.png)

</details>

## 4 - Implemente a função `get_max_salary`

> **Implemente em:** [`src/insights.py`](https://github.com/tcorrea/trybe-job-insights/blob/main/src/insights.py)

<details>
  <summary>Expandir</summary>

Os dados apresentam faixas salariais para cada emprego exibido. Vamos agora encontrar o maior valor de todas as faixas.

- A função deve obter os dados da mesma forma que o requisito 2.
- A função deve ignorar os valores ausentes.
- A função deve retornar _um valor inteiro_ com o maior salário presente na coluna `max_salary`.

### _Solução_

![carbon (6)](https://user-images.githubusercontent.com/20843662/201547862-7c9c4974-ce1c-45e2-94fc-6533ddbc0746.png)

</details>

## 5 - Implemente a função `get_min_salary`

> **Implemente em:** [`src/insights.py`](https://github.com/tcorrea/trybe-job-insights/blob/main/src/insights.py)

<details>
  <summary>Expandir</summary>

Os dados apresentam faixas salariais para cada emprego exibido. Vamos agora encontrar o menor valor de todas as faixas.

- A função deve obter os dados da mesma forma que o requisito 2.
- A função deve ignorar os valores ausentes.
- A função deve retornar _um valor inteiro_ com o menor salário presente na coluna `min_salary`.

### _Solução_

![carbon (7)](https://user-images.githubusercontent.com/20843662/201548003-970cf485-5eca-4ba7-87b3-c272f8ae1b27.png)

</details>

## 6 - Implemente a função `filter_by_job_type`

> **Implemente em:** [`src/insights.py`](https://github.com/tcorrea/trybe-job-insights/blob/main/src/insights.py)

<details>
  <summary>Expandir</summary>

Os empregos estão listados em um aplicativo web. Para permitir que a pessoa usuária possa filtrar os empregos por tipo de emprego, vamos precisar implementar esse filtro.

- A função deve receber uma lista de dicionários `jobs` como primeiro parâmetro.
- A função deve receber uma string `job_type` como segundo parâmetro.
- A função deve retornar uma lista com todos os empregos onde a coluna `job_type` corresponde ao parâmetro `job_type`.

### _Solução_

![carbon (8)](https://user-images.githubusercontent.com/20843662/201548236-9d439760-3097-474f-ae50-be876698f3f8.png)

</details>

## 7 - Implemente a função `filter_by_industry`

> **Implemente em:** [`src/insights.py`](https://github.com/tcorrea/trybe-job-insights/blob/main/src/insights.py)

<details>
  <summary>Expandir</summary>

Do mesmo modo, o aplicativo precisa permitir uma filtragem por indústria. Vamos precisar implementar esse filtro também.

- A função deve receber uma lista de dicionários `jobs` como primeiro parâmetro.
- A função deve receber uma string `industry` como segundo parâmetro.
- A função deve retornar uma lista de dicionários com todos os empregos onde a coluna `industry` corresponde ao parâmetro `industry`.

### _Solução_

![carbon (9)](https://user-images.githubusercontent.com/20843662/201548308-736e617e-dde1-4f47-8980-52504719e18d.png)

</details>

## 8 - Implemente a função `matches_salary_range`

> **Implemente em:** [`src/insights.py`](https://github.com/tcorrea/trybe-job-insights/blob/main/src/insights.py)

<details>
  <summary>Expandir</summary>

O aplicativo vai precisar filtrar os empregos por salário também. Como uma função auxiliar, implemente `matches_salary_range` para conferir que o salário procurado está dentro da faixa salarial daquele emprego. Vamos aproveitar também para conferir se a faixa salarial faz sentido -- isto é, se o valor mínimo é menor que o valor máximo.

- A função deve receber um dicionário `job` como primeiro parâmetro, com as chaves `min_salary` e `max_salary`.
- A função deve receber um inteiro `salary` como segundo parâmetro.
- A função deve lançar um erro `ValueError` nos seguintes casos:
  - alguma das chaves `min_salary` ou `max_salary` estão _ausentes_ no dicionário;
  - alguma das chaves `min_salary` ou `max_salary` tem valores não-numéricos;
  - o valor de `min_salary` é maior que o valor de `max_salary`;
  - o parâmetro `salary` tem valores não numéricos;
- A função deve retornar `True` se o salário procurado estiver dentro da faixa salarial ou `False` se não estiver.

### _Solução_

![carbon (10)](https://user-images.githubusercontent.com/20843662/201548424-2f198c69-ad0d-43f8-ac65-f4aca02bf2e9.png)

</details>

## 9 - Implemente a função `filter_by_salary_range`

> **Implemente em:** [`src/insights.py`](https://github.com/tcorrea/trybe-job-insights/blob/main/src/insights.py)

<details>
  <summary>Expandir</summary>

Agora vamos implementar o filtro propriamente dito. Para esta filtragem, podemos usar a função auxiliar implementada no requisito anterior -- tomando o cuidado de descartar os empregos que apresentarem faixas salariais inválidas.

- A função deve receber uma lista de dicionários `jobs` como primeiro parâmetro.
- A função deve receber um inteiro `salary` como segundo parâmetro.
- A função deve ignorar os empregos com valores inválidos para `min_salary` ou `max_salary`.
- A função deve retornar uma lista com todos os empregos onde o salário `salary` estiver entre os valores da coluna `min_salary` e `max_salary`.

### _Solução_

![carbon (11)](https://user-images.githubusercontent.com/20843662/201548505-8c2c6282-5aed-44f4-a6c6-cca01d1d1454.png)

</details>

## 10 - Implemente um teste para a função `count_ocurrences`

> **Implemente em:** [`tests/counter/test_counter.py`](https://github.com/tcorrea/trybe-job-insights/blob/main/tests/counter/test_counter.py)

<details>
  <summary>Expandir</summary>

A empresa cliente contratou um relatório que informa a quantidade de ocorrências das palavra _Python_ e _Javascript_ nos dados e, para isso, temos uma implementação pronta em `src/counter.py`. Durante o desenvolvimento, sofremos com alguns `bugs`, que já foram resolvidos. Para termos certeza e confiança da nossa entrega, no entanto, e não corrermos riscos, precisaremos de _testes automatizados_ que garantam isso!

O nome deste teste **deve** ser `test_counter`, e ele deve garantir que atenda estas especificações:

- **Chamar** a função `count_ocurrences` passando dois parâmetros:
  - `path` uma string com o caminho do arquivo (`src/jobs.csv`);
  - `word` uma string com a palavra a ser contabilizada.
- Garantir que a função retorna corretamente a quantidade de ocorrências da palavra solicitada
  - A contagem de palavras deve ser _case insentitive_, ou seja, não diferenciar letras maiúsculas de minúsculas

### _Solução_

![carbon (12)](https://user-images.githubusercontent.com/20843662/201548598-0ee1936b-93a1-460b-aeaa-2638782ddae8.png)

</details>

## 11 - Implemente um teste para a função `read_brazilian_file`

> **Implemente em:** [`tests/brazilian/test_brazilian_jobs.py`](https://github.com/tcorrea/trybe-job-insights/blob/main/tests/brazilian/test_brazilian_jobs.py)

<details>
  <summary>Expandir</summary>

A empresa cliente analisa relatórios em inglês, porém agora ela quer expandir seus negócios aqui para o Brasil e deseja analisar relatórios em português também. No entanto, as chaves do `dict` que usamos pra organizar os dados **devem** continuar em inglês. Ou seja: para gerar o relatório, deveremos ler as chaves em português e traduzi-las para inglês para povoar os nossos dados.

Nossa equipe já implementou essa função, a `read_brazilian_file`, na qual adotamos a estratégia de chamar o método original `read`, que implementamos no `requisito 1`, e depois traduzimos as chaves para o inglês. Agora precisamos criar testes para ter certeza que esta tudo certo!

O nome deste teste **deve** ser `test_brazilian_jobs`, e ele deve garantir que atenda as seguintes especificações:

- **Chamar** a função `read_brazilian_file` e ela deve receber um parâmetro:
  - `path` que é uma string com o caminho do arquivo csv em português (`tests/mocks/brazilians_jobs.csv`);
  - Retorna uma lista de dicionários com as chaves em inglês

### _Solução_

![carbon (13)](https://user-images.githubusercontent.com/20843662/201548735-a001c376-ad02-4641-81e2-99d0b4816b14.png)

</details>

## 12 - Implemente um teste para a função `sort_by`

> **wip:** //TODO

## 13 - (`Bônus`) Implemente a página de um job

> **Implemente em:** [`src/routes_and_views.py`](https://github.com/tcorrea/trybe-job-insights/blob/main/src/routes_and_views.py)

<details>
  <summary>Expandir</summary>

Para fechar com chave de ouro, que tal testar o quanto você consegue aprender de Flask apenas vendo como fizemos as páginas de `index` e de `jobs`, e tentar criar uma página que irá exibir todas as informações de um job em específico?

- A função deve ser decorada com a rota `/job/<index>`.
- A função deve receber um parâmetro `index`.
- A função deve chamar a `read` para ter uma lista com todos os jobs.
- A função deve chamar a `get_job`, declarada no arquivo `src/more_insights.py`, para selecionar um job específico pelo `index`.
- A função deve renderizar o template `job.jinja2`, passando um parâmetro `job` contendo o job retornado pela `get_job`.

### _Solução_

![carbon (14)](https://user-images.githubusercontent.com/20843662/201548938-d67c3f60-6362-49ca-91e9-bcf87b0d7374.png)

</details>

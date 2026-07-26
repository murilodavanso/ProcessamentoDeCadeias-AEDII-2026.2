# Processamento de Cadeias — AED II — 2026.2

Projeto em grupo desenvolvido durante o segundo quadrimestre de 2026 para a disciplina de **Algoritmos e Estruturas de Dados II**, da Universidade Federal do ABC — UFABC.

## Descrição do projeto

Este projeto implementa uma aplicação de **casamento de cadeias** voltada à busca de padrões em sequências de nucleotídeos.

A aplicação utiliza dois algoritmos:

* **Força Bruta**
* **Knuth-Morris-Pratt — KMP**

Os dois algoritmos são executados sobre os mesmos arquivos de entrada e os mesmos padrões de busca. Durante a execução, são coletadas informações como:

* quantidade de ocorrências encontradas;
* posições das ocorrências;
* número de comparações realizadas;
* tempo de execução.

A explicação teórica dos algoritmos, a metodologia dos experimentos, a análise dos resultados e as conclusões são apresentadas no relatório do trabalho. Este README tem como foco a estrutura e o funcionamento do repositório.

## Tecnologias utilizadas

* Python 3
* Pandas
* JSON
* CSV

## Estrutura do repositório

```text
ProcessamentoDeCadeias-AEDII-2026.2/
├── algoritmos/
│   ├── ForcaBruta.py
│   └── KMP.py
├── input/
│   ├── GenBank.txt
│   ├── LargeGenerated.txt
│   ├── MediumGenerated.txt
│   ├── NCBI.txt
│   ├── SmallGenerated.txt
│   └── VeryLargeGenerated.txt
├── out/
│   ├── forcaBruta/
│   └── kmp/
├── main.py
├── padroes.json
└── README.md
```

## Organização dos arquivos

### `algoritmos/`

Contém as implementações dos algoritmos de casamento de cadeias.

#### `ForcaBruta.py`

Implementa a busca por força bruta.

O algoritmo testa o padrão a partir de cada posição possível do texto. Em cada tentativa, os caracteres são comparados até que o padrão seja encontrado completamente ou seja identificada uma diferença.

#### `KMP.py`

Implementa o algoritmo Knuth-Morris-Pratt.

O algoritmo utiliza o vetor LPS para reaproveitar informações de comparações anteriores e evitar que o índice do texto retorne após uma diferença.

Cada algoritmo retorna:

* as posições iniciais das ocorrências encontradas;
* o número de comparações realizadas.

### `input/`

Contém os arquivos de entrada utilizados nos experimentos:

```text
input/GenBank.txt
input/LargeGenerated.txt
input/MediumGenerated.txt
input/NCBI.txt
input/SmallGenerated.txt
input/VeryLargeGenerated.txt
```

Cada arquivo contém uma sequência de nucleotídeos que será utilizada como texto durante as buscas.

A aplicação processa automaticamente todos os arquivos com extensão `.txt` presentes nessa pasta.

### `padroes.json`

Contém os padrões que serão procurados nos arquivos de entrada.

Exemplo:

```json
{
  "padroes": [
    "ACG",
    "GCTA",
    "ACACAG"
  ]
}
```

Cada padrão é buscado em todos os arquivos da pasta `input/`, utilizando os dois algoritmos.

### `out/`

Contém os arquivos gerados durante a execução dos experimentos.

Os resultados são separados por algoritmo:

```text
out/
├── forcaBruta/
└── kmp/
```

Cada arquivo de entrada gera um arquivo CSV correspondente em cada uma das pastas.

Exemplo:

```text
Entrada:
input/GenBank.txt

Saídas:
out/forcaBruta/resultados_GenBank.csv
out/kmp/resultados_GenBank.csv
```

### `main.py`

É o ponto de entrada da aplicação e coordena o fluxo dos experimentos.

Suas principais responsabilidades são:

1. carregar os padrões definidos em `padroes.json`;
2. localizar os arquivos da pasta `input/`;
3. carregar as sequências;
4. executar os algoritmos de força bruta e KMP;
5. medir o tempo de execução;
6. registrar as métricas;
7. validar os resultados encontrados;
8. gerar os arquivos CSV.

A lógica dos algoritmos permanece separada nos arquivos de `algoritmos/`, enquanto a `main` é responsável apenas pela coordenação das execuções.

## Fluxo de execução

O funcionamento geral da aplicação é:

```text
padroes.json
      │
      ▼
Carregamento dos padrões
      │
      ▼
Leitura dos arquivos de input/
      │
      ├───────────────┐
      ▼               ▼
Força Bruta          KMP
      │               │
      └───────┬───────┘
              ▼
Coleta e validação dos resultados
              │
              ▼
Geração dos arquivos CSV
```

Para cada arquivo de entrada, todos os padrões são executados pelos dois algoritmos.

## Métricas registradas

Cada linha dos arquivos CSV representa a execução de um algoritmo para um padrão específico.

As colunas podem incluir:

| Coluna               | Descrição                             |
| -------------------- | ------------------------------------- |
| `Algoritmo`          | Algoritmo utilizado                   |
| `Tamanho Texto (N)`  | Tamanho da sequência de entrada       |
| `Tamanho Padrão (M)` | Tamanho do padrão buscado             |
| `Padrão`             | Cadeia procurada                      |
| `Total Ocorrências`  | Quantidade de ocorrências encontradas |
| `Primeiras Posições` | Primeiras posições encontradas        |
| `Nº Comparações`     | Número de comparações realizadas      |
| `Tempo (ms)`         | Tempo de execução em milissegundos    |

## Validação dos resultados

Os dois algoritmos devem encontrar exatamente as mesmas ocorrências para cada combinação entre texto e padrão.

A aplicação pode comparar diretamente as listas de posições retornadas:

```python
posicoes_forca_bruta == posicoes_kmp
```

Caso os resultados sejam diferentes, a execução deve indicar o arquivo e o padrão que apresentaram divergência.

Essa validação garante que a comparação de desempenho seja realizada apenas entre implementações funcionalmente equivalentes.

## Requisitos

Para executar o projeto, é necessário possuir:

* Python 3
* pip
* Pandas

A dependência pode ser instalada com:

```bash
pip install pandas
```

## Como executar

Clone o repositório:

```bash
git clone https://github.com/murilodavanso/ProcessamentoDeCadeias-AEDII-2026.2.git
```

Entre na pasta do projeto:

```bash
cd ProcessamentoDeCadeias-AEDII-2026.2
```

Execute o programa a partir da raiz do repositório:

```bash
python main.py
```

Em alguns sistemas, pode ser necessário utilizar:

```bash
python3 main.py
```

Ao final da execução, os resultados serão armazenados nas pastas:

```text
out/forcaBruta/
out/kmp/
```

## Integrantes

* Murilo Davanso
* Leonardo Jae Yong Noh
* Guilherme Augusto Carvalho Eira
* Vinicius de Oliveira Bezerra
* Victor Martim Nascimento
* Rafael Rezende Pereira
* Matheus Fernandes Rafaini

## Links relevantes

[Drive do Grupo](https://drive.google.com/drive/folders/1YdYvQaHChox5Pv2v3E1uvA9Lpn-S4YQU)
[Grupos do Trabalho](https://drive.google.com/file/d/1oabsE2WDMPJW9bNbE6jfybiC02nDUEME/view)
[Normas do Trabalho](https://drive.google.com/file/d/1a8c5C__9V2yIGJhoP0glYj6S5KH1WJyX/view)

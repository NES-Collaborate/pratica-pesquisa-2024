# Índice

1. [Introdução ao Pandas](#1)
2. [Criação de DataFrames](#2)
   - [A partir de dicionários](#2.1)
   - [A partir de listas](#2.2)
   - [A partir de arrays NumPy](#2.3)
   - [A partir de arquivos (CSV, Excel, JSON)](#2.4)
3. [Visualização e Exploração de Dados](#3)
   - [Visualização rápida dos dados](#3.1)
   - [Informações do DataFrame](#3.2)
   - [Estatísticas descritivas](#3.3)
4. [Seleção e Indexação de Dados](#4)
   - [Seleção com colchetes](#4.1)
   - [Seleção com `loc` e `iloc`](#4.2)
   - [Seleção com `at` e `iat`](#4.3)
5. [Filtragem de Dados](#5)
   - [Filtragem básica](#5.1)
   - [Filtragem com múltiplas condições](#5.2)
   - [Uso do método `query`](#5.3)
6. [Manipulação de Dados](#6)
   - [Adicionar e remover colunas](#6.1)
   - [Renomear colunas](#6.2)
   - [Alterar tipos de dados](#6.3)
7. [Aplicação de Funções](#7)
   - [Uso de `apply`](#7.1)
   - [Uso de `map`](#7.2)
   - [Uso de `applymap`](#7.3)
8. [Trabalhando com Dados Ausentes](#8)
   - [Identificação de valores nulos](#8.1)
   - [Remoção de valores nulos](#8.2)
   - [Substituição de valores nulos](#8.3)
9. [Remoção de Duplicatas](#9)
   - [Identificar duplicatas](#9.1)
   - [Remover duplicatas](#9.2)
10. [Agrupamento e Agregação de Dados](#10)
    - [Uso de `groupby`](#10.1)
    - [Funções de agregação](#10.2)
11. [Ordenação de Dados](#11)
    - [Ordenação com `sort_values`](#11.1)
    - [Ordenação com `sort_index`](#11.2)
12. [Combinação de DataFrames](#12)
    - [Concatenação com `concat`](#12.1)
    - [Mesclagem com `merge`](#12.2)
    - [Junção com `join`](#12.3)
13. [Entrada e Saída de Dados](#13)
    - [Leitura de arquivos](#13.1)
    - [Escrita de arquivos](#13.2)
14. [Operações Avançadas](#14)
    - [Uso de `pivot_table`](#14.1)
    - [Trabalhando com índices hierárquicos (MultiIndex)](#14.2)
15. [Parâmetro `axis` em Operações](#15)
    - [Entendendo `axis=0` e `axis=1`](#15.1)
    - [Aplicações práticas](#15.2)

---

<a id="1"></a>

## 1. Introdução ao Pandas

Pandas é uma biblioteca poderosa para manipulação e análise de dados em Python. Ela fornece estruturas de dados flexíveis e expressivas, tornando o trabalho com dados tabulares e séries temporais mais fácil.

### Como começar:

```python
import pandas as pd
```

Pandas permite o uso de dois tipos principais de estruturas de dados:

- **Series**: um array unidimensional.
- **DataFrame**: uma estrutura bidimensional (tabela).

---

<a id="2"></a>

## 2. Criação de DataFrames

Existem várias formas de criar um `DataFrame` no Pandas. Vamos explorar as principais abordagens.

<a id="2.1"></a>

### 2.1 A partir de dicionários

Um dos métodos mais comuns de criar um DataFrame é a partir de dicionários.

**Exemplo 1:**

```python
data = {
    'Nome': ['Ana', 'Bruno', 'Carlos'],
    'Idade': [23, 35, 50],
    'Salário': [4000, 5000, 6000]
}
df = pd.DataFrame(data)
print(df)
```

Saída:

```text
     Nome  Idade  Salário
0     Ana     23     4000
1   Bruno     35     5000
2  Carlos     50     6000
```

**Exemplo 2:**

Incluindo índices personalizados:

```python
data = {
    'Produto': ['A', 'B', 'C'],
    'Preço': [10.5, 20.3, 15.0]
}
df = pd.DataFrame(data, index=['ID1', 'ID2', 'ID3'])
print(df)
```

Saída:

```text
    Produto  Preço
ID1       A   10.5
ID2       B   20.3
ID3       C   15.0
```

---

<a id="2.2"></a>

### 2.2 A partir de listas

DataFrames também podem ser criados a partir de listas.

**Exemplo 3:**

```python
data = [
    ['Ana', 23, 4000],
    ['Bruno', 35, 5000],
    ['Carlos', 50, 6000]
]
df = pd.DataFrame(data, columns=['Nome', 'Idade', 'Salário'])
print(df)
```

Saída:

```text
     Nome  Idade  Salário
0     Ana     23     4000
1   Bruno     35     5000
2  Carlos     50     6000
```

**Exemplo 4:**

Com índices personalizados:

```python
data = [
    [10.5, 'Categoria A'],
    [20.3, 'Categoria B'],
    [15.0, 'Categoria A']
]
df = pd.DataFrame(data, index=['Produto1', 'Produto2', 'Produto3'], columns=['Preço', 'Categoria'])
print(df)
```

Saída:

```text
          Preço    Categoria
Produto1   10.5  Categoria A
Produto2   20.3  Categoria B
Produto3   15.0  Categoria A
```

---

<a id="2.3"></a>

### 2.3 A partir de arrays NumPy

Se você já trabalha com NumPy, pode criar DataFrames diretamente a partir de arrays.

**Exemplo 5:**

```python
import numpy as np

array = np.array([
    ['Ana', 23, 4000],
    ['Bruno', 35, 5000],
    ['Carlos', 50, 6000]
])
df = pd.DataFrame(array, columns=['Nome', 'Idade', 'Salário'])
print(df)
```

Saída:

```text
     Nome Idade Salário
0     Ana    23    4000
1   Bruno    35    5000
2  Carlos    50    6000
```

---

<a id="2.4"></a>

### 2.4 A partir de arquivos (CSV, Excel, JSON)

Porém, você pode facilmente criar DataFrames lendo dados de arquivos externos.

**Exemplo 6: Leitura de CSV**

```python
df = pd.read_csv('datasets/sample.csv')
print(df.head())
```

Saída:

```text
     nome  idade          cidade   profissao
0    João     34       São Paulo  Engenheiro
1   Maria     28  Rio de Janeiro      Médica
2  Carlos     45  Belo Horizonte   Professor
3     Ana     37    Porto Alegre    Advogada
4   Pedro     30        Salvador   Arquiteto
```

**Exemplo 7: Leitura de Excel**

```python
df = pd.read_excel('datasets/sample.xlsx', sheet_name='SheetLegal')
print(df.head())
```

Saída:

```text
     nome  idade          cidade   profissao
0    João     34       São Paulo  Engenheiro
1   Maria     28  Rio de Janeiro      Médica
2  Carlos     45  Belo Horizonte   Professor
3     Ana     37    Porto Alegre    Advogada
4   Pedro     30        Salvador   Arquiteto
```

**Exemplo 8: Leitura de JSON**

```python
df = pd.read_json('datasets/sample.json')
print(df.head())
```

Saída:

```text
                                            nome  idade          cidade   profissao
0       {'primeiro': 'João', 'segundo': 'Paulo'}     34       São Paulo  Engenheiro
1     {'primeiro': 'Maria', 'segundo': 'Santos'}     28  Rio de Janeiro      Médica
2  {'primeiro': 'Carlos', 'segundo': 'Ferreira'}     45  Belo Horizonte   Professor
3      {'primeiro': 'Ana', 'segundo': 'Pereira'}     37    Porto Alegre    Advogada
4      {'primeiro': 'Pedro', 'segundo': 'Alves'}     30        Salvador   Arquiteto
```

---

<a id="3"></a>

## 3. Visualização e Exploração de Dados

Uma vez que os dados estejam carregados no DataFrame, a visualização rápida e a exploração são fundamentais para entender a estrutura dos dados.

<a id="3.1"></a>

### 3.1 Visualização rápida dos dados

É possível usar métodos como `head()` e `tail()` para visualizar as primeiras ou últimas linhas do DataFrame.

**Exemplo 9:**

```python
print(df.head())    # Primeiros 5 registros
print(df.tail(3))   # Últimos 3 registros
```

<a id="3.2"></a>

### 3.2 Informações do DataFrame

O método `info()` fornece um resumo detalhado do DataFrame.

**Exemplo 10:**

```python
print(df.info())    # Informações gerais
```

Saida com `df` definido em cima do arquivo `sample.json`:

```text
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 8 entries, 0 to 7
Data columns (total 4 columns):
 #   Column     Non-Null Count  Dtype
---  ------     --------------  -----
 0   nome       8 non-null      object
 1   idade      8 non-null      int64
 2   cidade     8 non-null      object
 3   profissao  8 non-null      object
dtypes: int64(1), object(3)
memory usage: 388.0+ bytes
```

<a id="3.3"></a>

### 3.3 Estatísticas descritivas

O método `describe()` gera estatísticas descritivas para cada coluna **numérica**.

**Exemplo 11:**

```python
print(df.describe())    # Estatísticas básicas
```

Saída com `df` definido em cima do arquivo `sample.json`:

```text
           idade
count   8.000000
mean   33.750000
std     6.453128
min    25.000000
25%    29.500000
50%    33.000000
75%    37.500000
max    45.000000
```

Outras operações úteis:

```python
# Média
print(df['idade'].mean())

# Mediana
print(df['idade'].median())

# Desvio Padrão
print(df['idade'].std())
```

Saída:

```text
33.75
33.0
6.453127702351562
```

---

<a id="4"></a>

## 4. Seleção e Indexação de Dados

Existem várias maneiras de selecionar dados em um DataFrame. Vamos explorar as principais.

<a id="4.1"></a>

### 4.1 Seleção com colchetes

A seleção com colchetes é o método mais simples.

**Exemplo 12: Selecionar coluna única**

```python
nomes = df['nome']
print(nomes)
```

Saída com `df` definido em cima do arquivo `sample.csv`:

```text
0      João
1     Maria
2    Carlos
3       Ana
4     Pedro
5     Lucas
6       Lia
7     Tânia
Name: nome, dtype: object
```

**Exemplo 13: Selecionar múltiplas colunas**

```python
dados = df[['nome', 'idade']]
print(dados)
```

Saída com `df` definido em cima do arquivo `sample.csv`:

```text
     nome  idade
0    João     34
1   Maria     28
2  Carlos     45
3     Ana     37
4   Pedro     30
5   Lucas     25
6     Lia     32
7   Tânia     39
```

---

<a id="4.2"></a>

### 4.2 Seleção com `loc` e `iloc`

O Pandas oferece dois métodos para selecionar dados: `loc` e `iloc`.

- **`loc`**: seleção baseada em rótulos (nomes).

- **`iloc`**: seleção baseada em posição numérica (índices).

Considere `df` como definido a seguir:

```python
data = {
    'Nome': ['Felipe', 'Arthur', 'Luiz', 'Edeilson'],
    'Salário': [1_999_999, 16_000, 13_000, 87_321]
}
df = pd.DataFrame(data, index=['ID1', 'ID2', 'ID3', p])
print(df)
```

Saída:

```text
         Nome  Salário
ID1    Felipe  1999999
ID2    Arthur    16000
ID3      Luiz    13000
ID4  Edeilson    87321
```

**Exemplo 14: `loc` para seleção baseada em rótulos**

```python
# Selecionar linhas de 'ID1' a 'ID2' e colunas 'Nome' e 'Salário'
df_loc = df.loc['ID1':'ID2', ['Nome', 'Salário']]
print(df_loc)
```

Saída:

```text
       Nome  Salário
ID1  Felipe  1999999
ID2  Arthur    16000
```

**Exemplo 15: `iloc` para seleção baseada em posição**

```python
# Selecionar as linhas de 1 a 3 e primeiras 2 colunas
df_iloc = df.iloc[1:3, 0:2]
print(df_iloc)
```

Saída:

```text
       Nome  Salário
ID2  Arthur    16000
ID3    Luiz    13000
```

---

<a id="4.3"></a>

### 4.3 Seleção com `at` e `iat`

Esses métodos são mais eficientes para acessar um único elemento, seja por rótulo (`at`) ou por posição (`iat`).

**Exemplo 16:**

```python
# Obter valor específico
valor = df.at[0, 'Nome']   # Equivalente a df.loc[0, 'Nome']
print(valor)
```

**Exemplo 17:**

```python
# Obter valor específico usando posições inteiras
valor = df.iat[0, 1]       # Equivalente a df.iloc[0, 1]
print(valor)
```

---

<a id="5"></a>

## 5. Filtragem de Dados

A filtragem de dados é uma operação muito comum e útil para análise.

<a id="5.1"></a>

### 5.1 Filtragem básica

Filtrar linhas com base em condições simples.

**Exemplo 18:**

```python
# Filtrar linhas onde 'Idade' > 30
df_filtrado = df[df['Idade'] > 30]
print(df_filtrado)
```

**Exemplo 19:**

```python
# Filtrar linhas onde 'Categoria' é 'Categoria A'
df_filtrado = df[df['Categoria'] == 'Categoria A']
print(df_filtrado)
```

---

<a id="5.2"></a>

### 5.2 Filtragem com múltiplas condições

Você pode combinar condições usando operadores lógicos (`&`, `|`, `~`).

**Exemplo 20:**

```python
# Filtrar onde 'Idade' > 30 e 'Salário' > 5000
df_filtrado = df[(df['Idade'] > 30) & (df['Salário'] > 5000)]
print(df_filtrado)
```

**Exemplo 21:**

```python
# Filtrar onde 'Categoria' é 'Categoria A' ou 'Preço' > 15
df_filtrado = df[(df['Categoria'] == 'Categoria A') | (df['Preço'] > 15)]
print(df_filtrado)
```

---

<a id="5.3"></a>

### 5.3 Uso do método `query`

`query()` é uma forma mais legível de aplicar condições de filtragem complexas.

**Exemplo 22:**

```python
# Usando query para filtrar dados
df_filtrado = df.query('Idade > 30 and Salário > 5000')
print(df_filtrado)
```

**Exemplo 23:**

```python
# Usando query com variável
categoria = 'Categoria A'
df_filtrado = df.query('Categoria == @categoria')
print(df_filtrado)
```

---

<a id="6"></a>

## 6. Manipulação de Dados

Manipular dados é essencial para pré-processamento e limpeza.

<a id="6.1"></a>

### 6.1 Adicionar e remover colunas

**Exemplo 24: Adicionar coluna**

```python
# Adicionar coluna 'Bonus' com 10% do salário
df['Bonus'] = df['Salário'] * 0.10
print(df)
```

**Exemplo 25: Remover coluna**

```python
# Remover coluna 'Bonus'
df_sem_bonus = df.drop('Bonus', axis=1)
print(df_sem_bonus)
```

---

<a id="6.2"></a>

### 6.2 Renomear colunas

**Exemplo 27:**

```python
# Renomear coluna 'Nome' para 'Funcionário'
df_renomeado = df.rename(columns={'Nome': 'Funcionário'})
print(df_renomeado)
```

---

<a id="6.3"></a>

### 6.3 Alterar tipos de dados

**Exemplo 29:**

```python
# Converter 'Idade' para float
df['Idade'] = df['Idade'].astype(float)
print(df.dtypes)
```

---

<a id="7"></a>

## 7. Aplicação de Funções

A aplicação de funções é fundamental para manipulação avançada de dados.

<a id="7.1"></a>

### 7.1 Uso de `apply`

O `apply()` permite aplicar funções customizadas a colunas ou linhas.

**Exemplo 31:**

```python
# Aplicar função que classifica idade
def classificar_idade(idade):
    if idade < 30:
        return 'Jovem'
    elif idade < 50:
        return 'Adulto'
    else:
        return 'Sênior'

df['Faixa Etária'] = df['Idade'].apply(classificar_idade)
print(df)
```

---

<a id="7.2"></a>

### 7.2 Uso de `map`

**Exemplo 33:**

```python
# Mapear valores em uma série
mapeamento = {'Ana': 'A', 'Bruno': 'B', 'Carlos': 'C'}
df['Iniciais'] = df['Nome'].map(mapeamento)
print(df)
```

---

<a id="7.3"></a>

### 7.3 Uso de `applymap`

**Exemplo 35:**

```python
# Aplicar função a todos os elementos do DataFrame
df_numerico = df[['Idade', 'Salário']]
df_dobro = df_numerico.applymap(lambda x: x * 2)
print(df_dobro)
```

---

<a id="8"></a>

## 8. Trabalhando com Dados Ausentes

Identificar e lidar com dados ausentes é crucial para garantir a qualidade da análise.

<a id="8.1"></a>

### 8.1 Identificação de valores nulos

**Exemplo 36:**

```python
# Verificar valores nulos
print(df.isnull())
```

---

<a id="8.2"></a>

### 8.2 Remoção de valores nulos

**Exemplo 38:**

```python
# Remover linhas com valores nulos
df_sem_nulos = df.dropna()
print(df_sem_nulos)
```

---

<a id="8.3"></a>

### 8.3 Substituição de valores nulos

**Exemplo 41:**

```python
# Preencher valores nulos com zero
df_preenchido = df.fillna(0)
print(df_preenchido)
```

---

<a id="9"></a>

## 9. Remoção de Duplicatas

Remover duplicatas é útil para evitar ruído nos dados.

<a id="9.1"></a>

### 9.1 Identificar duplicatas

**Exemplo 44:**

```python
# Verificar linhas duplicadas
duplicatas = df.duplicated()
print(duplicatas)
```

---

<a id="9.2"></a>

### 9.2 Remover duplicatas

**Exemplo 45:**

```python
# Remover linhas duplicadas
df_unico = df.drop_duplicates()
print(df_unico)
```

---

<a id="10"></a>

## 10. Agrupamento e Agregação de Dados

Agrupamento e agregação são fundamentais para análise de grandes conjuntos de dados.

<a id="10.1"></a>

### 10.1 Uso de `groupby`

**Exemplo 47:**

```python
# Agrupar por 'Faixa Etária' e contar quantos registros em cada grupo
grupo = df.groupby('Faixa Etária').size()
print(grupo)
```

---

<a id="10.2"></a>

### 10.2 Funções de agregação

**Exemplo 49:**

```python
# Usar múltiplas funções de agregação
grupo = df.groupby('Categoria').agg({'Preço': ['mean', 'min', 'max']})
print(grupo)
```

---

<a id="11"></a>

## 11. Ordenação de Dados

A ordenação é útil para visualizar ou trabalhar com os dados de forma organizada.

<a id="11.1"></a>

### 11.1 Ordenação com `sort_values`

**Exemplo 51:**

```python
# Ordenar por 'Salário' ascendente
df_ordenado = df.sort_values(by='Salário')
print(df_ordenado)
```

---

<a id="11.2"></a>

### 11.2 Ordenação com `sort_index`

**Exemplo 54:**

```python
# Ordenar pelo índice
df_ordenado = df.sort_index()
print(df_ordenado)
```

---

<a id="12"></a>

## 12. Combinação de DataFrames

Você pode combinar diferentes DataFrames de várias maneiras.

<a id="12.1"></a>

### 12.1 Concatenação com `concat`

**Exemplo 56:**

```python
# Concatenar DataFrames verticalmente
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
df_concat = pd.concat([df1, df2])
print(df_concat)
```

---

<a id="12.2"></a>

### 12.2 Mesclagem com `merge`

**Exemplo 58:**

```python
# Mesclar DataFrames com chave comum
df_esquerda = pd.DataFrame({'Chave': ['K0', 'K1', 'K2'], 'A': [1, 2, 3]})
df_direita = pd.DataFrame({'Chave': ['K0', 'K1', 'K3'], 'B': [4, 5, 6]})
df_merge = pd.merge(df_esquerda, df_direita, on='Chave', how='inner')
print(df_merge)
```

---

<a id="12.3"></a>

### 12.3 Junção com `join`

**Exemplo 60:**

```python
# Junção baseada no índice
df_esquerda = df_esquerda.set_index('Chave')
df_direita = df_direita.set_index('Chave')
df_join = df_esquerda.join(df_direita, how='inner')
print(df_join)
```

---

<a id="13"></a>

## 13. Entrada e Saída de Dados

Pandas suporta leitura e escrita de vários formatos de arquivo.

<a id="13.1"></a>

### 13.1 Leitura de arquivos

**Exemplo 61: Leitura de CSV com separador personalizado**

```python
df = pd.read_csv('dados.txt', sep='|')
print(df.head())
```

---

<a id="13.2"></a>

### 13.2 Escrita de arquivos

**Exemplo 64: Escrever CSV sem índice**

```python
df.to_csv('saida.csv', index=False)
```

---

<a id="14"></a>

## 14. Operações Avançadas

<a id="14.1"></a>

### 14.1 Uso de `pivot_table`

**Exemplo 67:**

```python
# Criar tabela dinâmica
tabela_pivot = pd.pivot_table(df, values='Salário', index='Faixa Etária', columns='Categoria', aggfunc='mean')
print(tabela_pivot)
```

---

<a id="14.2"></a>

### 14.2 Trabalhando com índices hierárquicos (MultiIndex)

**Exemplo 68:**

```python
# Criar MultiIndex
arrays = [
    ['Grupo1', 'Grupo1', 'Grupo2', 'Grupo2'],
    ['Subgrupo1', 'Subgrupo2', 'Subgrupo1', 'Subgrupo2']
]
index = pd.MultiIndex.from_arrays(arrays, names=('Grupo', 'Subgrupo'))
df_multi = pd.DataFrame({'Dados': [1, 2, 3, 4]}, index=index)
print(df_multi)
```

---

<a id="15"></a>

## 15. Parâmetro `axis` em Operações

O parâmetro `axis` define a direção na qual as operações serão aplicadas.

<a id="15.1"></a>

### 15.1 Entendendo `axis=0` e `axis=1`

- `axis=0`: Operação ao longo das linhas (por coluna).
- `axis=1`: Operação ao longo das colunas (por linha).

---

<a id="15.2"></a>

### 15.2 Aplicações práticas

**Exemplo 72: Calcular soma por coluna**

```python
# Soma dos valores por coluna
soma_colunas = df[['Idade', 'Salário']].sum(axis=0)
print(soma_colunas)
```

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

### 5.2 Filtragem com Múltiplas Condições

A filtragem com múltiplas condições em Pandas é feita combinando expressões lógicas. Você pode usar operadores como `&` (E lógico), `|` (OU lógico) e `~` (NÃO lógico) para filtrar os dados de forma mais específica. Esses operadores funcionam em nível elementar, o que significa que eles avaliam as condições para cada linha do DataFrame.

#### Operadores lógicos:

- **`&`** (E lógico): Retorna verdadeiro se **ambas** as condições forem verdadeiras.
- **`|`** (OU lógico): Retorna verdadeiro se **uma ou ambas** as condições forem verdadeiras.
- **`~`** (NÃO lógico): Inverte o valor lógico (True para False, e vice-versa).

#### Importante:

- Quando você utiliza múltiplas condições, cada uma delas deve estar entre parênteses `()` para evitar problemas de precedência.
- Estes operadores não são os mesmos que os operadores lógicos do Python (`and`, `or`, `not`). O Pandas requer esses operadores elementares para vetores de dados.

#### Exemplo Explicado:

```python
# Filtrar onde 'Idade' > 30 e 'Salário' > 5000
df_filtrado = df[(df['Idade'] > 30) & (df['Salário'] > 5000)]
print(df_filtrado)
```

**Explicação**:
Aqui estamos selecionando as linhas onde a idade é maior que 30 **e** o salário é maior que 5000. Ambas as condições precisam ser verdadeiras para que a linha seja incluída no DataFrame filtrado.

#### Mais exemplos:

**Exemplo 1: Filtrando com `|` (OU lógico)**

```python
# Filtrar onde 'Categoria' é 'Categoria A' ou 'Preço' > 15
df_filtrado = df[(df['Categoria'] == 'Categoria A') | (df['Preço'] > 15)]
print(df_filtrado)
```

**Explicação**:
Neste caso, estamos selecionando as linhas onde **uma ou ambas** as condições são verdadeiras: a categoria é 'Categoria A' **ou** o preço é maior que 15.

**Exemplo 2: Filtrando com `~` (NÃO lógico)**

```python
# Filtrar todas as linhas onde a categoria NÃO é 'Categoria B'
df_filtrado = df[~(df['Categoria'] == 'Categoria B')]
print(df_filtrado)
```

**Explicação**:
Aqui estamos usando o operador `~` para inverter a condição. Ou seja, todas as linhas onde a categoria **não** é 'Categoria B' serão incluídas.

**Exemplo 3: Múltiplas condições com três critérios**

```python
# Filtrar onde 'Idade' > 25, 'Salário' > 4000 e 'Categoria' é 'Categoria A'
df_filtrado = df[(df['Idade'] > 25) & (df['Salário'] > 4000) & (df['Categoria'] == 'Categoria A')]
print(df_filtrado)
```

**Explicação**:
Aqui estamos combinando três condições: a idade deve ser maior que 25, o salário maior que 4000 e a categoria deve ser 'Categoria A'. Todas as três condições devem ser verdadeiras para que a linha seja incluída.

**Exemplo 4: Condições complexas com `&`, `|`, e `~`**

```python
# Filtrar onde 'Idade' > 30 e ('Salário' > 5000 ou 'Categoria' é 'Categoria A'), exceto 'Nome' não ser 'Ana'
df_filtrado = df[(df['Idade'] > 30) & ((df['Salário'] > 5000) | (df['Categoria'] == 'Categoria A')) & ~(df['Nome'] == 'Ana')]
print(df_filtrado)
```

**Explicação**:
Neste exemplo mais complexo, filtramos as linhas onde a idade é maior que 30 **e** ou o salário é maior que 5000 **ou** a categoria é 'Categoria A'. Além disso, também estamos excluindo as linhas onde o nome é 'Ana'.

#### Dicas práticas:

- **Uso de parênteses**: Sempre use parênteses em torno de cada condição, pois a ausência deles pode resultar em erros de precedência.
- **Clareza no código**: Em operações complexas, é útil dividir suas condições em variáveis nomeadas para tornar o código mais legível.

**Exemplo 5: Usando variáveis para tornar o código mais legível**

```python
condicao_idade = df['Idade'] > 30
condicao_salario = df['Salário'] > 5000
condicao_categoria = df['Categoria'] == 'Categoria A'

# Combinação das condições
df_filtrado = df[condicao_idade & (condicao_salario | condicao_categoria)]
print(df_filtrado)
```

**Explicação**:
Aqui, dividimos as condições em variáveis para facilitar a compreensão do filtro complexo. A vantagem de fazer isso é que o código se torna mais fácil de manter e ajustar se necessário.

#### Comparação com o método `query`:

Você também pode utilizar o método `query()` para expressar as mesmas condições de forma ainda mais legível, especialmente quando está trabalhando com condições complexas.

```python
# Usando query para fazer a mesma filtragem do Exemplo 5
df_filtrado = df.query('Idade > 30 and (Salário > 5000 or Categoria == "Categoria A")')
print(df_filtrado)
```

**Explicação**:
Usar `query()` é útil para manter seu código mais limpo e intuitivo, especialmente para quem está acostumado com SQL ou linguagens similares.

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

### 7.1 Uso de `apply`

O método `apply()` no Pandas permite aplicar funções personalizadas em colunas ou linhas de um DataFrame ou Series. Ele é extremamente flexível e pode ser utilizado para aplicar uma função em uma única coluna (ou linha), ou mesmo em múltiplas colunas se for usado com funções mais complexas.

#### Quando usar `apply()`?

- Quando você precisa de uma transformação mais complexa do que as funções embutidas do Pandas podem oferecer.
- Para aplicar funções em colunas ou linhas individualmente.
- Para usar funções definidas pelo usuário (UDFs) para transformar dados.

#### Diferença entre `apply()` e outras funções:

- **`apply()` é mais versátil**. Ele pode trabalhar tanto em colunas quanto em linhas inteiras e pode aplicar funções que retornam valores escalares ou novos DataFrames/Series.
- Pode ser usado com funções definidas pelo usuário ou lambdas.

#### Exemplo 1: Aplicar uma função para classificar idade em categorias

```python
# Função para classificar idades em grupos
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

**Explicação**:
Neste exemplo, a função `classificar_idade()` é aplicada a cada valor da coluna `Idade`. Dependendo da idade, ela retorna uma categoria (`Jovem`, `Adulto`, `Sênior`), e essa categoria é inserida em uma nova coluna chamada `Faixa Etária`.

#### Exemplo 2: Usando `apply()` para operações em múltiplas colunas

```python
# Aplicar uma função para somar 'Idade' e 'Salário'
df['Total'] = df.apply(lambda row: row['Idade'] + row['Salário'], axis=1)
print(df)
```

**Explicação**:
Aqui, a função lambda soma os valores das colunas `Idade` e `Salário` para cada linha do DataFrame. O parâmetro `axis=1` indica que estamos aplicando a função ao longo das linhas (e não das colunas).

---

### 7.2 Uso de `map`

O método `map()` é usado principalmente para substituir ou mapear valores em uma Series com base em um dicionário ou função. Ele é mais limitado que o `apply()` porque só funciona com Series e não pode ser aplicado em múltiplas colunas ou linhas. No entanto, ele é muito útil quando você deseja fazer substituições diretas de valores.

#### Quando usar `map()`?

- Quando você quer substituir valores em uma única coluna com base em um dicionário ou uma função.
- Para mapear valores de uma Series para outros valores.

#### Diferença entre `map()` e `apply()`:

- **`map()` só funciona em Series**, enquanto `apply()` pode ser usado em DataFrames ou Series.
- `map()` é mais eficiente para substituições simples, como mapear valores de uma Series para outros.

#### Exemplo 1: Mapear valores com um dicionário

```python
# Dicionário de mapeamento
mapeamento = {'Ana': 'A', 'Bruno': 'B', 'Carlos': 'C'}

# Aplicar o mapeamento
df['Iniciais'] = df['Nome'].map(mapeamento)
print(df)
```

**Explicação**:
Aqui, o método `map()` substitui os valores da coluna `Nome` com base no dicionário `mapeamento`. O nome "Ana" se torna "A", "Bruno" se torna "B", e assim por diante. Esse tipo de operação é extremamente eficiente para substituições diretas.

#### Exemplo 2: Mapear valores com uma função

```python
# Mapear com uma função lambda para deixar os nomes em maiúsculas
df['Nome Maiúsculo'] = df['Nome'].map(lambda x: x.upper())
print(df)
```

**Explicação**:
Neste exemplo, usamos `map()` com uma função lambda para converter os nomes da coluna `Nome` para letras maiúsculas. O `map()` percorre cada elemento da Series e aplica a função.

---

### 7.3 Uso de `applymap`

O `applymap()` é um método que funciona em todo o DataFrame, aplicando uma função a **cada elemento individual**. Ele é útil quando você deseja aplicar a mesma função em todos os valores de um DataFrame, coluna por coluna e linha por linha.

#### Quando usar `applymap()`?

- Quando você quer aplicar uma função em cada valor individual de um DataFrame.
- Quando você precisa transformar ou manipular todos os elementos de um DataFrame ao mesmo tempo.

#### Diferença entre `applymap()` e `apply()`:

- **`applymap()`** é específico para DataFrames, e **trabalha elemento por elemento**.
- **`apply()`** pode ser usado tanto em DataFrames quanto em Series, mas trabalha por linha ou coluna, não em elementos individuais.

#### Exemplo 1: Multiplicar todos os valores numéricos por 2

```python
# Aplicar função lambda para dobrar todos os valores no DataFrame numérico
df_numerico = df[['Idade', 'Salário']]
df_dobro = df_numerico.applymap(lambda x: x * 2)
print(df_dobro)
```

**Explicação**:
Aqui usamos `applymap()` para aplicar uma função lambda que multiplica por 2 cada valor do DataFrame `df_numerico`. Cada valor da coluna `Idade` e `Salário` é processado individualmente e multiplicado por 2.

#### Exemplo 2: Transformar todos os valores em string

```python
# Converter todos os valores do DataFrame para string
df_str = df.applymap(str)
print(df_str)
```

**Explicação**:
Neste exemplo, usamos `applymap()` para converter cada valor do DataFrame em uma string. Cada elemento, independentemente de seu tipo original, será transformado em uma string.

---

### Diferença entre `apply()`, `map()` e `applymap()`

| Método       | Escopo              | Uso Comum                                     | Funcionamento                                                                            |
| ------------ | ------------------- | --------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `apply()`    | DataFrame ou Series | Aplicar funções em colunas ou linhas inteiras | Pode trabalhar em colunas ou linhas inteiras, ideal para operações complexas.            |
| `map()`      | Series              | Substituir ou mapear valores individuais      | Trabalha apenas com Series e é ideal para substituições diretas.                         |
| `applymap()` | DataFrame           | Aplicar uma função em todos os elementos      | Aplica uma função em cada elemento de um DataFrame, ideal para manipulações elementares. |

#### Resumo:

- Use `apply()` quando precisar aplicar uma função em uma coluna ou linha inteira.
- Use `map()` quando quiser substituir valores em uma Series com base em um dicionário ou função.
- Use `applymap()` quando precisar aplicar a mesma função em cada elemento de um DataFrame.

Esses métodos são poderosos para manipular e transformar dados no Pandas e, dependendo da tarefa, um deles será mais eficiente e apropriado que os outros.

---

<a id="8"></a>

### 8. Trabalhando com Dados Ausentes

Trabalhar com dados ausentes é uma parte fundamental do pré-processamento de dados. Valores nulos ou ausentes podem ocorrer por diversos motivos, como falhas na coleta de dados ou erros de processamento. Pandas oferece uma ampla gama de métodos para identificar, remover e substituir esses valores, garantindo que sua análise seja confiável.

---

<a id="8.1"></a>

### 8.1 Identificação de Valores Nulos

Pandas fornece funções como `isnull()` e `notnull()` para identificar valores nulos. Elas retornam um DataFrame ou Series de valores booleanos, onde `True` indica que o valor é nulo (`NaN`), e `False` indica que o valor não é nulo.

#### Exemplos de Identificação de Valores Nulos:

**Exemplo 1: Verificar se existem valores nulos no DataFrame**

```python
# Verificar se há valores nulos no DataFrame
print(df.isnull())
```

**Exemplo 2: Contar o número de valores nulos por coluna**

```python
# Contar o número de valores nulos em cada coluna
print(df.isnull().sum())
```

**Exemplo 3: Verificar colunas específicas quanto a valores nulos**

```python
# Verificar valores nulos em uma coluna específica
print(df['Salário'].isnull())

# Verificar valores nulos em múltiplas colunas
print(df[['Nome', 'Idade']].isnull())
```

**Exemplo 4: Verificar valores não nulos**

```python
# Verificar onde os valores NÃO são nulos
print(df.notnull())
```

**Exemplo 5: Filtrar linhas que têm valores nulos em uma coluna específica**

```python
# Selecionar linhas onde 'Salário' está ausente (nulo)
df_nulos = df[df['Salário'].isnull()]
print(df_nulos)
```

---

<a id="8.2"></a>

### 8.2 Remoção de Valores Nulos

Pandas permite remover valores nulos de várias formas. O método mais comum é o `dropna()`, que remove linhas ou colunas onde os valores são nulos.

#### Exemplos de Remoção de Valores Nulos:

**Exemplo 1: Remover todas as linhas que contenham valores nulos**

```python
# Remover todas as linhas que contenham algum valor nulo
df_sem_nulos = df.dropna()
print(df_sem_nulos)
```

**Exemplo 2: Remover colunas que contenham valores nulos**

```python
# Remover todas as colunas que contenham algum valor nulo
df_sem_nulos_colunas = df.dropna(axis=1)
print(df_sem_nulos_colunas)
```

**Exemplo 3: Remover linhas apenas se todas as colunas tiverem valores nulos**

```python
# Remover linhas onde TODAS as colunas são nulas
df_sem_nulos_total = df.dropna(how='all')
print(df_sem_nulos_total)
```

**Exemplo 4: Remover linhas apenas se uma quantidade mínima de valores não nulos estiver presente**

```python
# Manter linhas que tenham pelo menos 2 valores não nulos
df_minimos_valores = df.dropna(thresh=2)
print(df_minimos_valores)
```

**Exemplo 5: Remover valores nulos apenas em colunas específicas**

```python
# Remover linhas onde há valores nulos apenas na coluna 'Salário'
df_sem_nulos_salario = df.dropna(subset=['Salário'])
print(df_sem_nulos_salario)
```

#### Parâmetros importantes de `dropna()`:

- **`axis=0`** (padrão): Remove valores nulos em linhas.
- **`axis=1`**: Remove valores nulos em colunas.
- **`how='any'`** (padrão): Remove a linha/coluna se **qualquer** valor for nulo.
- **`how='all'`**: Remove a linha/coluna apenas se **todos** os valores forem nulos.
- **`thresh`**: Mantém a linha/coluna se contiver ao menos um número mínimo de valores não nulos.

---

<a id="8.3"></a>

### 8.3 Substituição de Valores Nulos

Em vez de remover dados, muitas vezes é útil preencher (ou imputar) valores nulos com algum valor de substituição. Pandas permite fazer isso com o método `fillna()`.

#### Exemplos de Substituição de Valores Nulos:

**Exemplo 1: Substituir valores nulos por zero**

```python
# Substituir todos os valores nulos por 0
df_preenchido = df.fillna(0)
print(df_preenchido)
```

**Exemplo 2: Substituir valores nulos com a média de uma coluna**

```python
# Preencher os valores nulos na coluna 'Salário' com a média dos salários
df['Salário'] = df['Salário'].fillna(df['Salário'].mean())
print(df)
```

**Exemplo 3: Substituir valores nulos com o valor anterior (preenchimento forward)**

```python
# Preencher valores nulos com o valor da linha anterior
df_preenchido = df.fillna(method='ffill')
print(df_preenchido)
```

**Exemplo 4: Substituir valores nulos com o próximo valor válido (preenchimento backward)**

```python
# Preencher valores nulos com o próximo valor válido
df_preenchido = df.fillna(method='bfill')
print(df_preenchido)
```

**Exemplo 5: Substituir valores nulos em colunas específicas**

```python
# Preencher valores nulos na coluna 'Salário' com 5000 e na coluna 'Idade' com a média da coluna
df_preenchido = df.fillna({'Salário': 5000, 'Idade': df['Idade'].mean()})
print(df_preenchido)
```

#### Parâmetros importantes de `fillna()`:

- **`value`**: Define o valor para preencher os valores nulos.
- **`method`**: Permite preenchimento com o valor anterior (`ffill`) ou próximo valor (`bfill`).
- **`inplace=False`**: Se `True`, modifica o DataFrame original em vez de retornar uma nova cópia.
- **`limit`**: Limita o número de valores nulos a preencher.

---

### Contagem de Valores Nulos

Pandas oferece formas eficientes de contar valores nulos em todo o DataFrame ou em colunas específicas.

**Exemplo 1: Contar o número total de valores nulos no DataFrame**

```python
# Contar o número total de valores nulos no DataFrame
total_nulos = df.isnull().sum().sum()
print(f'Total de valores nulos: {total_nulos}')
```

**Exemplo 2: Contar valores nulos por coluna**

```python
# Contar valores nulos em cada coluna
nulos_por_coluna = df.isnull().sum()
print(nulos_por_coluna)
```

**Exemplo 3: Contar valores nulos em colunas específicas**

```python
# Contar valores nulos apenas nas colunas 'Salário' e 'Idade'
nulos_selecionados = df[['Salário', 'Idade']].isnull().sum()
print(nulos_selecionados)
```

---

<a id="9"></a>

### 9. Remoção de Duplicatas

Remover duplicatas é uma etapa importante na limpeza de dados para evitar ruído ou distorções na análise. Linhas duplicadas podem ocorrer devido a falhas no processo de entrada de dados ou durante a combinação de diferentes conjuntos de dados. O Pandas oferece métodos fáceis e eficientes para identificar e remover essas duplicatas.

---

<a id="9.1"></a>

### 9.1 Identificar Duplicatas

O método `duplicated()` é utilizado para identificar duplicatas em um DataFrame. Ele retorna uma Series booleana indicando `True` para as linhas duplicadas e `False` para as linhas únicas. Por padrão, ele considera todas as colunas ao verificar duplicatas, mas é possível ajustar o comportamento com diferentes parâmetros.

#### Exemplos de Identificação de Duplicatas:

**Exemplo 1: Verificar todas as duplicatas no DataFrame**

```python
# Verificar linhas duplicadas no DataFrame inteiro
duplicatas = df.duplicated()
print(duplicatas)
```

**Exemplo 2: Verificar duplicatas com base em colunas específicas**

```python
# Verificar duplicatas apenas com base na coluna 'Nome'
duplicatas = df.duplicated(subset=['Nome'])
print(duplicatas)
```

**Exemplo 3: Considerar apenas a primeira ocorrência como única**

```python
# Verificar duplicatas, mantendo a primeira ocorrência
duplicatas = df.duplicated(keep='first')
print(duplicatas)
```

**Exemplo 4: Considerar apenas a última ocorrência como única**

```python
# Verificar duplicatas, mantendo a última ocorrência
duplicatas = df.duplicated(keep='last')
print(duplicatas)
```

**Exemplo 5: Marcar todas as ocorrências duplicadas como `True`**

```python
# Verificar duplicatas, marcando todas as ocorrências duplicadas como True
duplicatas = df.duplicated(keep=False)
print(duplicatas)
```

#### Parâmetros úteis do `duplicated()`:

- **`subset`**: Define as colunas a serem consideradas na verificação de duplicatas.
- **`keep='first'`** (padrão): Marca todas as duplicatas como `True`, exceto a primeira ocorrência.
- **`keep='last'`**: Marca todas as duplicatas como `True`, exceto a última ocorrência.
- **`keep=False`**: Marca todas as ocorrências duplicadas como `True`.

---

<a id="9.2"></a>

### 9.2 Remover Duplicatas

O método `drop_duplicates()` remove as linhas duplicadas de um DataFrame. Assim como no `duplicated()`, você pode especificar se deseja manter a primeira ou última ocorrência de cada valor duplicado.

#### Exemplos de Remoção de Duplicatas:

**Exemplo 1: Remover todas as duplicatas, mantendo a primeira ocorrência**

```python
# Remover linhas duplicadas, mantendo a primeira ocorrência
df_unico = df.drop_duplicates()
print(df_unico)
```

**Exemplo 2: Remover duplicatas, mantendo apenas a última ocorrência**

```python
# Remover duplicatas, mantendo a última ocorrência
df_unico = df.drop_duplicates(keep='last')
print(df_unico)
```

**Exemplo 3: Remover todas as duplicatas sem manter nenhuma ocorrência**

```python
# Remover todas as duplicatas, mantendo apenas linhas 100% únicas
df_unico = df.drop_duplicates(keep=False)
print(df_unico)
```

**Exemplo 4: Remover duplicatas com base em colunas específicas**

```python
# Remover duplicatas com base apenas na coluna 'Nome'
df_unico_nome = df.drop_duplicates(subset=['Nome'])
print(df_unico_nome)
```

#### Parâmetros importantes do `drop_duplicates()`:

- **`subset`**: Especifica as colunas nas quais verificar duplicatas.
- **`keep='first'`** (padrão): Mantém a primeira ocorrência e remove as duplicatas subsequentes.
- **`keep='last'`**: Mantém a última ocorrência e remove as anteriores.
- **`keep=False`**: Remove todas as duplicatas, sem manter nenhuma ocorrência.
- **`inplace=False`**: Se `True`, modifica o DataFrame original, sem retornar uma nova cópia.

---

### Contar Duplicatas

Antes de remover duplicatas, pode ser útil contar quantas linhas duplicadas existem no DataFrame. Isso pode ser feito utilizando o método `duplicated()` em combinação com `sum()`.

**Exemplo 5: Contar o número de linhas duplicadas**

```python
# Contar o número de linhas duplicadas no DataFrame
num_duplicatas = df.duplicated().sum()
print(f'Número de duplicatas: {num_duplicatas}')
```

**Exemplo 6: Contar duplicatas com base em colunas específicas**

```python
# Contar duplicatas com base na coluna 'Nome'
num_duplicatas_nome = df.duplicated(subset=['Nome']).sum()
print(f'Número de duplicatas na coluna "Nome": {num_duplicatas_nome}')
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

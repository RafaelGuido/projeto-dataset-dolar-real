# Projeto

## Visualização da Informação

### Esse projeto consiste em apresentar uma implementação, em Python, da visualização de informações presentes em um dataset usando ao menos três técnicas.

## Passo a passo

### Instalar o Python e VSCode:

- [python.org](https://www.python.org)
- [code.visualstudio.com](https://code.visualstudio.com)

### Instalar Extensões Necessárias no VSCode:

- Instale a extensão "Python" da Microsoft.

### Criar um Novo Projeto:

- Crie uma nova pasta para o projeto em seu computador.
- Abra essa pasta no VSCode.

### Configurar um Ambiente Virtual (opcional, mas recomendado):

- Abra o terminal integrado no VSCode.
- Navegue até a pasta do projeto e crie um ambiente virtual: 
  ```sh
  python -m venv venv
  ```
- Ative o ambiente virtual no Windows: 
  ```sh
  .\venv\Scripts\activate
  ```
- Ative o ambiente virtual no MacOS/Linux: 
  ```sh
  source venv/bin/activate
  ```

### Instalar as Bibliotecas Necessárias:

- Com o ambiente virtual ativado, instale as bibliotecas necessárias usando o terminal:
  ```sh
  pip install pandas matplotlib seaborn plotly networkx geopandas
  ```

### Criar o Arquivo de Código:

- Crie um novo arquivo Python (.py) na pasta do projeto. Por exemplo, `visualization_project.py`.

### Escrever o Código de Visualização:

- Copie e cole o exemplo de código fornecido no arquivo `visualization_project.py`.

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import networkx as nx
import geopandas as gpd

# Carregar o dataset
file_path = 'Dataset_USD_BRL.csv'
dataset = pd.read_csv(file_path)

# Converter a coluna de data para datetime
dataset['Data'] = pd.to_datetime(dataset['Data'], format='%d.%m.%Y')

# Ordenar o dataset por data
dataset = dataset.sort_values('Data')

# Visualização de Informação Temporal (gráfico de linhas)
plt.figure(figsize=(12, 6))
plt.plot(dataset['Data'], dataset['USD_BRL'], marker='o')
plt.title('Variação da Taxa de Câmbio USD/BRL ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Taxa de Câmbio USD/BRL')
plt.grid(True)
plt.show()

# Visualização com gráficos da Estatística Descritiva (gráfico de linhas)
plt.figure(figsize=(12, 6))
sns.lineplot(x='Data', y='USD_BRL', data=dataset)
plt.title('Variação da Taxa de Câmbio USD/BRL ao Longo do Tempo (Seaborn)')
plt.xlabel('Data')
plt.ylabel('Taxa de Câmbio USD/BRL')
plt.grid(True)
plt.show()

# Visualização com gráficos interativos (Plotly)
fig = px.line(dataset, x='Data', y='USD_BRL', title='Variação da Taxa de Câmbio USD/BRL ao Longo do Tempo (Plotly)')
fig.show()
```

### Executar o Código:

- No terminal integrado do VSCode, certifique-se de que seu ambiente virtual está ativado.

- Execute o arquivo de código:
  ```sh
  python visualization_project.py
  ```

### Considerações finais:

- O dataset utilizado contém dados históricos da taxa de câmbio USD/BRL, com as seguintes colunas:
  - **Data**: A data da observação no formato `dd.mm.yyyy`.
  - **USD_BRL**: A taxa de câmbio entre o dólar americano (USD) e o real brasileiro (BRL).

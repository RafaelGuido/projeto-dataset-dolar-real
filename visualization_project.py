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
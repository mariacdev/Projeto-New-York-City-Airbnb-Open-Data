import pandas as pd
import numpy as np
import plotly.express as px
import folium
from matplotlib import pyplot as plt

data = pd.read_csv('/content/AB_NYC_2019.csv')
data.head()

# selecionar a coluna price
price = data.loc[:, 'price']
# calcular o valor medio do preco
valor_medio = np.mean( price )
# mostrar os valores
print( 'O valor medio eh:' )
print( valor_medio )
# Resposta: U$ 152.72

# selecionar a coluna região
regioes = data.loc[:, 'neighbourhood_group']
# selecionar a coluna neighbourhood_group
regioes_unicas = pd.unique( regioes )
regioes_unicas
# Resposta: 'Brooklyn', 'Manhattan', 'Queens', 'Staten Island', 'Bronx'

# selecionar a coluna price
price = data.loc[:, 'price']
# selecionar a coluna região
price = np.max( price )
# Resposta: U$ 10.000

# selecionar o tipo de sala
room_type = data.loc[:, 'room_type']
# mostrar os valores únicos
room_type_unique = np.unique( room_type )
# mostrar os valores
print( 'As categorias são:' )
print( room_type_unique )
# Resposta: 'Entire home/apt', 'Private room', 'Shared room'

# selecionar a coluna host id
data.loc[:, 'host_id']
# selecionar a coluna neighbourhood_group
host_id = data.loc[:, 'host_id']
host_id_unique = np.unique( host_id )
len( host_id_unique )
# Resposta: 37.457 hosts únicos

# selecionar a coluna price
price = data.loc[:, 'price']
# calcular o desvio padrão
desvio_padrao = np.std( price )
desvio_padrao
# Resposta: Os preços estão disperson em U$ 240.15 em torno da média

# selecionar a coluna price e filtrar linhas
linhas = data.loc[:, 'price'] < 1250
price = data.loc[linhas, 'price']
# desenhar o histograma
plt.hist( price, bins=12);
# Resposta: Existem mais de 20.000 imóveis com valor de aluguel de até U$ 100,00

# selecionar a coluna price e filtrar linhas
linhas = data.loc[:, 'number_of_reviews'] < 300
number_reviews = data.loc[linhas, 'number_of_reviews']
# desenhar o histograma
plt.hist( price, bins=12);
# Resposta: Existem quase 30.000 imóveis com até 10 avaliações.

# Selecionando as linhas e colunas
colunas = ['price', 'neighbourhood_group']
colunas_groupby = ['neighbourhood_group']
# Criando os segmentos
data_plot = data.loc[:, colunas].groupby(colunas_groupby).max().reset_index()
# Desenhando o gráfico
px.bar( data_plot, x='neighbourhood_group', y='price' )

# Selecionando linhas e colunas
colunas = ['price', 'neighbourhood_group', 'latitude', 'longitude']
colunas_groupby = ['neighbourhood_group']
# Criando os segmentos
data_plot = data.loc[:, colunas].groupby(colunas_groupby).max().reset_index()
# Criando a área do mapa
f = folium.Figure( width=1024, height=768 )
# Desenhando o mapa
map = folium.Map(
location=[data_plot['latitude'].mean(),
data_plot['longitude'].mean()],
zoom_start=14,
control_scale=True
)
# Adicionando os pinos nos mapas
for index, location_info in data_plot.iterrows():
   folium.Marker( [location_info['latitude'],
   location_info['longitude']],
   popup=location_info['neighbourhood_group'] ).add_to( map )
# Mostrando o mapa
map

# Selecionando linhas aleatoriamente e colunas
colunas = ['neighbourhood_group', 'room_type', 'latitude', 'longitude']
data_plot = data.loc[:, colunas].sample( 100 )
# Criando uma nova coluna chamada 'color'
data_plot.loc[:, 'color'] = 'NA'
# Selecionando as linhas do segmento
linhas_private_room = data_plot.loc[:, 'room_type'] == 'Private room'
linhas_entire_apt = data_plot.loc[:, 'room_type'] == 'Entire home/apt'
linhas_shared_room = data_plot.loc[:, 'room_type'] == 'Shared room'
# Colocando as cores para cada segmento
data_plot.loc[linhas_private_room, 'color'] = 'darkgreen'
data_plot.loc[linhas_entire_apt, 'color'] = 'darkred'
data_plot.loc[linhas_shared_room, 'color'] = 'purple'
# Criando a área do mapa
map = folium.Map()
# Adicionando os pins nos mapas
for index, location_info in data_plot.iterrows():
    folium.Marker(
    [location_info['latitude'], location_info['longitude']],
    popup=location_info[['neighbourhood_group', 'room_type']],
    icon=folium.Icon( color=location_info['color'] )
).add_to( map )
# Exibindo o mapa
map
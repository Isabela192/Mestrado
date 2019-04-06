
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mlp
import numpy as np
import matplotlib.dates as mdates
import datetime 
import matplotlib.ticker as ticker
get_ipython().run_line_magic('matplotlib', 'inline')


# ### Mexendo com dados meteorológicos (dados do dia 02/02/2017):
# 
# A seguir serão analisadas duas séries temporais de temperatura em superfície (1000 hPa) para um ponto da região de Campinas, localizada em [22°52'28.3''S 47°03'32.3''W](https://www.google.com.br/maps/place/22%C2%B052'28.3%22S+47%C2%B003'32.3%22W/@-22.8745278,-47.0589722,17z/data=!3m1!4b1!4m5!3m4!1s0x0:0x0!8m2!3d-22.8745278!4d-47.0589722) em um parque da cidade.
# 
# As séries consistem dos valores realmente medidos pela estação localizada no ponto acima (arq1) e dados de uma simulação numérica realizada utilizando o modelo regional BRAMS (arq2), numa grade de 4 km de resolução, com duração de 48 horas de integração numérica tendo sido iniciada às 00 horas do dia 01/02/2017, sendo os dados de valor inicial provindos de outro modelo numérico global (GFS) com resolução de 0,25° ou aproximadamente 25 km. O objetivo é responder a seguinte pergunta: o modelo conseguiu captar a variação diurna de temperatura medida pela estação? Se não, houve superestimativa ou subestimativa?

# In[2]:


#Dados da estação e simulação:
arq1 = 'taquaral.csv'
arq2 = '../taquaral_oge.csv'

arq3 = '../taquaral_TEB.csv'
#Nomeando as colunas dos dados da estação
col_names = ['data', 'hora', 'direcao', 'temp', 'velocidade']

#Lendo os dados da estação
df1 = pd.read_csv(arq1, sep = ';', skiprows= 7, names=col_names)
df1 = df1.dropna()

#lendo os dados da simulação
df2 = pd.read_csv(arq2, sep = ';')
df3 = pd.read_csv(arq3, sep = ';')

#Mudando vírgula pra ponto nos dados da estação
df1.temp = df1.temp.apply(lambda x: str(x.replace(',','.')))

#convertendo o objeto em float
df1.temp = df1.temp.astype(float)

#juntando os dois conjuntos:

df1['temp_oge'] = df2['TEMP']
df1['temp_TEB'] = df3['TEMP']

df1


# In[3]:


df1['Timestamp'] = df1['data'] + ' ' + df1['hora']
df1['Timestamp'] = pd.to_datetime(df1['Timestamp'], format = '%d/%m/%Y %H:%M')
df1.drop(labels = ['data', 'hora'], axis=1)


# ### Análise das séries temporais
# 
# Abaixo está o gráfico de temperatura para ambos os dados

# In[13]:


mlp.style.use('ggplot')
fig, axes = plt.subplots(figsize = (10,5), dpi=255)
df1.plot.line(x = 'Timestamp', style = 'green', y = 'temp', ax = axes, title = 'Taquaral - Campinas', 
              ylim = [18, 36], fontsize = 12, label = 'Temperatura Estação')

df1.plot.line(x = 'Timestamp', y = 'temp_oge', ax = axes, label = 'Temperatura Urb off', style ='royalblue')
df1.plot.line(x = 'Timestamp', y = 'temp_TEB', ax = axes, label = 'Temperatura Urb on', style='orange')

plt.xlabel('Hora')
plt.ylabel('Temperatura (°C)')
plt.tight_layout()

plt.savefig('campinas.png')


# Analisando o gráfico acima, conclui-se que o modelo superestima a temperatura durante a simulação, poŕem, ela acompanha o ciclo medido pela estação, apresentando temperatura máxima medida no dia para o horário das 12 horas.
# Interessante notar que por volta das 16 horas, há uma diminuição da temperatura medida pela estação, isso pode estar relacionado com a entrada de um ar mais frio ou falha de instrumentação.

# In[9]:


#Dados da estação e simulação:
arq1 = '../iag.csv'
arq2 = '../sp_oge.csv'
arq3 = '../sp_TEB.csv'

#Nomeando as colunas dos dados da estação
col_names = ['data', 'hora', 'temp']

#Lendo os dados da estação
df1 = pd.read_csv(arq1, sep = ';', skiprows=1, names=col_names)
df1 = df1.dropna()

#lendo os dados da simulação
df2 = pd.read_csv(arq2, sep = ';')
df3 = pd.read_csv(arq3, sep = ';')

#convertendo o objeto em float
#df1.temp = df1.temp.astype(float)

#juntando os dois conjuntos:

df1['temp_oge'] = df2['TEMP']
df1['temp_TEB'] = df3['TEMP']

df1


# In[10]:


df1['Timestamp'] = df1['data'] + ' ' + df1['hora']
df1['Timestamp'] = pd.to_datetime(df1['Timestamp'], format = '%d/%m/%Y %H:%M')
df1.drop(labels = ['data', 'hora'], axis=1)


# In[11]:


mlp.style.use('ggplot')
fig, axes = plt.subplots(figsize = (10,5), dpi=255)
df1.plot.line(x = 'Timestamp', style = 'green', y = 'temp', ax = axes, title = 'Estação Água Funda - São Paulo', 
              ylim = [18, 36], fontsize = 12, label = 'Temperatura Estação')

df1.plot.line(x = 'Timestamp', y = 'temp_oge', ax = axes, label = 'Temperatura Urb off', style ='royalblue')
df1.plot.line(x = 'Timestamp', y = 'temp_TEB', ax = axes, label = 'Temperatura Urb on', style='orange')

plt.xlabel('Hora')
plt.ylabel('Temperatura (°C)')
plt.tight_layout()

plt.savefig('saopaulo.png')


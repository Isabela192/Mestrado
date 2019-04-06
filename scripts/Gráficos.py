
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mlp
import numpy as np
import matplotlib.dates as mdates
import datetime 
get_ipython().run_line_magic('matplotlib', 'inline')


# ### Fazendo a leitura dos dados:
# 
# **Alguns dados não tem valores de temperatura**
# 
# Por isso é melhor deixar pra renomear em outra célula
# 
# Estações **COM** temperatura: [Araraquara, Bauru, Sorocaba, Guarulho-Paço Municipal, Ibirapuera, Pinheiros, Jundiaí, Taubaté, S. José dos Campos]
# 
# Estações **SEM** temperatura: Santana, Santo Amaro, 
# 
# Estações **SEM** anemometro: Sorocaba

# In[2]:


arq1 = '02022017/araraquara.csv'
arq2 = '02022017/taquaral.csv'
arq3 = '02022017/sorocaba.csv'
arq4 = '02022017/jundiai.csv'

#Para séries com teperatura:
col_names = ['data', 'hora', 'direcao', 'temp', 'velocidade']
#Para séries sem temperatura
col_names2 = ['data', 'hora', 'temp']

df1 = pd.read_csv(arq1, sep = ';', skiprows= 7, names=col_names)
df1 = df1.dropna()

df2 = pd.read_csv(arq2, sep=';', skiprows=7, names=col_names)
df2 = df2.dropna()

df3 = pd.read_csv(arq3, sep=';', skiprows=7, names=col_names2)
df3 = df3.dropna()

df4 = pd.read_csv(arq4, sep=';', skiprows=7, names=col_names)
df4 = df4.dropna()

#Mudando vírgula pra ponto por razões...
df1.temp = df1.temp.apply(lambda x: str(x.replace(',','.')))
df1.velocidade = df1.velocidade.apply(lambda x: str(x.replace(',','.')))

df2.temp = df2.temp.apply(lambda x: str(x.replace(',','.')))
df2.velocidade = df2.velocidade.apply(lambda x: str(x.replace(',','.')))

df3.temp = df3.temp.apply(lambda x: str(x.replace(',','.')))


df4.temp = df4.temp.apply(lambda x: str(x.replace(',','.')))
df4.velocidade = df4.velocidade.apply(lambda x: str(x.replace(',','.')))

#convertendo o objeto em float
df1.temp = df1.temp.astype(float)
df1.velocidade = df1.velocidade.astype(float)

df2.temp = df2.temp.astype(float)
df2.velocidade = df2.velocidade.astype(float)

df3.temp = df3.temp.astype(float)

df4.temp = df4.temp.astype(float)
df4.velocidade = df4.velocidade.astype(float)


# ### Gráficos
# 
# CAMPINAS

# In[3]:


mlp.style.use('ggplot')
fig, axes = plt.subplots(2,2, figsize = (10,5))
df1.plot.line(x = 'hora', y = 'temp', ax = axes[0,0], title = 'Araraquara', ylim = [19, 30])
df2.plot.line(x = 'hora', y = 'temp', ax = axes[0,1], title = 'Campinas', ylim = [19, 30])
df3.plot.line(x = 'hora', y = 'temp', ax = axes[1,0], title = 'Sorocaba', ylim = [19, 30])
df4.plot.line(x='hora', y= 'temp', ax=axes[1,1], title = 'Jundiaí', ylim = [19, 30])
plt.tight_layout()


# ### Gráficos
# São Paulo dia 22/02/2017

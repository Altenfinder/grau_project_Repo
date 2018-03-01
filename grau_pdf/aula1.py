# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,53,34,45,64,34],
             'Bounce_rate':[65,72,62,64,54,66]}

df = pd.DataFrame(web_stats)
'''
style('ggplot')
#print df #imprime todo o dataFrame
#print df.head() #imprime as primeiras 5 linhas
#print df.tail() #imprime as ultimas 5 linhas
#print df.tail(2) #imprime as ultimas 2 linhas

#print df.set_index('Day')
#print df.head() python irá imprimir dataFrame sem o indice definido acima, pois quando se configura um index diferente e o printa,
#é como se outro dataframe fosse criado...
#o dataframe deve ser modificado na criação, ou setado para o indice que quiser:
df2= df.set_index('Day')
print df2.head()
#porém, um jeito mais fácil seria dar overwrite na df atual:
df.set_index('Day', inplace=True)
print df.head()

para imprimir uma coluna especifica:
print df['nomeColuna']

para referenciar multiplas colunas:
print(df[['Day','Bounce_rate']])

para converter uma coluna em uma lista:
print df.Visitors.tolist()

para exibir multiplas colunas em uma lista, deve ser criado um array, USAR numpy:
print np.array(df[['Bounce_rate','Visitors']])

transformar um array em um dF:
print pd.DataFrame(np.array(df[['Bounce_rate','Visitors']]))
'''

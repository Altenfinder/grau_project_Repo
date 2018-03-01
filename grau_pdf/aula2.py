import pandas as pd
df = pd.read_csv('/home/felipe/Downloads/DY2-I2060001265.csv')
print df.head()
#configurar indice para ser data e salvar em outro csv
df.set_index('Period_Date', inplace=True)

df.to_csv('/home/felipe/Downloads/teste.csv')

df = pd.read_csv('/home/felipe/Downloads/teste.csv', index_col = 0 )



#como renomear colunas:
df.columns = ['China_GLSS']
print df
df.to_html('/home/felipe/Downloads/exemplo.html')

'''
para dar clear no header e dar o nome que quiser as colunas:
df.to_csv('teste3.csv', header=False)
df=pd.read_csv('teste3.csv',names=['Date','China_GLSS'],index_col=0)
print df.head()

para renomear uma coluna:

'''
df.rename(columns={'China_GLSS':'5555'},inplace=True)

print df.head()

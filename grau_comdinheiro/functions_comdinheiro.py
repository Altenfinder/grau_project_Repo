import pandas as pd
import numpy as np

def isin_comdinheiro(isin):
    db = pd.read_csv('/usr/lib/python2.7/dist-packages/grau_project/grau_comdinheiro/lista_ativos_comdinheiro.csv').set_index('isin')

    if pd.notnull(isin):

        if isin in db.index:

            result = db['ticker_comdinheiro'][str(isin)]

            if isinstance(result, pd.Series):
                return result[0]
            else:
                return result

        else:
            return np.nan

    else:
        return np.nan


def formato_comdinheiro_lista_ativos(df, tipo='ativos'):

    df = df.dropna().drop_duplicates()
    df = df.reset_index(drop=True)
    lista = ''
    lista_um = ''
    for i, row in enumerate(df):
        lista = lista + '+' + df[i]
        lista_um = lista_um + '+' + '1'

    lista = lista[1:]
    lista_um = lista_um[1:]

    if tipo == 'ativos':
        return lista
    else:
        return lista_um

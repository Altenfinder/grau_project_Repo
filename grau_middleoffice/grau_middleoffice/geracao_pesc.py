import pandas as pd
from datetime import datetime, date, time
import os, sys
import xlrd



#class grau_pesc:
df_boletagem = pd.read_excel('/home/servidor/Desktop/DISTRI_SINACOR_GRAU_GESTAO_PLANNER.xls', dtype={'DATA':str, 'PAPEL':str, 'CLIENTE':str, 'QUANTIDADE':str, 'CART. LIQUIDACAO':str})
df_pesc = pd.DataFrame(columns=['column_1','column_2','column_3'])

def data():
    dia = df_boletagem['DATA'][1][0:2]
    mes = df_boletagem['DATA'][1][2:4]
    ano = df_boletagem['DATA'][1][4:8]
    data = ano + mes + dia
    return data


def column_1(df_boletagem):
    df_pesc.loc[0,'column_1'] = '00PESC0129CBLC'

    i=1
    while i < df_boletagem.shape[0]:
        df_pesc['column_1'][i] = '01' + data()+ df_boletagem['PAPEL'][i]
        i = i + 1

    df_pesc['column_1'][df_pesc['column_1'].shape[0]+1] = '99PESC0129CBLC'

    return df_pesc['column_1']


# def tipo_operacao(ativo):
dict = {'A':'OPC',
        'B':'OPC',
        'C':'OPC',
        'D':'OPC',
        'E':'OPC',
        'F':'OPC',
        'G':'OPC',
        'H':'OPC',
        'I':'OPC',
        'J':'OPC',
        'K':'OPC',
        'L':'OPC',
        'M':'OPV',
        'N':'OPV',
        'O':'OPV',
        'P':'OPV',
        'Q':'OPV',
        'R':'OPV',
        'S':'OPV',
        'T':'OPV',
        'U':'OPV',
        'V':'OPV',
        'W':'OPV',
        'X':'OPV'}

def column_2(df_boletagem):
    df_pesc.loc[0,'column_2'] = '0129' + data() + data()

    i=1
    while i < df_boletagem.shape[0]:
        codigo_negociacao = '0000000' + df_boletagem['C/V'][i] #Codigo de negociacao. Verificar as implicacoes dele na britech
        codigo_cliente = '00' + df_boletagem['CLIENTE'][i]

        quantidade = df_boletagem['QUANTIDADE'][i]
        while len(quantidade) < 15:
            quantidade = '0' + quantidade

        codigo_carteira = '216' # df_boletagem['CART. LIQUIDACAO'][i]
        codigo_cliente_custodiante = df_boletagem['CLIENTE'][i]

        while len(codigo_cliente_custodiante) < 10:
            codigo_cliente_custodiante = '0' + codigo_cliente_custodiante

        tipo_operacao = ' '
        if df_boletagem['PAPEL'][i][4] in dict:
            tipo_operacao = tipo_operacao + dict[df_boletagem['PAPEL'][i][4]]
        else: tipo_operacao = tipo_operacao + 'VIS'

        df_pesc['column_2'][i] = codigo_negociacao + codigo_cliente + quantidade + codigo_carteira + codigo_cliente_custodiante + tipo_operacao
        i = i + 1


    return df_pesc['column_2']
#print dict['X']

print column_2(df_boletagem=df_boletagem)

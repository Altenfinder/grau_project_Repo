
# encoding: 'latin-1'

#Nome: Felipe Altenfelder
#Data: 06/02/2018
#Proposito: Enviar relatorios de cotas e cdi- Coleta de informacoes
import os
import re
import pandas as pd
import numpy as np
from datetime import datetime
import sys

class grau_relatorio_pdf:
    @staticmethod
    def relatorio_parse(path, keyword):
        lines = []
        result = []
        temp_result = []
        cota=''
        cdi=''
        posi=''
        with open(path, 'rt') as in_file:

                for line in in_file:
                    lines.append(line)
                    for k in keyword:
                        if k in line:
                            temp_result = temp_result + [line]

                return temp_result

    @staticmethod
    def pdf_global(path):
        keywordType = 'GLOBAL'
        k=['COTA', 'CDI', 'Posi']
        temp_result = grau_relatorio_pdf.relatorio_parse(path='/home/felipe/Desktop/attachments/2018-1-31_16:35:53_CMD GLOBAL FIM_CARTEIRA_DIARIA_30012018.TXT',keyword=k)
        data_posicao = temp_result[0][10:-24]
        print data_posicao
        result = data_posicao+temp_result[1][2]


        re.split(r'\t+', temp_result[1].rstrip('\t'))
        re.split(r'\t+', temp_result[2].rstrip('\t'))

        with open('/home/felipe/Desktop/attachments/teste/Relatorio.csv', 'wb') as in_file:
            if(temp_result!=''):
                in_file.write(result)#escreve no arquivo csv o resultado
            #    return in_file

        df = pd.read_csv('/home/felipe/Desktop/attachments/teste/Relatorio.csv',sep='\t',header=None).dropna(axis='columns',how='all')
        #print df
        df.columns = ['Index','0','1','%_dia','%_mes','%_ano','%_6_meses','%_12_meses']
        # df.loc[(np.where(df['index']=='COTA'))]['index']

        df_cotas = pd.read_csv('/usr/lib/python2.7/dist-packages/grau_project/grau_pdf/relatorio_pdf/cotas.csv',index_col=0)

        edit_lin = df_cotas.shape[0]

        data=datetime.now()
        df_cotas.loc[edit_lin, 'nome'] = keywordType
        df_cotas.loc[edit_lin,'%_dia'] = df.loc[1, '%_dia']
        df_cotas.loc[edit_lin,'data'] = posi
        df_cotas.loc[edit_lin,'%_mes'] = df.loc[1,'%_mes']
        df_cotas.loc[edit_lin,'%_ano'] = df.loc[1,'%_ano']
        df_cotas.loc[edit_lin,'%_6_meses'] = df.loc[1,'%_6_meses']
        df_cotas.loc[edit_lin,'%_12_meses'] = df.loc[1,'%_12_meses']
        print df_cotas



        #print df_cotas
        df_cotas.to_csv('/usr/lib/python2.7/dist-packages/grau_project/grau_pdf/relatorio_pdf/cotas.csv')
        # print df

#teste
if __name__=='__main__':

    grau_relatorio_pdf.pdf_global('/home/felipe/Desktop/attachments/2018-1-31_16:35:53_CMD GLOBAL FIM_CARTEIRA_DIARIA_30012018.TXT')

# encoding: 'latin-1'

#Nome: Felipe Altenfelder
#Data: 07/02/2018
#Proposito: Enviar relatorios de cotas e cdi- Coleta de informacoes
import os
import re
import pandas as pd
from pandas.tseries.offsets import BDay
import numpy as np
from datetime import datetime
import sys
import numpy as np
from operator import eq
from grau_project.grau_datas import grau_datas
from dateutil import parser
import calendar
from openpyxl import Workbook
from grau_project.grau_excel.grau_excel import grau_excel
from grau_project.grau_email import grau_email



class grau_relatorio_pdf:


    @staticmethod#metodo para coletar informacoes do pdf, e arrays desejados para filtrar.
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


    @staticmethod#metodo para pdfs tipo global, filtrar informacoes.
    def pdf_global(path):
        keywordType = 'GLOBAL'
        k=['PRODUTO', 'CDI_I', 'Movimento','Patri','Tx.Adm']
        path = path.replace(" ","\ ")
        #os.system("ssconvert " +path+ " aaalo.csv")
        df = pd.read_csv('/home/felipe/aaalo.csv', index_col=0)
        temp_result = grau_relatorio_pdf.relatorio_parse(path='/home/felipe/aaalo.csv',keyword=k)


        co=0
        custo=0
        co_cust=0
        test='""lll'
        retorno_GLOBAL=['']
        retorno_GLOBAL_CDI=['']
        retorno_GLOBAL_Patri=['']
        retorno_GLOBAL_apropriada=['']
        retorno_data=['']

        for c in temp_result:
            if 'CDI' in temp_result[co]:

                retorno_GLOBAL_CDI+=(' '.join(temp_result[co].split())).split(' ')
                co+=1
            elif 'Movimento' in temp_result[co]:
                co+=1
                retorno_data+=((' '.join(temp_result[0].split())).split(' '))
            elif 'Patr'in temp_result[co]:
                retorno_GLOBAL_Patri+=((' '.join(temp_result[co].split())).split(' '))
                co+=1
            elif 'Tx.Adm' in temp_result[co]:
                retorno_GLOBAL_apropriada+=(' '.join(temp_result[co].split())).split(' ')
                co+=1
            else:
                retorno_GLOBAL+=(' '.join(temp_result[co].split())).split(' ')
                co+=1


        custo = retorno_GLOBAL_apropriada[7][13:21].replace('.','')

        custo = float(custo.replace(",",".",1).replace('"','').replace(',',''))

        data = retorno_data[4][2:12]
        nome=keywordType
        data = data.split('/')
        data_inicial = data[2]+'-'+data[1]+'-'+data[0]
        data_inicial=str(data_inicial).split('-')

        ano=int(data_inicial[0])

        if (int(data_inicial[1][0])==0):
            mes=int(data_inicial[1][1])
        else:
            mes=int(data_inicial[1])

        dia=int(data_inicial[2])

        dias_do_mes = calendar.monthrange(ano,mes)
        dias_restantes=grau_datas.dias_uteis_restantes_mes(ano,mes,dia)

        dias_uteis=grau_datas.dias_uteis_mes(ano,mes,dia)

        dias_uteis_meses=0
        for i in range(1,mes+1):
            dias_uteis_meses += grau_datas.dias_uteis_mes(ano,i,dia)
        #custo=grau_relatorio_pdf.aux_pdf(keywordType,retorno_GLOBAL_apropriada)

        cota_l_diaria= float(retorno_GLOBAL[1][13:20].replace(',','.').replace('"',''))
        cdi_diario = float(retorno_GLOBAL_CDI[1][11:17].replace(',','.').replace('"',''))
        cota_l_mensal = float(retorno_GLOBAL[1][23:29].replace(',','.').replace('"',''))
        cdi_mensal = float(retorno_GLOBAL_CDI[1][20:26].replace(',','.').replace('"',''))

        cota_anual = float(retorno_GLOBAL[1][41:47].replace(',','.').replace('"',''))
        #.replace(',','',1).replace('"','').replace(',','.')

        print cota_anual
        cdi_anual = float(retorno_GLOBAL_CDI[1][37:44].replace(',','.').replace('"',''))
        print cdi_anual
        patrimonio = retorno_GLOBAL_Patri[3][3:12].replace('.','').replace('"','')
        patrimonio = float(patrimonio.replace(',','.').replace('"',''))
        custo= custo/patrimonio





        grau_relatorio_pdf.calcular_dados_pdf(dias_uteis_meses,cota_l_diaria,cdi_diario,cota_l_mensal,cdi_mensal,cota_anual,cdi_anual,patrimonio,custo,dias_uteis,dias_restantes,data_inicial,keywordType)

    @staticmethod#metodo para calcular dados dos respectivos pdfs, para envio ao arquivo.
    def calcular_dados_pdf(dias_uteis_meses,cota_l_diaria,cdi_diario,cota_l_mensal,cdi_mensal,cota_anual,cdi_anual,patrimonio,custo,dias_uteis,dias_restantes,data,nome):
        mcdi_acum=cdi_mensal/100+(((1+cdi_diario/100)**dias_restantes)-1)
        acdi_acum=cdi_anual/100+(1+cdi_diario/100)**(252-(dias_uteis_meses-dias_restantes))-1
        mcdi_acum130=cdi_mensal/100+(((1+1.3*cdi_diario/100)**dias_restantes)-1)
        acdi_acum130=cdi_anual/100+(1+1.3*cdi_diario/100)**(252-(dias_uteis_meses-dias_restantes))-1
        cdi_DIA = (cota_l_diaria/cdi_diario)*100
        print cota_anual,cdi_anual
        cdi_ANO= (cota_anual/cdi_anual)*100
        print cdi_ANO
        cdi_acum = (cota_l_mensal/cdi_mensal)*100


        if '-' in str(cota_l_mensal):
            cota_proj= cota_l_mensal*(1+custo)
        else:
            cota_proj= cota_l_mensal*(1-custo)

        cdi_proj =  ((cota_proj/100)/mcdi_acum)*100

        alfa=cota_proj/100-mcdi_acum
        print alfa, patrimonio
        falta_cdi_100_mes=alfa*patrimonio
        falta_cdi_100_ano= ((cota_anual - (cota_anual)/(cdi_ANO/100))*patrimonio)/100

        falta_cdi_130_mes=((cota_l_mensal-1.3*cdi_mensal)*patrimonio)/100
        falta_cdi_130_ano=((cota_anual-1.3*cdi_anual)*patrimonio)/100

        alfa=alfa*100
        #formatacao

        cota_l_diaria = "%.4f" % cota_l_diaria
        cdi_DIA = "%.0f" % cdi_DIA
        cota_l_mensal = "%.4f" % cota_l_mensal
        cdi_acum = "%.0f" % cdi_acum
        cota_proj = "%.4f" % cota_proj
        cdi_proj = "%.0f" % cdi_proj
        alfa = "%.4f" % alfa
        cota_anual = "%.4f" % cota_anual
        cdi_ANO = "%.0f" % cdi_ANO
        falta_cdi_100_mes="%.2f" % falta_cdi_100_mes
        falta_cdi_130_mes="%.2f" % falta_cdi_130_mes
        falta_cdi_100_ano="%.2f" % falta_cdi_100_ano
        falta_cdi_130_ano="%.2f" % falta_cdi_130_ano

        grau_relatorio_pdf.update_relatorio_cotas(data,dias_restantes,nome, cota_l_diaria, cdi_DIA, cota_l_mensal,cdi_acum, cota_proj, cdi_proj, alfa, cota_anual,cdi_ANO, falta_cdi_100_mes, falta_cdi_130_mes, falta_cdi_100_ano, falta_cdi_130_ano)



    @staticmethod#metodo para pdfs tipo benford, filtrar informacoes.
    def pdf_benford(path):
        contador_data=0
        contador_benf=0
        co=0
        co_cust=0
        retorno_BENF=['']
        retorno_BENF_CDI=['']
        retorno_BENF_Patri=['']
        retorno_BENF_apropriada=['']
        retorno_BENF_cust=['']
        retorno_BENF_gest=['']
        custo=0
        keywordType = 'BENF'
        k=['BRUTA', 'CDI', 'Posi','PATRI','Apropriada']
        temp_result = grau_relatorio_pdf.relatorio_parse(path=path,keyword=k)

        # for c in temp_result:
        for c in temp_result:
            if 'CDI' in temp_result[co]:
                retorno_BENF_CDI+=(' '.join(temp_result[co].split())).split(' ')
                co+=1
            elif 'Posi' in temp_result[co]:
                co+=1
            elif 'PATRI'in temp_result[co]:
                retorno_BENF_Patri+=((' '.join(temp_result[co].split())).split(' '))
                co+=1
            elif 'Apropriada' in temp_result[co]:
                retorno_BENF_apropriada+=(' '.join(temp_result[co].split())).split(' ')
                co+=1

            else:
                retorno_BENF+=(' '.join(temp_result[co].split())).split(' ')
                co+=1
        result_data = temp_result[0][19:-70].split('/')
        data_inicial = result_data[2]+'-'+result_data[1]+'-'+result_data[0]
        data_inicial=str(data_inicial).split('-')
        ano=int(data_inicial[0])
        if (int(data_inicial[1][0])==0):
            mes=int(data_inicial[1][1])
        else:
            mes=int(data_inicial[1])
        dia=int(data_inicial[2])
        dias_sem_feriado=0
        dias_uteis_meses=0
        for i in range(1,mes+1):
            dias_uteis_meses += grau_datas.dias_uteis_mes(ano,i,dia)

        dias_do_mes = calendar.monthrange(ano,mes)
        dias_restantes=grau_datas.dias_uteis_restantes_mes(ano,mes,dia)
        dias_uteis=grau_datas.dias_uteis_mes(ano,mes,dia)

        custo=grau_relatorio_pdf.aux_pdf(keywordType,retorno_BENF_apropriada)

        cota_l_diaria = float(retorno_BENF[2].replace('%',''))
        cdi_diario = float(retorno_BENF_CDI[4].replace('%',''))
        cota_l_mensal = float(retorno_BENF[3].replace('%',''))
        cdi_mensal = float(retorno_BENF_CDI[5].replace('%',''))
        cota_anual = float(retorno_BENF[4].replace('%',''))
        cdi_anual = float(retorno_BENF_CDI[6].replace('%',''))
        patrimonio = float(retorno_BENF_Patri[2].replace(',',''))
        custo= custo/patrimonio


        grau_relatorio_pdf.calcular_dados_pdf(dias_uteis_meses,cota_l_diaria,cdi_diario,cota_l_mensal,cdi_mensal,cota_anual,cdi_anual,patrimonio,custo,dias_uteis,dias_restantes,data_inicial,keywordType)

    @staticmethod#metodo para calcular custos com os dados do pdf
    def aux_pdf(nome_pdf, retorno_apropriada):
        co_cust=0
        custo=0
        if 'BENF' in nome_pdf:
            for i in retorno_apropriada:
                if 'Adm' in retorno_apropriada[co_cust]:
                    custo+=float(retorno_apropriada[co_cust+2].replace('(','').replace(')','').replace(',',''))
                    co_cust+=1

                elif 'Cust' in retorno_apropriada[co_cust]:
                    custo+=float(retorno_apropriada[co_cust+2].replace('(','').replace(')','').replace(',',''))
                    co_cust+=1

                elif 'Gest' in retorno_apropriada[co_cust]:
                    custo+=float(retorno_apropriada[co_cust+2].replace('(','').replace(')','').replace(',',''))
                    co_cust+=1
                else:
                    co_cust+=1
        elif 'GLOBAL' in nome_pdf:
            for i in retorno_apropriada:
                if 'ADM' in retorno_apropriada[co_cust]:
                    custo+=float(retorno_apropriada[co_cust+5].replace('(','').replace(')','').replace(',',''))
                    co_cust+=1

                elif 'Cust' in retorno_apropriada[co_cust]:
                    custo+=float(retorno_apropriada[co_cust+2].replace('(','').replace(')','').replace(',',''))
                    co_cust+=1

                elif 'Gest' in retorno_apropriada[co_cust]:
                    custo+=float(retorno_apropriada[co_cust+2].replace('(','').replace(')','').replace(',',''))
                    co_cust+=1
                else:
                    co_cust+=1
        custo=str(custo)
        if '-' in custo:
            custo=float(custo.replace('-',''))
        else:
            custo = float(custo)
        return custo


    @staticmethod
    def verificar_linha_vazia(excel):
        io=0
        for i in range(5,1048576):
            if sheet.cell(row=i, column=1).value in [None,'None']:
                pass
            else:
                return 5 + i


    @staticmethod#metodo para coletar informacoes filtradas nos pdfs.
    def update_relatorio_cotas(data='',dias_sem_feriado='',nome='', pct_dia='', cdi_DIA='', pct_mes='',cdi_Acum='', cota_proj='', cdi_proj='', alfa='', cota_anual='',cdi_ANO='', falta_cdi_100_mes='', falta_cdi_130_mes='', falta_cdi_100_ano='', falta_cdi_130_ano=''):

        excel = grau_excel(workbook_path='/home/felipe/Desktop/attachments/teste/Relatorio.xlsx', sheet_name='Rentabilidade')

        df_cotas = pd.read_csv('/usr/lib/python2.7/dist-packages/grau_project/grau_pdf/relatorio_pdf/cotas.csv',index_col=0)
        edit_lin = df_cotas.shape[0]
        #data=datetime.now()
        df_cotas.loc[edit_lin,'data'] = str(data[2]) + '/' + str(data[1]) + '/' + str(data[0])
        df_cotas.loc[edit_lin,'Dias_Uteis_Mes'] = dias_sem_feriado
        df_cotas.loc[edit_lin, 'Fundo'] = nome
        df_cotas.loc[edit_lin,'%_dia'] = pct_dia
        df_cotas.loc[edit_lin,'%_cdi_dia'] = cdi_DIA
        df_cotas.loc[edit_lin,'%_mes'] = pct_mes
        df_cotas.loc[edit_lin,'cdi_Acum'] = cdi_Acum
        df_cotas.loc[edit_lin,'cota_proj'] = cota_proj
        df_cotas.loc[edit_lin,'cdi_proj'] = cdi_proj
        df_cotas.loc[edit_lin,'alfa'] = alfa
        df_cotas.loc[edit_lin,'%_ano'] = cota_anual
        df_cotas.loc[edit_lin,'%_cdi_ano'] = cdi_ANO
        df_cotas.loc[edit_lin,'falta_cdi_100_mes'] = falta_cdi_100_mes
        df_cotas.loc[edit_lin,'falta_cdi_100_ano'] = falta_cdi_100_ano
        df_cotas.loc[edit_lin,'falta_cdi_130_mes'] = falta_cdi_130_mes
        df_cotas.loc[edit_lin,'falta_cdi_130_ano'] = falta_cdi_130_ano

        data = str(data[2]) + '/' + str(data[1]) + '/' + str(data[0])

        df_cotas = pd.read_excel('/home/felipe/Desktop/attachments/teste/Relatorio.xlsx',index_col=0)
        row_count = df_cotas.shape[0]

        row_count+=2


        excel.value_input(row_count, 1, data)
        excel.value_input(row_count,2, dias_sem_feriado)
        excel.value_input(row_count,3, nome)
        excel.value_input(row_count,4, str(pct_dia)+'%')
        excel.value_input(row_count,5, str(cdi_DIA)+'%')
        excel.value_input(row_count,6, str(pct_mes)+'%')
        excel.value_input(row_count,7, str(cdi_Acum)+'%')
        excel.value_input(row_count,8, str(cota_proj)+'%')
        excel.value_input(row_count,9, str(cdi_proj)+'%')
        excel.value_input(row_count,10, str(alfa)+'%')
        excel.value_input(row_count,11, str(cota_anual)+'%')
        excel.value_input(row_count,12, str(cdi_ANO)+'%')
        excel.value_input(row_count,13, float(falta_cdi_100_mes))
        excel.value_input(row_count,14, float(falta_cdi_100_ano))
        excel.value_input(row_count,15, float(falta_cdi_130_mes))
        excel.value_input(row_count,16, float(falta_cdi_130_ano))

        for i in range(13,17):
         excel.format_number(i)
        grau_email.envio_email_anexo('felipe@graugestao.com.br','felipe@graugestao.com.br','Olhobagabago123','Relatorio','oi','/home/felipe/Desktop/attachments/teste/Relatorio.xlsx','relatorio.xlsx')

        #df_cotas.to_csv('/usr/lib/python2.7/dist-packages/grau_project/grau_pdf/relatorio_pdf/cotas.csv')#grava no relatorio de cotas




if __name__=='__main__':

    #grau_relatorio_pdf.pdf_global('/home/felipe/Desktop/attachments/teste/2018-1-31_16:35:53_CMD GLOBAL FIM_Carteira_Diaria_30012018.txt')
    grau_relatorio_pdf.pdf_global('/home/felipe/Downloads/40477 - GRAU GLOBALTECH FUNDO DE INVESTIMENTO MULTIMERCADO_22022018134856.xls')
    #grau_relatorio_pdf.pdf_benford('/home/felipe/Desktop/attachments/teste/CMD GRAU BENF_Carteira_Diaria_30012018.txt')
    #2018-2-1_11:29:52_CMD GRAU BENF_Carteira_Diaria_300120181.txt
    #2018-2-1_20:35:58_CMD GRAU BENF_Carteira_Diaria_31012018.txt
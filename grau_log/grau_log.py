from grau_project.grau_email import grau_email
from grau_project.grau_datas import grau_datas
import pandas as pd
from datetime import datetime
import numpy as np
import sys
import os

class grau_log:
    @staticmethod
    def get_line(file):
        return file(sys._getframe().f_lineno)
        
    @staticmethod
    def log(rotina, full_file, log_file='', error='', ):
        if log_file == '':
            log_file = '/usr/lib/python2.7/dist-packages/grau_project/grau_log/log.csv'

        df_log = pd.read_csv(log_file)

        df_temp = pd.DataFrame(columns=df_log.columns, index=[0])

        df_temp['horario'] = datetime.now()
        df_temp['rotina'] = rotina

        df_temp['file'] = full_file.split('/')[-1]
        df_temp['full_file'] = full_file

        if error != '':
            # Acha a linha erro
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            linha_erro = exc_tb.tb_lineno

            df_temp['status'] = 'ERROR'
            df_temp['mensagem'] = error
            df_temp['linha_erro'] = str(linha_erro)

        if error == 'WARNING':
            df_temp['status'] = 'WARNING'
            df_temp['mensagem'] = np.nan
            df_temp['linha_erro'] = np.nan

        else:
            df_temp['status'] = 'OK'
            df_temp['mensagem'] = np.nan
            df_temp['linha_erro'] = np.nan

        df_log = pd.concat([df_log, df_temp])#.reset_index(inplace=True)
        df_log = df_log[['horario', 'rotina', 'file', 'full_file', 'status', 'mensagem','linha_erro']]
        df_log.reset_index(inplace=True, drop=True)


        return df_log.to_csv(log_file)

    @staticmethod
    def log_diario(delta_days=0):
        log_file = '/usr/lib/python2.7/dist-packages/grau_project/grau_log/log.csv'

        df_log = pd.read_csv(log_file)

        index = df_log.index
        df_log = df_log.astype(str)

        df_log_exp = df_log.loc[np.where(df_log['horario'].apply(lambda x: x.split(' ')[0]) == grau_datas.data_log(delta_days=delta_days))]

        historico_path = '/usr/lib/python2.7/dist-packages/grau_project/grau_log/historico/' + grau_datas.data_log(delta_days=delta_days) + '_log.csv'

        df_log_exp.to_csv(historico_path)

        return historico_path

    @staticmethod
    def send_log(delta_days=0):
        destinatarios = ['rafael.chow@graugestao.com.br']
        assunto = 'LOG - ' + str(grau_datas.padrao_brasileiro_datas())

        body = """<p>Boa noite</p> <p>Segue o log file para o dia """ + str(grau_datas.padrao_brasileiro_datas()) + """ </p> <p>Att.,</p>"""

        anexo = grau_log.log_diario(delta_days=delta_days)
        nome_anexo = anexo.split('/')[-1]

        for dest in destinatarios:
            grau_email.envio_email_anexo(para=dest, assunto=assunto, corpo_mensagem='', anexo=anexo, nome_anexo=nome_anexo)

if __name__=='__main__':
    print grau_log.send_log(delta_days=-1)

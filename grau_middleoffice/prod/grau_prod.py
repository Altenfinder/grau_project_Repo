from grau_project.grau_email.grau_leitor_email import grau_leitor_email
from grau_project.grau_email import grau_email
from grau_project.grau_britech_site.grau_britech_site import grau_britech_site
from grau_project.grau_datas import grau_datas
from grau_project.grau_log.grau_log import grau_log
from datetime import datetime, timedelta
import sys
import os


class grau_prod:
    @staticmethod
    def grau_prod(data=''):
        try:
            print grau_datas.feriado_check()

            path = '/usr/lib/python2.7/dist-packages/grau_project/grau_middleoffice/prod/temp/downloaded/'

            if data == '':
                date = datetime.now()
                data = str(date.year) + '-' + str(date.month) +  '-' + str(date.day)
                data_prod = grau_datas.data_papt_prod()

            else:
                date = data
                data = str(date.year) + '-' + str(date.month) +  '-' + str(date.day)
                data_prod = grau_datas.data_papt_prod(data=date)


            for file in os.listdir(path):
                print file[0:11]
                if file[0:11] == 'PROD_' + data_prod:
                    arquivo_upload = os.path.join(path, file)
                    print arquivo_upload


            britech_site = grau_britech_site()
            print britech_site.upload_importacao_operacoes(tipo_upload='prod', file_path=arquivo_upload, data=date)

            body = """
            <p>
            Prezados(as),
            </p>
            <p>
            Segue anexada a imagem comfirmando o upload do PROD no dia """ + data + """
            </p>
            <p>
            Att.,
            </p>
            """

            anexo = '/usr/lib/python2.7/dist-packages/grau_project/grau_middleoffice/prod/temp/upload/' + data + '_prod_upload.png'
            nome_anexo = data + '_prod_upload.png'

            grau_email.envio_email_anexo(para='rafael.chow@graugestao.com.br', assunto='Upload - PROD', corpo_mensagem=body, anexo=anexo, nome_anexo=nome_anexo)

            grau_log.log(rotina='upload_prod', full_file=__file__)


        except Exception, e:
            grau_log.log(rotina='upload_prod', full_file=__file__, error=e)


    @staticmethod
    def loop_grau_prod(dias_retrocedidos, inicio='d-1'):
        if inicio == 'd-0' or inicio == 'hoje':
            i = 0
        else:
            i = 1

        while i <= dias_retrocedidos:
            date = datetime.now() + timedelta(days=-i)
            grau_prod.grau_prod(data=date)
            i = i + 1


if __name__=='__main__':
    grau_prod.loop_grau_prod(dias_retrocedidos=1)

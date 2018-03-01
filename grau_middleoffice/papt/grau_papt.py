from grau_project.grau_email.grau_leitor_email import grau_leitor_email
from grau_project.grau_email import grau_email
from grau_project.grau_britech_site.grau_britech_site import grau_britech_site
from grau_project.grau_datas import grau_datas
from grau_project.grau_log.grau_log import grau_log
from datetime import datetime, timedelta
import sys
import os


class grau_papt:
    @staticmethod
    def grau_papt(data=''):
        try:
            print grau_datas.feriado_check()

            path = '/usr/lib/python2.7/dist-packages/grau_project/grau_middleoffice/papt/temp/downloaded/'

            if data == '':
                date = datetime.now()
                data = str(date.year) + '-' + str(date.month) +  '-' + str(date.day)
                data_papt = grau_datas.data_papt_prod()

            else:
                date = data
                data = str(date.year) + '-' + str(date.month) +  '-' + str(date.day)
                data_papt = grau_datas.data_papt_prod(data=date)

            for file in os.listdir(path):
                print data_papt
                if file[0:11] == 'PAPT_' + data_papt:
                    arquivo_upload = os.path.join(path, file)


            britech_site = grau_britech_site()
            print britech_site.upload_importacao_operacoes(tipo_upload='papt', file_path=arquivo_upload, data=date)


            body = """
            <p>
            Prezados(as),
            </p>
            <p>
            Segue anexada a imagem comfirmando o upload do PAPT no dia """ + data + """
            </p>
            <p>
            Att.,
            </p>
            """

            anexo = '/usr/lib/python2.7/dist-packages/grau_project/grau_middleoffice/papt/temp/upload/' + data + '_papt_upload.png'
            nome_anexo = data + '_papt_upload.png'

            grau_email.envio_email_anexo(para='rafael.chow@graugestao.com.br', assunto='Upload - PAPT', corpo_mensagem=body, anexo=anexo, nome_anexo=nome_anexo)

            grau_log.log(rotina='upload_prod', full_file=__file__)

        except Exception, e:
            grau_log.log(rotina='upload_prod', full_file=__file__, error=e)

    @staticmethod
    def loop_grau_papt(dias_retrocedidos, inicio='d-1'):
        if inicio == 'd-0' or inicio == 'hoje':
            i = 0
        else:
            i = 1

        while i <= dias_retrocedidos:
            date = datetime.now() + timedelta(days=-i)
            print date
            grau_papt.grau_papt(data=date)
            i = i + 1


if __name__=='__main__':
    grau_papt.loop_grau_papt(dias_retrocedidos=1)

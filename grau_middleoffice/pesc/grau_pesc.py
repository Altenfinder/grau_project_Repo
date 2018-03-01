from grau_project.grau_email.grau_leitor_email import grau_leitor_email
from grau_project.grau_email import grau_email
from grau_project.grau_britech_site.grau_britech_site import grau_britech_site
from grau_tratamento_pesc import grau_tratamento_pesc
from grau_project.grau_log.grau_log import grau_log
from grau_project.grau_datas import grau_datas
from datetime import datetime, timedelta

class grau_pesc:
    @staticmethod
    def grau_pesc(data=''):
        try:
            print grau_datas.feriado_check()

            if data == '':
                date = datetime.now()
                data = str(date.year) + '-' + str(date.month) +  '-' + str(date.day)
                data_pesc = grau_datas.data_pesc()

            else:
                date = data
                data = str(date.year) + '-' + str(date.month) +  '-' + str(date.day)
                data_pesc = grau_datas.data_pesc(data=data)



            print grau_tratamento_pesc.grau_tratamento_pesc(initial_folder='/usr/lib/python2.7/dist-packages/grau_project/grau_middleoffice/pesc/temp/downloaded/', final_folder='/usr/lib/python2.7/dist-packages/grau_project/grau_middleoffice/pesc/temp/final/', data=data)


            britech_site = grau_britech_site()
            arquivo_upload = '/usr/lib/python2.7/dist-packages/grau_project/grau_middleoffice/pesc/temp/final/' + data + '_pesc.txt'
            print britech_site.upload_importacao_operacoes(tipo_upload='pesc', file_path=arquivo_upload, data=date)

            body = """
            <p>
            Prezados(as),
            </p>
            <p>
            Segue anexada a imagem comfirmando o upload do PESC no dia """ + data + """
            </p>
            <p>
            Att.,
            </p>
            """

            anexo = '/usr/lib/python2.7/dist-packages/grau_project/grau_middleoffice/pesc/temp/upload/' + data + '_pesc_upload.png'
            nome_anexo = data + '_pesc_upload.png'

            grau_email.envio_email_anexo(para='rafael.chow@graugestao.com.br', assunto='Upload - PESC', corpo_mensagem=body, anexo=anexo, nome_anexo=nome_anexo)

            grau_log.log(rotina='upload_prod', full_file=__file__)

        except Exception, e:
            grau_log.log(rotina='upload_prod', full_file=__file__, error=e)


    @staticmethod
    def loop_grau_pesc(dias_retrocedidos, inicio='d-1'):
        if inicio == 'd-0' or inicio == 'hoje':
            i = 0
        else:
            i = 1

        while i <= dias_retrocedidos:
            date = datetime.now() + timedelta(days=-i)
            grau_pesc.grau_pesc(data=date)
            i = i + 1

if __name__=='__main__':
    grau_pesc.loop_grau_pesc(dias_retrocedidos=1)

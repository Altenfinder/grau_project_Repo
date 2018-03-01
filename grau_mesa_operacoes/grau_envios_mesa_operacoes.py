from grau_project.grau_britech_site.grau_britech_site import grau_britech_site
from grau_project.grau_email import grau_email
from grau_project.grau_datas import grau_datas
import time

class grau_envios_mesa_operacoes:
    @staticmethod
    def envio_vecimentos_futuros():
        britech = grau_britech_site()
        arquivo_anexo = britech.vencimentos_futuros()

        assunto = 'Vencimentos: ' + grau_datas.padrao_brasileiro_datas() + ' a ' + grau_datas.padrao_brasileiro_datas(delta_days=7)

        body = """
        <p>Boa tarde, </p>
        <p>Segue a tabela com vencimentos para a semana seguinte.</p>
        <p>Att.,</p>
        """

        nome_anexo = 'Vencimentos ' + grau_datas.padrao_brasileiro_datas() + ' - ' + grau_datas.padrao_brasileiro_datas(delta_days=7) + '.xls'

        grau_email.envio_email_anexo(para='rafael.chow@graugestao.com.br',assunto=assunto, anexo=arquivo_anexo, nome_anexo=nome_anexo)

        time.sleep(20)
        britech.close()

if __name__=='__main__':
    print envios_mesa_operacoes.envio_vecimentos_futuros()

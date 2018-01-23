from grau_project.grau_geckodriver.grau_geckodriver import grau_geckodriver
from grau_project.grau_excel.grau_excel import grau_excel
from grau_project.grau_email import grau_email
from datetime import datetime
import pandas as pd
import glob
import os
import time


class grau_informa_planner(grau_geckodriver):
    def __init__(self):
        super(grau_informa_planner, self).__init__()
        time.sleep(2)
        self.driver.get('http://informa.planner.com.br/vdfpmf/index.asp')
        time.sleep(5)
        self.login = 'railda@graugestao.com.br'
        self.password = 'planner123@'
        self.driver.find_element_by_xpath('//*[@id="Csag300"]/fieldset/label[1]/span/input').send_keys(self.login)
        self.driver.find_element_by_xpath('//*[@id="Csag300"]/fieldset/label[2]/span/input').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="Csag300"]/fieldset/button/span').click()

    def caixa_carteiras(self):
        time.sleep(10)
        url = 'http://informa.planner.com.br/VDFPMF/PSCC0001_02.ASP'
        self.driver.get(url)
        time.sleep(10)
        self.driver.find_element_by_xpath('//*[@id="PSCC0001_02-form"]/div[12]/div/div/button').click()
        time.sleep(10)
        self.driver.find_element_by_xpath('//*[@id="dt_report_wrapper"]/div[1]/a[4]/span').click()
        time.sleep(10)
        folder = glob.glob('/usr/lib/python2.7/dist-packages/grau_project/grau_informa_planner_site/downloaded/*')
        latest_file = max(folder, key=os.path.getctime)
        self.filename = '/usr/lib/python2.7/dist-packages/grau_project/grau_informa_planner_site/downloaded/' + 'downloaded_caixa_planner_' + str(datetime.now())+ '.csv'
        os.rename(latest_file, self.filename)
        self.driver.quit()

    def caixa_planner(self):
        path_template = '/usr/lib/python2.7/dist-packages/grau_project/grau_informa_planner_site/lista_clientes_caixa_planner.csv'
        final_path = '/usr/lib/python2.7/dist-packages/grau_project/grau_informa_planner_site/final/'

        caixa = pd.read_csv(self.filename)
        template = pd.read_csv(path_template)

        caixa = caixa[['ID.1', 'Nome.1', 'Disponivel', 'Projetado', 'Total']]

        temp_ids = pd.DataFrame(columns=['temp_ID','ID'])
        temp_ids['ID'] = template['CARTEIRA ADM'].str[0:7].loc[template['CARTEIRA ADM'].str[0:5].isin(caixa['ID.1'].astype(str))]
        temp_ids['temp_ID'] = (temp_ids['ID'].str[0:5]).astype(str)

        ids = (caixa['ID.1'].astype(str)).isin(template['CARTEIRA ADM'].str[0:5])
        caixa = caixa.loc[ids]

        caixa['ID.1'] = caixa['ID.1'].astype(str)

        caixa = caixa.merge(temp_ids, left_on='ID.1', right_on='temp_ID', how='left')
        caixa = caixa[['ID','Nome.1','Disponivel','Projetado','Total']]
        caixa.columns = ['ID','Nome','Disponivel','Projetado','Total']
        caixa = caixa.sort_values(by=['Nome'])

        now = datetime.now()
        data = str(now.year) + '-' + str(now.month) + '-' + str(now.day) + '_' +  str(now.hour) + ':' +  str(now.minute)

        self.xlsx_final_path = final_path + data + '_caixa_planner.xlsx'
        caixa.to_excel(self.xlsx_final_path, index=False, sheet_name='CC CADM')

        time.sleep(3)

        excel = grau_excel(workbook_path=self.xlsx_final_path, sheet_name='CC CADM')
        excel.border()
        excel.font
        excel.header()
        excel.resize_column(column="A",size=10)
        excel.resize_column(column="B",size=55)
        excel.resize_column(column="C",size=13)
        excel.resize_column(column="D",size=13)
        excel.resize_column(column="E",size=13)
        excel.resize_column(column="F",size=11)

    def envio_email(self):
        now = datetime.now()
        data = str(now.year) + '-' + str(now.month) + '-' + str(now.day)
        corpo='''
        <style="font-family:verdana; font-size="3">
        <p></p>
        Prezados,
        <p></p>
        Segue o C/C das carteiras com a data de hoje.
        <p></p>
        <p></p>
        Att.,
        '''

        grau_email.envio_email_anexo(para='rafael.chow@graugestao.com.br',corpo_mensagem=corpo, assunto='C/C CARTEIRAS - ' + data, anexo=self.xlsx_final_path, nome_anexo='caixa_carteiras_planner' + data + '.xlsx')


if __name__=='__main__':
    informa_planner = grau_informa_planner()
    informa_planner.caixa_carteiras()

    path_caixa = '/usr/lib/python2.7/dist-packages/grau_project/grau_informa_planner_site/downloaded/downloaded_caixa_planner_2018-01-22 16:02:27.502435.csv'
    informa_planner.caixa_planner()
    informa_planner.envio_email()

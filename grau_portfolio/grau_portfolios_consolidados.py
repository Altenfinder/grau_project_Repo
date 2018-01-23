from grau_project.grau_bloomberg.grau_bloomberg import grau_bloomberg
from grau_portfolio_xml import grau_portfolio_xml
from grau_project.grau_comdinheiro.grau_comdinheiro import grau_comdinheiro
from grau_project.grau_britech.grau_britech import grau_britech
from datetime import datetime
from shutil import copy2
from xml.etree import ElementTree
import os, sys
import pandas as pd
import numpy as np
import csv
import glob


class grau_portfolio_consolidado:
    def __init__(self, path, data='',timedelta=200):
        self.path = path
        self.data = data
        self.xml_path = '/usr/lib/python2.7/dist-packages/grau_project/grau_portfolio/temp/xml_grau/'
        self.temp_path = '/usr/lib/python2.7/dist-packages/grau_project/grau_portfolio/temp/tickers_consolidados/'
        self.timedelta = timedelta

        if data == '':
            date = datetime.now()
            self.data = str(date.year) + '-' + str(date.month) +  '-' + str(date.day)

    def consolidada_xml(self, final_path):
        for file in os.listdir(self.path):
            if file.endswith(".xml"):# and file[:file.find('_')] == self.data:
                self.portfolio_xml = grau_portfolio_xml(xml_path=self.path, xml_file=file)
                print copy2(self.path + file, final_path + self.portfolio_xml.data() + "_" + self.portfolio_xml.nome().replace(' ','_').replace('.','') + '.xml')

    def consolidada_tickers(self):
        self.ticker_bloomberg = pd.DataFrame(columns=['ticker_bloomberg'])
        self.ticker_comdinheiro = pd.DataFrame(columns=['ticker_comdinheiro'])
        self.cnpj_fundo = pd.DataFrame(columns=['cnpj_fundo'])

        xml_data = self.data.replace('-','')
        for file in os.listdir(self.xml_path):
            if file[:file.find('_')] == xml_data:
                self.portfolio_xml = grau_portfolio_xml(xml_path=self.xml_path, xml_file=file)
                portfolio = self.portfolio_xml.portfolio(tipo='sintetico',apenas_ativos_risco=True)

                if 'ticker_bloomberg' in portfolio:
                    self.ticker_bloomberg['ticker_bloomberg'] = pd.DataFrame((self.ticker_bloomberg['ticker_bloomberg'].tolist() + portfolio['ticker_bloomberg'].tolist()), columns=['ticker_bloomberg'])

                if 'ticker_comdinheiro' in portfolio:
                    self.ticker_comdinheiro['ticker_comdinheiro']  =  pd.DataFrame((self.ticker_comdinheiro['ticker_comdinheiro'].tolist() + portfolio['ticker_comdinheiro'].tolist()), columns=['ticker_comdinheiro'])

                if 'cnpj_fundo' in portfolio:
                    self.cnpj_fundo['cnpj_fundo']  = pd.DataFrame((self.cnpj_fundo['cnpj_fundo'].tolist() + portfolio['cnpj_fundo'].tolist()),columns=['cnpj_fundo'])

                (self.ticker_bloomberg.dropna().drop_duplicates().reset_index(drop=True)).to_pickle(self.temp_path + 'ticker_bloomberg')
                (self.ticker_comdinheiro.dropna().drop_duplicates().reset_index(drop=True)).to_pickle(self.temp_path + 'ticker_comdinheiro')
                (self.cnpj_fundo.dropna().drop_duplicates().reset_index(drop=True)).to_pickle(self.temp_path + 'ticker_cnpj_fundo')


    def bloomberg(self):
        path = '/usr/lib/python2.7/dist-packages/grau_project/grau_portfolio/temp/bloomberg/'
        ativos = pd.read_pickle(self.temp_path + 'ticker_bloomberg')['ticker_bloomberg'].tolist()
        self.bloomberg = grau_bloomberg(ativos, final_date=datetime.now(), timedelta=self.timedelta)
        px_last = self.bloomberg.px_last()
        px_last.to_pickle(path + self.data + '_' + 'bloomberg')
        return px_last

    def comdinheiro_duration(self):
        path = '/usr/lib/python2.7/dist-packages/grau_project/grau_portfolio/temp/duration/'
        ativos = pd.read_pickle(self.temp_path + 'ticker_comdinheiro')['ticker_comdinheiro']
        self.comdinheiro = grau_comdinheiro()
        duration = self.comdinheiro.duration(df=ativos)
        duration.to_pickle(path + self.data + '_' + 'duration')
        return duration

    def cotas(self):
        path = '/usr/lib/python2.7/dist-packages/grau_project/grau_portfolio/temp/fundos/'
        ativos = pd.read_pickle(self.temp_path + 'ticker_cnpj_fundo')['cnpj_fundo']
        print ativos
        self.britech = grau_britech()

        for cnpj in ativos:
            historico_precos = self.britech.carteiras(cpf_cnpj=cnpj, intervalo=12) #,  data_especifica='',data_especifica_inicial='', data_especifica_final='', tipo_retorno='', acumular_retorno=False, data_ultima_atualizacao=False, pl=False):
            historico_precos = historico_precos['cotafechamento']
            historico_precos.columns = [cnpj]
            print historico_precos
            historico_precos.to_piickle(path + self.data + cnpj)

        return historico_precos

    def main():
        pass


if __name__=='__main__':
    grau_portfolio_consolidado = grau_portfolio_consolidado('/usr/lib/python2.7/dist-packages/grau_project/grau_portfolio/temp/xml_planner/', data='2017-11-08')
    # print grau_portfolio_consolidado.consolidada_xml(final_path='/usr/lib/python2.7/dist-packages/grau_project/grau_portfolio/temp/xml_grau/')
    # print grau_portfolio_consolidado.consolidada_tickers()
    #print grau_portfolio_consolidado.bloomberg()
    print grau_portfolio_consolidado.comdinheiro_duration()
    # print grau_portfolio_consolidado.cotas()
    # britech = grau_britech()
    # print britech.query("""select * from pessoa where idpessoa like '1234567';""")
    # cpf_cnpj = '01653201000150'
    # print britech.query("""select idpessoa, cpfcnpj as cpf_cnpj from fin_grau.dbo.pessoa where cpfcnpj like ('""" + cpf_cnpj + """');""",)
    # print britech.carteiras(cpf_cnpj=cpf_cnpj)

import pandas as pd
from grau_portfolio_xml import grau_portfolio_xml
from grau_project.grau_bloomberg import grau_functions
import glob

class grau_portfolio:
    def __init__(self, portfolio_xml=True, folder_path='', file='', tipo='sintetico', apenas_ativos_risco=True, ajustar_pesos=True, ticker_bloomberg=True, ticker_comdinheiro=True):
        if portfolio_xml == True:

            self.portfolio = grau_portfolio_xml(xml_path=folder_path, file_path=file, tipo=tipo, apenas_ativos_risco=apenas_ativos_risco, ajustar_pesos=ajustar_pesos,ticker_bloomberg=ticker_bloomberg, ticker_comdinheiro=ticker_comdinheiro)


        # for file in glob.glob
    def precos(self, remove_na=True, timedelta=100):
        pass

    def retornos(self, remove_na=True, timedelta=100):
        pass

    def duration():
        pass

    def retornos_carteira():
        pass

    def volatilidade():
        pass

    def sharpe():
        pass

    def var_parametrica():
        pass

    def var_n_parametrica():
        pass


if __name__=='__main__':
    portfolio = grau_portfolio_xml(xml_path='/home/rafael/rafael.chow@graugestao.com.br/xml_planner/xml/atual', xml_file='FD14298834000130_20171109_20171113093348_Grau Hedge.xml')

    teste = portfolio.portfolio(tipo='sintetico', apenas_ativos_risco=True, ajustar_pesos=True)
    print teste
    #print teste.ticker_bloomberg()

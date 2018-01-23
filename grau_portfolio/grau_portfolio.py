from grau_project.grau_bloomberg.grau_bloomberg import grau_bloomberg
from grau_portfolio_xml import grau_portfolio_xml
import pandas as pd
import glob

class grau_portfolio:
    def __init__(self,data_dados='',timedelta=62, portfolio_xml=True, folder_path='', file='', tipo='sintetico', apenas_ativos_risco=True, ajustar_pesos=True, ticker_bloomberg=True, ticker_comdinheiro=True):

        super(grau_portfolio, self).__init__(xml_path=folder_path, xml_file=file)

        self.comdinheiro_path = '/usr/lib/python2.7/dist-packages/grau_project/grau_portfolio/temp/comdinheiro/'
        self.bloomberg_path = '/usr/lib/python2.7/dist-packages/grau_project/grau_portfolio/temp/bloomberg/'
        self.britech_path = '/usr/lib/python2.7/dist-packages/grau_project/grau_portfolio/temp/britech/'

        self.data = data_dados
        if data_dados == '':
            date = datetime.now()
            self.data = str(date.year) + '-' + str(date.month) +  '-' + str(date.day)

        #self.data = self.data.replace('-','')

        portfolio = grau_portfolio_xml(xml_path=folder_path, xml_file=file)

        if portfolio_xml == True:
            self.portfolio = portfolio.portfolio(tipo=tipo, apenas_ativos_risco=apenas_ativos_risco, ajustar_pesos=ajustar_pesos,ticker_bloomberg=ticker_bloomberg, ticker_comdinheiro=ticker_comdinheiro)

    def precos(self, remove_na=True):
        self.portfolio.groupby(['cnpj_fundo']).sum()
        self.portfolio.groupby(['ticker_bloomberg']).sum()
        self.portfolio.groupby(['ticker_comdinheiro']).sum()

        self.df_bloomberg_precos = pd.read_pickle(self.bloomberg_path + self.data + '_' + 'bloomberg')
        #df_britech = pd.read_pickle(self.britech_path + self.data + '_' + 'britech')

        print self.df_bloomberg_precos
        #print df_britech

    def retornos(self, remove_na=True):
        self.df_bloomberg_retornos = df_bloomberg_precos.pct_change()


    def duration():

        df_duration = pd.read_pickle(path + self.data + '_' + 'duration')
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
    # portfolio = grau_portfolio_xml(xml_path='/usr/lib/python2.7/dist-packages/grau_project/grau_portfolio/temp/xml_grau/', xml_file='20171229_GRAU_HEDGE_FUNDO_DE_INVESTIMENTO_MULTIMERCADO.xml')
    # teste = portfolio.portfolio(tipo='sintetico', apenas_ativos_risco=True, ajustar_pesos=True)
    # print teste
    portfolio = grau_portfolio(data_dados='2017-11-08',folder_path='/usr/lib/python2.7/dist-packages/grau_project/grau_portfolio/temp/xml_grau/', file='20171229_GRAU_HEDGE_FUNDO_DE_INVESTIMENTO_MULTIMERCADO.xml')
    portfolio.portfolio(tipo='sintetico',apenas_ativos_risco=True,ajustar_pesos=False, ticker_bloomberg=True)
    #print portfolio.precos()
    #print teste.ticker_bloomberg()

import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import os, sys
from pyvirtualdisplay import Display
import time


class grau_pentagono_site:
    def __init__(self, ativo=''):
        # self.driver_options = webdriver.FirefoxOptions()
        # prefs = {'download.default_directory' : '/home/grau/Gestao/Railda/Importacao/'}
        # self.driver_options.add_experimental_option('prefs', prefs)
        #self.display = Display(visible=0, size=(800, 600))
        #self.display.start()
        self.ativo = ativo

        pentagono_url = 'http://www.pentagonotrustee.com.br/PrecosUnitarios.aspx'
        self.driver=webdriver.Firefox(executable_path='/usr/lib/python2.7/dist-packages/grau_project/grau_geckdriver/geckodriver')
        self.driver.set_page_load_timeout(360)

        load = False
        while load == False:
            try:
                self.driver.get(pentagono_url)
                load = True
                print load
            except TimeoutException:
                print 'Falha no carregamento do site - Tentando novamente'

        self.select = Select(self.driver.find_element_by_xpath('//*[@id="ctl00_Conteudo_Ativo"]'))
        time.sleep(2)
        self.select.select_by_visible_text(self.ativo)
        self.driver.find_element_by_xpath('//*[@id="ctl00_Conteudo_Pesquisar"]').click()
        time.sleep(6)

    def df_debenture(self):
        html_source = self.driver.page_source
        df_html = pd.read_html(html_source, thousands='.', decimal=',')
        df_html = df_html[0]
        df_html.columns = df_html.iloc[0]
        df_html = df_html.loc[1]
        return df_html

    def pu_debenture(self, return_float=False):
        df_pu = grau_pentagono_site.df_debenture(self)
        df_pu = df_pu['PU']
        df_pu = df_pu.replace(df_pu[0:3],'')
        df_pu = df_pu.replace('.','')

        if return_float == False:
            return str(df_pu)
        else:
            df_pu = df_pu.replace(',','.')
            df_pu = float(df_pu)
            return df_pu

    def close(self):
        self.driver.quit()

if __name__=='__main__':
    pentagono = grau_pentagono_site('14B0480838')
    print pentagono.pu_debenture()
    print pentagono.pu_debenture(return_float=True)

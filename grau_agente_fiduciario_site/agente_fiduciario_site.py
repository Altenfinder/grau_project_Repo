import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os, sys
from pyvirtualdisplay import Display
import time


class grau_agente_fiduciario_site:
    def __init__(self, ativo=''):
        # self.driver_options = webdriver.FirefoxOptions()
        # prefs = {'download.default_directory' : '/home/grau/Gestao/Railda/Importacao/'}
        # self.driver_options.add_experimental_option('prefs', prefs)
        #self.display = Display(visible=0, size=(800, 600))
        #self.display.start()
        self.ativo = ativo
        self.driver=webdriver.Firefox(executable_path='/usr/lib/python2.7/dist-packages/grau_classes/geckodriver')
        self.login = 'rafael'
        self.password = 'gestao1400'
        self.driver.get('http://www.fiduciario.com.br/')
        self.select = Select(self.driver.find_element_by_xpath('//*[@id="cd_ativo"]'))
        self.select.select_by_visible_text(ativo)
        time.sleep(3)

    def df_debenture(self):
        self.driver.find_element_by_xpath('//*[@id="agfiduconthome"]/tbody/tr/td[2]/div[3]/form/input[3]').click()
        time.sleep(5)
        html_source = self.driver.page_source
        df_html = pd.read_html(html_source, thousands='.', decimal=',')
        df_html = df_html[3]
        df_html = df_html[df_html.columns[0:5]]
        df_html = df_html.drop_duplicates(subset='Data')
        df_html = df_html.set_index('Data')
        df_html = df_html.iloc[4:]
        return df_html

    def pu_debenture(self, return_float=False):
        df_pu = grau_agente_fiduciario_site.df_debenture(self)
        df_pu = df_pu[df_pu.columns[3]][df_pu.index[0]]
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
    site = grau_agente_fiduciario_site('MTEL15')
    df_debenture = site.pu_debenture(return_float=True)
    print df_debenture

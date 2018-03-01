import pandas as pd
import numpy as np
from selenium import webdriver
import os, sys
from pyvirtualdisplay import Display
import time

list_clientes_ativos = pd.read_csv('/usr/lib/python2.7/dist-packages/grau_project/grau_planner_site/lista_clientes_planner.csv').set_index('CARTEIRA ADM')

class grau_planner:
    def __init__(self):
        self.display = Display(visible=0, size=(800, 600))
        self.display.start()
        self.driver = webdriver.Firefox(executable_path='/usr/lib/python2.7/dist-packages/grau_project/grau_geckdriver/geckodriver')
        self.login = 'sergio@graugestao.com.br'
        self.password = 'erica@003'
        self.driver.get('https://www.plannerbackoffice.com.br/wvdf_cac_8/PAG300_04.Asp')
        time.sleep(3)
        self.driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[2]/td/input').send_keys(self.login)
        time.sleep(3)
        self.driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[4]/td/input').send_keys(self.password)
        time.sleep(3)
        self.driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[5]/td/img').click()
        time.sleep(2)


    def caixa_carteiras(self, decimal_brasileiro=True, planner_id_index=False):
        self.driver.get('https://www.plannerbackoffice.com.br/WVDF_ACC_1/PSINT550_02Oracle.asp#')
        time.sleep(4)
        self.driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td/table/tbody/tr[1]/td/fieldset/table[2]/tbody/tr[10]/td/input').click()
        time.sleep(4)
        self.driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td/img').click()
        time.sleep(4)
        html_source = self.driver.page_source
        if decimal_brasileiro == True:
            df_html = pd.read_html(html_source, thousands='.', decimal=',')
        else:
            df_html = pd.read_html(html_source)

        df_html = df_html[0]
        df_html = df_html[:][1:]
        df_html.reset_index(drop=True, inplace=True)
        df_html.columns = df_html.iloc[0]
        df_html = df_html[:][1:]
        df_html.reset_index(drop=True, inplace=True)

        df_html = df_html.loc[df_html['Cliente'].str[0:7].isin(list_clientes_ativos.index.str[0:7])]


        df_html['ID'] = df_html['Cliente'].apply(lambda x: x[0:7])
        df_html['Cliente'] = df_html['Cliente'].apply(lambda x: x[12:len(x)])


        index = df_html.index
        if planner_id_index == True:
            df_html = df_html.set_index('ID')
        else:
            df_html.reset_index(inplace=True)

        return df_html

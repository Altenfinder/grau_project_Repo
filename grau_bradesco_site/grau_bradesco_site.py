import pandas as pd
import numpy as np
from selenium import webdriver
import os, sys
from pyvirtualdisplay import Display
import time

list_clientes_ativos = pd.read_csv('/usr/lib/python2.7/dist-packages/grau_project/grau_planner_site/lista_clientes_planner.csv').set_index('CARTEIRA ADM')

class grau_bradesco_site:
    def __init__(self):
#        self.display = Display(visible=0, size=(800, 600))
#        self.display.start()
        self.driver = webdriver.Firefox(executable_path='/usr/lib/python2.7/dist-packages/grau_project/grau_geckdriver/geckodriver')
        self.login = 'm173500'
        self.password = 'brad0812'
        self.driver.get('https://wwws.bradescoprivate.com.br/iprilogin/login.jsf')
        self.driver.find_element_by_xpath('//*[@id="txtLogin"]').send_keys(self.login)
        self.driver.find_element_by_xpath('//*[@id="txtSenha"]').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="frmLoginSenha:_id62"]').click()

if __name__=='__main__':
    bradesco = grau_bradesco_site()
    print bradesco

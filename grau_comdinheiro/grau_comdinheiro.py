from selenium import webdriver
from grau_project.grau_datas import grau_datas
from grau_project.grau_comdinheiro import functions_comdinheiro
import time
import pandas as pd
#from pyvirtualdisplay import Display

class grau_comdinheiro:
    def __init__(self):
        #self.display = Display(visible=0, size=(800, 600))
        #self.display.start()
        self.driver = webdriver.Firefox(executable_path='/home/rafael/rafael.chow@graugestao.com.br/xml_planner/python_planner/geckodriver')
        self.login = 'feausp'
        self.password = 'feausp'
        self.driver.get('https://www.comdinheiro.com.br/home2/')
        self.driver.find_element_by_xpath('//*[@id="list_item_login"]/button').click()
        #time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="textUser"]').send_keys(self.login)
        #time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="textSenha"]').send_keys(self.password)
        #time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="login_button"]').click()

    def duration(self, df):
        time.sleep(5)
        url_duration = 'https://www.comdinheiro.com.br/Duration001.php?&data=' + grau_datas.padrao_brasileiro_datas() +'&papeis=' + functions_comdinheiro.formato_comdinheiro_lista_ativos(df, tipo='ativos') + '&quantidades=' + functions_comdinheiro.formato_comdinheiro_lista_ativos(df, tipo='') + '+&num_casas=3&flag_nd=0&agrupar=0&vertices=&check_duration=modo2&flag_discrimina_juros=1'
        self.driver.get(url_duration)
        time.sleep(5)

        df_html = pd.read_html(self.driver.page_source, thousands='.', decimal=',')

        df_html_debenture = df_html[-4]
        df_html_ntnb = df_html[-2]

        df = pd.concat([df_html_debenture, df_html_ntnb])

        return df

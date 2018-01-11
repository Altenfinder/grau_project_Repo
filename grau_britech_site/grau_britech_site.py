import pandas as pd
import numpy as np
from selenium import webdriver
import os, sys
from pyvirtualdisplay import Display
from grau_project.grau_datas import grau_datas
import time


class grau_britech_site:
    def __init__(self):
        # self.driver_options = webdriver.FirefoxOptions()
        # prefs = {'download.default_directory' : '/home/grau/Gestao/Railda/Importacao/'}
        # self.driver_options.add_experimental_option('prefs', prefs)
        # self.display = Display(visible=0, size=(800, 600))
        # self.display.start()
        self.driver = webdriver.Firefox(executable_path='/usr/lib/python2.7/dist-packages/grau_project/grau_geckdriver/geckodriver')
        self.login = 'rafael'
        self.password = 'gestao1400'
        self.driver.get('https://saas.britech.com.br/grau/Login/LoginInit.aspx?ReturnUrl=%2fgrau%2f')
        self.driver.find_element_by_xpath('//*[@id="Login1_UserName"]').send_keys(self.login)
        self.driver.find_element_by_xpath('//*[@id="Login1_Password"]').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="Login1_LoginButton"]').click()
        time.sleep(3)


    def interface_importacao_geral(self):
        self.driver.get('https://saas.britech.com.br/grau/Interfaces/Importacao.aspx')
        time.sleep(7)
        self.driver.find_element_by_xpath('//*[@id="ASPxRoundPanel1_tabArquivos_chkBDIN"]').click()
        self.driver.find_element_by_xpath('//*[@id="ASPxRoundPanel1_tabArquivos_chkBDPregao"]').click()
        self.driver.find_element_by_xpath('//*[@id="ASPxRoundPanel1_tabArquivos_chkIndic"]').click()
        self.driver.find_element_by_xpath('//*[@id="ASPxRoundPanel1_tabArquivos_chkTarPar"]').click()
        self.driver.find_element_by_xpath('//*[@id="ASPxRoundPanel1_tabArquivos_chkAndimaIndice"]').click()
        self.driver.find_element_by_xpath('//*[@id="ASPxRoundPanel1_tabArquivos_chkAndimaMercado"]').click()
        self.driver.find_element_by_xpath('//*[@id="ASPxRoundPanel1_tabArquivos_chkIma"]').click()
        self.driver.find_element_by_xpath('//*[@id="ASPxRoundPanel1_tabArquivos_chkTesouro"]').click()
        self.driver.find_element_by_xpath('//*[@id="ASPxRoundPanel1_tabArquivos_chkIBGE"]').click()
        self.driver.find_element_by_xpath('//*[@id="ASPxRoundPanel1_tabArquivos_chkDebenture"]').click()
        self.driver.find_element_by_xpath('//*[@id="ASPxRoundPanel1_tabArquivos_chkBVBG043"]').click()
        self.driver.find_element_by_xpath('//*[@id="ASPxRoundPanel1_tabArquivos_chkOffshore"]').click()
        self.driver.find_element_by_xpath('//*[@id="ASPxRoundPanel1_tabArquivos_chkAndima238"]').click()
        self.driver.find_element_by_xpath('//*[@id="ASPxRoundPanel1_tabArquivos_chkAndima550"]').click()
        self.driver.find_element_by_xpath('//*[@id="ASPxRoundPanel1_tabArquivos_chkTarPreg"]').click()
        self.driver.find_element_by_xpath('//*[@id="ASPxRoundPanel1_tabArquivos_chkRefVol"]').click()
        self.driver.find_element_by_xpath('//*[@id="ASPxRoundPanel1_tabArquivos_chkTaxaSwap"]').click()
        self.driver.find_element_by_xpath('//*[@id="ASPxRoundPanel1_tabArquivos_chkListaAtivoCVM"]').click()
        self.driver.find_element_by_xpath('//*[@id="ASPxRoundPanel1_tabArquivos_chkASEL007"]').click()
        self.driver.find_element_by_xpath('//*[@id="ASPxRoundPanel1_tabArquivos_chkPlCotaGalgoWcf"]').click()
        self.driver.find_element_by_xpath('//*[@id="ASPxRoundPanel1_tabArquivos_chkTMRV"]').click()
        self.driver.find_element_by_xpath('//*[@id="ASPxRoundPanel1_tabArquivos_chkBVBG044"]').click()
        self.driver.find_element_by_xpath('//*[@id="ASPxRoundPanel1_tabArquivos_textDataInicioInternet_I"]').click()
        self.driver.find_element_by_xpath('//*[@id="ASPxRoundPanel1_tabArquivos_textDataFimInternet_I"]').click()
        self.driver.find_element_by_xpath('//*[@id="ASPxRoundPanel1_tabArquivos_btnRunInternet"]').click()
        self.driver.close()

    def interface_importacao_debentures(self, ativo='', valor=''):
        self.driver.get('https://saas.britech.com.br/grau/CadastrosBasicos/RendaFixa/CotacaoSerie.aspx')
        time.sleep(6)
        self.driver.find_element_by_xpath('//*[@id="btnAdd"]/div').click()
        time.sleep(6)
        self.driver.find_element_by_xpath('//*[@id="gridCadastro_DXPEForm_efnew_textData_I"]').click()
        time.sleep(4)
        self.driver.find_element_by_xpath('//*[@id="gridCadastro_DXPEForm_efnew_textData_I"]').click()#send_keys(grau_datas.padrao_brasileiro_datas().replace('/',''))

        if ativo == 'MTEL15' or ativo == 'mtel15':
            self.driver.find_element_by_xpath('//*[@id="gridCadastro_DXPEForm_efnew_dropSerie_I"]').send_keys('34 - DEBC - MTEL15 - 141 - Area Interna')

        elif ativo == 'CRI PENTAGONO' or ativo == 'CRI_PENTAGONO':
            self.driver.find_element_by_xpath('//*[@id="gridCadastro_DXPEForm_efnew_dropSerie_I"]').send_keys('4 - CRI - PENTAGONO -108 - Area Interna')

        self.driver.find_element_by_xpath('//*[@id="gridCadastro_DXPEForm_efnew_textValor_I"]').send_keys(str(valor))
        time.sleep(10)
        self.driver.find_element_by_xpath('//*[@id="gridCadastro_DXPEForm_efnew_btnOK"]').click()
        time.sleep(6)

    def atualizacao_cotas_fundos(self):
        time.sleep(6)
        self.driver.get('https://saas.britech.com.br/grau/CadastrosBasicos/Fundo/CotaFundo.aspx')
        time.sleep(6)
        self.driver.find_element_by_xpath('//*[@id="btnImportarCotas"]').click()
        time.sleep(6)
        self.driver.find_element_by_xpath('//*[@id="popupImportarCotas_checkTodasCotas_S_D"]').click()
        time.sleep(6)
        self.driver.find_element_by_xpath('//*[@id="popupImportarCotas_btnRunImportarCotas"]').click()

    def close(self):
        return self.driver.quit()


if __name__=='__main__':
    britech_site = grau_britech_site()
    #print britech_site.interface_importacao_debentures(ativo='CRI_PENTAGONO', valor='23131,32')
    print britech_site.atualizacao_cotas_fundos()

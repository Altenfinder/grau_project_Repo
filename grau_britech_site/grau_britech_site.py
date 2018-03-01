import pandas as pd
import numpy as np
from selenium import webdriver
import os, sys
from pyvirtualdisplay import Display
from grau_project.grau_datas import grau_datas
from selenium.webdriver.common.keys import Keys
import time
from subprocess import Popen, PIPE
from datetime import datetime, timedelta
from grau_project.grau_datas import grau_datas
from grau_project.grau_excel.grau_excel import grau_excel
from grau_project.grau_utilities.grau_utilities import grau_utilities
from selenium.webdriver.support import expected_conditions as EC
import glob

class grau_britech_site:
    def __init__(self):
        # self.driver_options = webdriver.FirefoxOptions()
        # prefs = {'download.default_directory' : '/home/grau/Gestao/Railda/Importacao/'}
        # self.driver_options.add_experimental_option('prefs', prefs)
        # self.display = Display(visible=0, size=(800, 600))
        # self.display.start()
        self.profile = webdriver.FirefoxProfile()
        self.profile.set_preference("browser.upload.panel.shown", False)
        self.profile.set_preference('browser.upload.manager.showWhenStarting', False)
        self.profile.set_preference("browser.download.panel.shown", False)
        self.profile.set_preference('browser.download.folderList', 2)
        self.profile.set_preference('browser.download.manager.showWhenStarting', False)
        self.profile.set_preference('browser.download.dir', '/usr/lib/python2.7/dist-packages/grau_project/grau_britech_site/downloaded')
        self.profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv,application/vnd.ms-excel")
        self.profile.set_preference("browser.helperApps.neverAsk.openFile", "text/csv,application/vnd.ms-excel")
        self.profile.set_preference("javascript.enabled", False)
        self.driver = webdriver.Firefox(firefox_profile=self.profile, executable_path='/usr/lib/python2.7/dist-packages/grau_project/grau_geckodriver/geckodriver')
        #waitForPresence = WebDriverWait(self.driver, 600)

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

        time.sleep(5)
        data = self.driver.find_element_by_xpath("""//*[@id="ASPxRoundPanel1_tabArquivos_textDataInicioInternet_I"]""")
        self.driver.find_element_by_xpath("""//*[@id="ASPxRoundPanel1_tabArquivos_textDataInicioInternet_I"]""").click()
        self.driver.execute_script("ASPxRoundPanel1_tabArquivos_textDataInicioInternet_I.value = '" + grau_datas.data_britech(delta_days=-7) + "';", data)

        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="ASPxRoundPanel1_tabArquivos_textDataFimInternet_I"]').click()

        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="ASPxRoundPanel1_tabArquivos_btnRunInternet"]').click()


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

    def upload_importacao_operacoes(self, tipo_upload='', file_path='', data=''):
        time.sleep(7)
        self.driver.get('https://saas.britech.com.br/grau/Interfaces/Importacao.aspx')
        time.sleep(7)
        self.driver.find_element_by_xpath('//*[@id="ASPxRoundPanel1_tabArquivos_T1T"]/span').click()
        time.sleep(7)
        self.driver.find_element_by_xpath('//*[@id="ASPxRoundPanel1_tabArquivos_textDataArquivos_I"]').click()
        time.sleep(7)

        if tipo_upload == 'pesc':
            self.driver.find_element_by_xpath('//*[@id="ASPxRoundPanel1_tabArquivos_uplPESC_TextBox0_Input"]').send_keys(os.path.abspath(file_path))
            control_f4_sequence = '''key Alternate_L key F4'''
            print grau_britech_site.keypress(control_f4_sequence)
            time.sleep(3)

        if tipo_upload == 'papt':
            self.driver.find_element_by_xpath('//*[@id="ASPxRoundPanel1_tabArquivos_uplPAPT_TextBox0_Input"]').send_keys(file_path)
            control_f4_sequence = '''key Alternate_L key F4'''
            print grau_britech_site.keypress(control_f4_sequence)
            time.sleep(3)

        if tipo_upload == 'prod':
            self.driver.find_element_by_xpath('//*[@id="ASPxRoundPanel1_tabArquivos_uplPROD_TextBox0_Input"]').send_keys(file_path)
            control_f4_sequence = '''key Alternate_L key F4'''
            print grau_britech_site.keypress(control_f4_sequence)
            time.sleep(3)

        if data != '':
            data_fim = self.driver.find_element_by_xpath("""//*[@id="ASPxRoundPanel1_tabArquivos_textDataArquivos_I"]""")
            self.driver.find_element_by_xpath("""//*[@id="ASPxRoundPanel1_tabArquivos_textDataArquivos_I"]""").click()
            time.sleep(5)

            self.driver.execute_script("ASPxRoundPanel1_tabArquivos_textDataArquivos_I.value = '" + grau_datas.data_britech(data=data) + "';", data_fim)

        else:
            self.driver.find_element_by_xpath("""//*[@id="ASPxRoundPanel1_tabArquivos_textDataArquivos_I"]""").click()


        time.sleep(7)
        print 'fazendo o upload'
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="ASPxRoundPanel1_tabArquivos_btnRunArquivos"]').click()

        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="ASPxRoundPanel1_tabArquivos_btnRunArquivos"]')))
        time.sleep(300)

        # Salva imagem
        if isinstance(data, datetime):
            data = str(data.year) + '-' + str(data.month) +  '-' + str(data.day)

        screenshot_path = '/usr/lib/python2.7/dist-packages/grau_project/grau_middleoffice/' + tipo_upload + '/temp/upload/' + data + '_' + tipo_upload + '_upload.png'
        self.driver.save_screenshot(screenshot_path)

        time.sleep(5)
        self.driver.quit()

    def vencimentos_futuros(self):

        self.driver.get('https://saas.britech.com.br/grau/Consultas/Vencimentos.aspx')

        data_fim = self.driver.find_element_by_xpath("""//*[@id="textDataFim_I"]""")
        self.driver.find_element_by_xpath("""//*[@id="textDataFim_I"]""").click()
        time.sleep(5)
        self.driver.execute_script("textDataFim_I.value = '" + grau_datas.data_britech(delta_days=8) + "';", data_fim)

        data_fim = self.driver.find_element_by_xpath("""//*[@id="textDataInicio_I"]""")
        self.driver.find_element_by_xpath("""//*[@id="textDataInicio_I"]""").click()
        time.sleep(5)
        self.driver.execute_script("textDataInicio_I.value = '" + grau_datas.data_britech(delta_days=0) + "';", data_fim)

        self.driver.find_element_by_xpath('//*[@id="btnExcel"]').click()
        time.sleep(15)

        excel_file = grau_utilities.find_most_recent_file(folder_path='/usr/lib/python2.7/dist-packages/grau_project/grau_britech_site/downloaded')

        return excel_file

    @staticmethod
    def keypress(sequence):
        p = Popen(['xte'], stdin=PIPE)
        p.communicate(input=sequence)


    def close(self):
        return self.driver.quit()


if __name__=='__main__':
    britech_site = grau_britech_site()
    print britech_site.interface_importacao_teste()
    #britech_site.upload_importacao_operacoes(tipo_upload='pesc', file_path='/usr/lib/python2.7/dist-packages/grau_project/grau_middleoffice/temp/pesc/final/2018-1-22_pesc.txt')

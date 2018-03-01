from selenium import webdriver
import pandas as pd
from datetime import datetime
import time
import os
from grau_project.grau_pdf.grau_relatorios_pdf3 import grau_relatorio_pdf
import shutil


class grau_minicom_planner:
    def __init__(self):
        self.profile = webdriver.FirefoxProfile()
        self.profile.set_preference("browser.download.panel.shown", False)
        self.profile.set_preference('browser.download.folderList', 2)
        self.profile.set_preference('browser.download.manager.showWhenStarting', False)
        self.profile.set_preference('browser.download.dir', "/home/felipe/Downloads")
        self.profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv,application/vnd.ms-excel")
        self.profile.set_preference("browser.helperApps.neverAsk.openFile", "text/csv,application/vnd.ms-excel")
        self.profile.set_preference("browser.helperApps.neverAsk.saveToDisk","application/pdf,application/x-pdf")
        self.profile.set_preference("pdfjs.disabled", "true")
        self.driver = webdriver.Firefox(firefox_profile=self.profile, executable_path='/usr/lib/python2.7/dist-packages/grau_project/grau_geckodriver/geckodriver')

        self.login = 'grau_gestao'
        self.password = 'grau'
        self.driver.get('http://minicom.planner.com.br/usaf4web/uscp3/?mod=wsm&dsp=login')
        self.driver.find_element_by_xpath('/html/body/form[2]/div[2]/div[1]/div/div[3]/div[2]/input').send_keys(self.login)
        self.driver.find_element_by_xpath('/html/body/form[2]/div[2]/div[1]/div/div[3]/div[4]/input').send_keys(self.password)
        self.driver.find_element_by_xpath('/html/body/form[2]/div[2]/div[1]/div/div[3]/div[5]/div[2]/input').click()
        self.now = datetime.now()

    def fundos_tratados(self, screenshot_path):
        time.sleep(5)
        self.driver.get('http://minicom.planner.com.br/usaf4web/uscp3/?mod=uscp&dsp=uscp231_U')
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/input').click()
        time.sleep(5)
        self.driver.save_screenshot(screenshot_path)

    def cotas_fundos(self):
        time.sleep(5)
        self.driver.get('http://minicom.planner.com.br/usaf4web/uscp3/?mod=uscp&dsp=uscp231_U')
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/input').click()
        time.sleep(5)
        self.driver.find_element_by_id('7gestor').click()
        self.driver.find_element_by_xpath("//input[@value='Gerar Excel']").click()
        time.sleep(5)
        c=''
        os.system('cp -r /tmp/mozilla_root0/ /home/felipe/Relatorio')
        c=os.listdir('/home/felipe/Relatorio/mozilla_root0')[0]
        print c
        #c = c.replace('.','',1).replace('.','',1).replace('~lock','').replace('#','')

        grau_relatorio_pdf.pdf_global('/home/felipe/Relatorio/mozilla_root0/'+c)
        shutil.rmtree('/home/felipe/Relatorio')
        shutil.rmtree('/tmp/mozilla_root0')
        time.sleep(5)
        os.system('mkdir /home/felipe/Relatorio')


        #self.driver.get("http://minicom.planner.com.br/usaf4web/uscp3/?mod=uscp&dsp=uscp231_U_PDF&codProd=40477&data=22/02/2018")
        #self.driver.find_element_by_id('Download').click()
    def cotas_fundos_benf_email(self):
        time.sleep(5)
        self.driver.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
        self.login = 'felipe@graugestao.com.br'
        self.password = 'Olhobagabago123'
        self.driver.find_element_by_id('identifierId').send_keys(self.login)
        self.driver.find_element_by_id('identifierNext').click()
        time.sleep(3)
        self.driver.find_element_by_id('password').send_keys(self.password)
        self.driver.find_element_by_id('passwordNext').click()





if __name__=='__main__':
    minicom = grau_minicom_planner()
    print minicom.cotas_fundos_benf_email()
    # print minicom.fundos_tratados()

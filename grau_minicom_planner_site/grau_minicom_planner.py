from selenium import webdriver
import pandas as pd
from datetime import datetime
import time


class grau_minicom_planner:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path='/usr/lib/python2.7/dist-packages/grau_project/grau_geckdriver/geckodriver')
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

if __name__=='__main__':
    minicom = grau_minicom_planner()
    print minicom.fundos_tratados()

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import unittest
class LoginTest(unittest.TestCase):
    driver = webdriver.Firefox(executable_path="/home/felipe/geckodriver")
    #self.driver=web
    def set_up(self):
        self.driver = webdriver.Firefox(executable_path="/home/felipe/geckodriver")
    def test_Login(self):
        driver = self.driver
        self.driver.get("http://minicom.planner.com.br/usaf4web/uscp3/?mod=wsm&dsp=login")
        Username = "grau_gestao"
        Password = "grau"
        emailFieldName = "user_name"
        passFieldName = "user_pass"
        LoginButtonXpath="//input[@value='Entrar']"
        fbLogoXpath = "(//a[contains(@href,'logo')])[1]"
        profileXPath = "(//a[contains(@href,'felipe.altenfelder3')])[1]"
        ativoXPath="/html/body/div[2]/ul/li[1]/a"
        selectxpath = "//a[@href='?mod=uscp&dsp=uscp260_9_9_U']"
        searchXPath = "/html/body/div[3]/div/div[2]/div[2]/input"



        emailFieldElement = WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_name(emailFieldName))
        passFieldElement = WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_name(passFieldName))
        loginButtonElement = WebDriverWait(driver,30).until(lambda driver:driver.find_element_by_xpath(LoginButtonXpath))
        emailFieldElement.clear()
        emailFieldElement.send_keys(Username)
        passFieldElement.clear()
        passFieldElement.send_keys(Password)
        loginButtonElement.click()
        lin = 2
        xpath_dict = dict()
        check = false
        while check == False:
            id = str(lin) + 'gestor'
            try:
                self.driver.find_element_by_id(id).text
                dict[id] = self.driver.find_element_by_id(id).text
            except:
                check = True

            lin = lin + 1
        #driver.find_element_by_css_selector("div.plan.right > a.select.").click()
        #self.driver.find_element_by_css_selector(".pull-down selected[href='?mod=uscp&dsp=uscp260_9_9_U']").click()
        self.driver.get('http://minicom.planner.com.br/usaf4web/uscp3/?mod=uscp&dsp=uscp260_9_9_U')
        searchFieldElement = WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_xpath(searchXPath))
        searchFieldElement.click()
        ativoElement = WebDriverWait(driver,2).until(lambda driver:driver.find_element_by_link_text("Ativo"))
        ativoElement.click()
        selectElement = WebDriverWait(driver,30).until(lambda driver:driver.find_element_by_xpath(selectxpath))
        selectElement.click()
        #SelecionarItem= WebDriverWait(driver,30).until(lambda driver:driver.find_element_by_link_text("Ativo"))
        #SelecionarItem.click()
        #SelecionarItem= WebDriverWait(driver,30).until(lambda driver:driver.find_element_by_link_text("Historico de Cotas"))
        #SelecionarItem.click()
        #Select(SelecionarItem).find_element_by_link_text("Historico de Cotas")
        #time.sleep(5)
        #profile = WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_xpath(profileXPath))
        #profile = WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_link_text("Felipe"))
        #profile.click()
        #self.driver.quit()





if __name__=='__main__':
    unittest.main()

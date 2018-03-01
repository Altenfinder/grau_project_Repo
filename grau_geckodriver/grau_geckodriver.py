from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class grau_geckodriver(object):
    def __init__(self, download_path):
        # self.driver_options.add_experimental_option('prefs', prefs)
        # self.display = Display(visible=0, size=(800, 600))
        # self.display.start()


        ## Download Preferences:
        self.profile = webdriver.FirefoxProfile()
        self.profile.set_preference("browser.download.panel.shown", False)
        self.profile.set_preference('browser.download.folderList', 2)
        self.profile.set_preference('browser.download.manager.showWhenStarting', False)
        self.profile.set_preference('browser.download.dir', download_path)
        self.profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv,application/vnd.ms-excel")
        self.profile.set_preference("browser.helperApps.neverAsk.openFile", "text/csv,application/vnd.ms-excel")
        self.driver = webdriver.Firefox(firefox_profile=self.profile, executable_path='/usr/lib/python2.7/dist-packages/grau_project/grau_geckodriver/geckodriver')

        @property
        def login(self):
            return self._login

        @property
        def password(self):
            return self._password

        @login.setter
        def login(self, value):
            self._login = value

        @login.getter
        def login(self, value):
            self._login = value

        @password.deleter
        def login(self):
            del self._login

        @password.setter
        def password(self, value):
            self._password = value

        @password.getter
        def password(self, value):
            self._password = value

        @password.deleter
        def password(self):
            del self._password

        def close(self):
            self.driver.quit()

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class test(object):

    def tearDown(self):
        try:
            self.driver.quit()
            pass
        except:
            pass

    def getDriver(self, browser, local=False):
        if browser == "firefox":
            cap = DesiredCapabilities.FIREFOX
        if browser == "ie":
            cap = DesiredCapabilities.INTERNETEXPLORER
        if browser == "chrome":
            cap = DesiredCapabilities.CHROME
            options = Options()
            options.add_argument("--disable-extensions")
            options.add_argument("test-type")
        if browser == "mobile chrome":
            cap = {}
            cap['browserName'] = "Chrome"
            cap['platformName'] = "Android"
            cap['deviceName'] = "android"
        if browser == "android":
            cap = {}
            cap['browserName'] = "Browser"
            cap['platformName'] = "Android"
            cap['deviceName'] = "android"
        if local:
          return webdriver.Chrome()
        else:
          return webdriver.Remote(
                                  command_executor='http://10.238.242.50:4444/wd/hub',
                                  desired_capabilities=cap
                                 )
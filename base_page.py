
from selenium.common.exceptions import WebDriverException

class Page(object):
    """
    Base Class For all Pages
    """
    
    def __init__(self, testsetup):
        self.testsetup = testsetup
        self.driver = testsetup['driver']
        self.timeout = testsetup['timeout']
        self.driver.implicitly_wait(testsetup['timeout'])
        #self.driver.get(testsetup['goto'])
        
        
    def maximize_window(self):
        try:
            self.driver.maximize_window()
        except WebDriverException:
            pass
        
    def goto(self, url):
        driver = self.driver
        driver.get(url)
    
    def go_back(self):
        self.driver.back()

    def refresh(self):
        self.driver.refresh() 

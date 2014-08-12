from base_page import Page

class webObject(Page):
    
    def __init__(self, driver, by, loc):
        self.driver = driver
        self.element = self.find(self.driver, by, loc)

    @staticmethod
    def find(parent, by, loc):
        if by == "css":
            return parent.find_element_by_css_selector(loc)
        elif by == "xpath":
            return parent.find_element_by_xpath(loc)

    def find_child(self, parent, by, loc):
        return self.find(parent, by, loc)

    def find_child_with_text(self, text):
        return self.find_child(self.element, "xpath", ".//*[contains(text(),'" + text + "')]")

from webObject import webObject
from random import randrange
from selenium.webdriver.support.ui import Select


class webEdit(webObject):
    
    def set(self, value):
        self.element.clear()
        self.element.send_keys(value)
        
    def append(self,value):
        self.element.send_keys(value)


class webButton(webObject):
    def click(self):
        self.element.click()


class webSelect(webObject):
    def __init__(self, driver, by, loc):
        super(webSelect, self).__init__(driver, by, loc)
        self.element = Select(self.element)
        
    def select_by_text(self, value):
        self.element.select_by_visible_text(value)
        
    def select_random(self):
        option_count = len(self.element.options)
        select = randrange(option_count)
        self.element.select_by_index(select)


class webLink(webObject):
    def click(self):
        self.element.click()


class webElement(webObject):
    def click(self):
        self.element.click()


class webTable(webObject):

    class webTable_row(webObject):
        def __init__(self, table, by, loc):
            super(webTable.webTable_row, self).__init__(table.element, by, loc)
            self.table = table

        def find_cell_by_index(self, index):
            if index == "first":
                return self.element.find_elements_by_tag_name("td")[0]
            elif index == 'last':
                return self.element.find_elements_by_tag_name("td")[-1]
            else:
                return self.element.find_elements_by_tag_name("td")[index]

    def row_containing_text(self, text):
        return webTable.webTable_row(self, "xpath", ".//tr[descendant::text()[contains(., '" + text + "')]]")


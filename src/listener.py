
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

class MyListener(AbstractEventListener):
    def __init__(self, num_months, days, start_row, start_column, end_row, end_column):
        self.scraped_data = ""
        self.i = 0
        self.num_months = num_months
        self.days = days
        self.start_row = start_row
        self.start_column = start_column
        self.end_row = end_row
        self.end_column = end_column


    # This function automatically runs after an edriver.get() call
    def after_navigate_to(self, _, driver):
        js_code = self.__get_js_code()
        self.scraped_data += driver.execute_script(js_code)
        self.i += 1


    def __get_js_code(self):
        return  f'''
        var scraped_data = "";
        var rows;

        rows = document.getElementsByClassName(\'maintab bwgtcolors\')[0].children;
        if({self.i} == 0) {{
            var days_to_scrape = Math.min({self.days} + {self.start_column}, 7)
            for(var j={self.start_column}; j<days_to_scrape; j++) {{
                scraped_data += rows[{self.start_row}].children[0].children[0].children[j].innerText;
            }}
        }}

        if({self.num_months} == 1 && {self.start_row} == {self.end_row})  {{
            return scraped_data;
        }}

        var next_row = ({self.i} == 0) ? {self.start_row} + 2 : 2;
        var last_row = ({self.num_months} - 1 == {self.i}) ? {self.end_row} : rows.length;
        for(var j=next_row; j<last_row; j+=2) {{
            scraped_data += rows[j].children[0].children[0].innerText;
        }}

        if({self.num_months} - 1 == {self.i}) {{
            for(var j=0; j<{self.end_column}+1; j++) {{
                scraped_data += rows[{self.end_row}].children[0].children[0].children[j].innerText;
            }}
        }}

        return scraped_data;
        '''
class WebTable():
    def __init__(self, web_element):
        self.web_element = web_element
        self.header = self.web_element.find_element_by_xpath("//div[@class = 'ui-grid-header ng-scope']")

        def find_row_by_column(column_name):


        def find_row_by_columns(column_names):
            rows = self.web_element.find_elements_by_xpath("//div[@class = 'ui-grid-row ng-scope']")
            for row in rows:
                columns = row.find_elements_by_xpath("//div[@class = 'ui-grid-cell']")

            for column in columns:
                columns = column.find

        def find_index_by_name(name):
            header_elements = self.header.find_elements_by_xpath(".//span")
            for idx, val in enumerate(header_elements):
                if val == name:
                    return idx
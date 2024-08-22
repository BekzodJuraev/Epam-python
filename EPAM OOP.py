class Pagination:
    def __init__(self, data, items_on_page):
        self.data=data
        self.items_on_page=items_on_page


    def page(self):
        str = []
        string = ""
        for item in self.data:
            string += item
            if len(string) >= self.items_on_page:
                str.append(string)
                string = ""
        str.append(string)
        return str
    @property
    def page_count(self):
        return len(self.page())





    @property
    def item_count(self):
        return len(self.data)



    def count_items_on_page(self, page_number):
        try:
            return len(self.page()[page_number])
        except:
            return "Exception: Invalid index. Page is missing."



    def find_page(self, data):
        try:
            x = []
            if data in self.data:
                for item in range(0, len(self.page())):
                    if data in self.page()[item]:
                        x.append(item)
            else:
                raise KeyError(f"Exception:'{data}' is missing on the pages")
        except KeyError as ke:
            return ke







        return x

    def display_page(self, page_number):
       return self.page()[page_number]









pages = Pagination('Your beautiful text', 5)
print(pages.page_count)
print(pages.item_count)
print(pages.count_items_on_page(4))
print(pages.find_page('e'))
print(pages.display_page(0))
#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    @property
    def page(self):
        return self.page_count

    @page.setter
    def page(self, new_page):
        if not isinstance(new_page, int):
            print('page_count must be an integer')
        else: 
            self.page_count = new_page
            
    def turn_page(self):
        print('Flipping the page...wow, you read fast!')



    

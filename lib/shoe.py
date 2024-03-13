#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, shoe_size):
        self.brand = brand
        self.shoe_size = shoe_size
        self.condition= "Used"
    @property
    def size(self):
        return self.shoe_size

    @size.setter
    def size(self, new_size):
        if not isinstance(new_size, int):
            print('size must be an integer')
        else: 
            self.shoe_size = new_size
    def cobble(self):
        self.condition= "New"
        print('Your shoe is as good as new!')
            


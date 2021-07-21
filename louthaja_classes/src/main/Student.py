'''
Created on Jul 21, 2021

@author: Jacob
'''

class Student(object):
    
    def __init__(self, first_name):
        
        self.first_name = first_name
        
        
        
class BetterStudent:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def toString(self):
        return "{} {}".format(self.first_name, self.last_name)
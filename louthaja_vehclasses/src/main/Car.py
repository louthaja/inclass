'''
Created on Jul 21, 2021

@author: Jacob
'''
 
from Vehicle import Vehicle

class Car(Vehicle):
    
    def __init__(self, type, make, model):
        self.make = make;
        self.model = model;
        vehicle.__init__(self, type);
        
    def printMake(self):
        print(self.make);
        
    def printmodel(self):
        print(self.model);
'''
Created on Jul 21, 2021

@author: Jacob
'''
from Car import Car

class Hybrid(Car):
    
    def __init__(self, type, make, model, batteryKVA):
        '''
        Constructor
        '''
        self.batteryyKVA = batteryKVA;
        Car.__init__(self, type, make, model);
        
    def printBatteryKVA(self):
        print(self.batteryyKVA);
'''
Created on Jul 21, 2021

@author: Jacob
'''

class Student(object):
    '''
    classdocs
    '''
    


    def __init__(self, first_name):
        '''
        Constructor
        '''
        self.first_name = first_name
        
bill = Student("Bill")
brenda = Student("Brenda")

print("{} {}".format(bill.firstName, brenda.first_name))

print(bill.__dict__)
print(brenda.__dict__)
'''
Created on Jul 21, 2021

@author: Jacob
'''

class Student(object):
    '''
    classdocs
    '''
    


    def __init__(self):
        '''
        Constructor
        '''
bill = Student()
brenda = Student()
bill.firstName = "Bill"
brenda.first_name = "Brenda"

print("{} {}".format(bill.firstName, brenda.first_name))

print(bill.__dict__)
print(brenda.__dict__)
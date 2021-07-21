'''
Created on Jul 21, 2021

@author: Jacob
'''


# from package.module import class
from main.Student import Student




if __name__ == '__main__':      # make sure I am the entry point for the project
    
    bill = Student("Bill")
    brenda = Student("Brenda")
    
    print("{} {}".format(bill.first_name, brenda.first_name))
    
    print(bill.__dict__)
    print(brenda.__dict__)
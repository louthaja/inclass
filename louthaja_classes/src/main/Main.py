'''
Created on Jul 21, 2021

@author: Jacob
'''


# from package.module import class
from main.Student import Student, BetterStudent




if __name__ == '__main__':      # make sure I am the entry point for the project
    
    bill = BetterStudent("Bill", "Louthan")
    brenda = BetterStudent("Brenda", "Louthan")
    
    
    print(bill.toString())
    print(brenda.toString())
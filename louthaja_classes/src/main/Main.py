'''
Created on Jul 21, 2021

@author: Jacob
'''

if __name__ == '__main__':      # make sure i am the entryy point for the project
    
    bill = Student("Bill")
    brenda = Student("Brenda")
    
    print("{} {}".format(bill.first_name, brenda.first_name))
    
    print(bill.__dict__)
    print(brenda.__dict__)
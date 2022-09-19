# 6. Write a python script to create a Calculator 2.0 class with 2 methods for multiplication
# and division of 2 values and inherit it from the Calculator class.

from q5 import *

class Calculator2point0(Calculator):
    
    def multiplication(self):
        return self.x*self.y

    def division(self):
        if(self.y==0):
            return "Error"
        else:
            return self.x/self.y    

c2=Calculator2point0(12,7)
c3=Calculator2point0(13,5)

# print(c2.multiplication(),c3.division())
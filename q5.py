# 5. Write a python script to create a Calculator class with 2 methods for adding and
# subtracting 2 values.


from re import X


class Calculator:
    
    def __init__(self,X,Y):
        self.x=X
        self.y=Y

    def add(self):
        return self.x+self.y

    def subtract(self):
        return self.x-self.y    

c1=Calculator(7,8)

# print(c1.add(),c1.subtract(),sep=':')

# 9. Write a python script to create an application like Truecaller where names and
# numbers are stored. Truecaller class will have 2 methods (1st to fetch the name of a
# number and 2nd to add a new entry).

class Truecaller:

    def __init__(self):
        self.__name=None
        self.__number=None

 

    def get_name(self):
        return self.__name

    def set__number(self,num,n):
        x=num
        count=0
        while(x):
            x//=10
            count+=1
        if(count==10):
                self.__number=num
                self.__name=n
     

t1=Truecaller()  
t2=Truecaller()        
      

t1.set__number(1234567890,"Babita")
t2.set__number(7890123459,"Ajay")

print(t1.get_name())
print(t2.get_name())
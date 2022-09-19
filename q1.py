# 1. Write a python script to create a Profile class with 3 attributes (name, email, age).




class Profile:
    def __init__(self,n,e,a):
        self.name=n 
        self.email=e
        self.age=a

    def show(self):
        print(self.name,self.email,self.age,sep="\t")    

p1=Profile("Tarun","abc@gmail.com",19)

# p1.show()
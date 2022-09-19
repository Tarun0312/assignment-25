# 3. Write a python script to update 2nd Question, change email and age to __email and
# __age.

class Profile:
    def __init__(self):
        self.name=None
        self.__email=None
        self.__age=None

    def set_name(self,n):
        self.name=n   

    def get_name(self):
        return self.name    

    def set_email(self,e):
        self.__email=e

    def get_email(self):
        return self.__email

    def set_age(self,a):
        if(a<0):
            self.__age=-a
        self.__age=a

    def get_age(self):
        return self.__age    

p1=Profile()

p1.set_name("Tarun"),p1.set_age(19),p1.set_email("1@gmail.com")
print(p1.get_age(),p1.get_email(),p1.get_name())

print(p1.name) 
print(p1.age,p1.email)# can't access __ attributes outside the class
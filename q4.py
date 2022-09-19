# 4. Write a python script to update 2nd Question, add a class variable (platform) and
# create a classmethod to access it.

class Profile:

    platform="iNeuron"
    def __init__(self):
        self.name=None
        self.age=None
        self.email=None

    @classmethod
    def get_Platform(cls):
        return cls.platform

p1=Profile() 
print(Profile.get_Platform())


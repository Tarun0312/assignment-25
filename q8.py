# 8. Write a python script to create a SmartPhone class by inheriting Calculator 2.0 and
# Phone Class.

from q6 import * 
from q7 import *

class SmartPhone(Calculator2point0,Phone):
    def game(self):
        return "PUBG"

    def email(self):
        return "You can email to any person anywhere in the world"

s1=SmartPhone(5,4)
s2=SmartPhone(4,0)

print(s1.add(),s1.subtract(),s2.division(),s1.multiplication())
s2.call(),s2.sms()
print(s2.email(),s2.game(),sep='\n')

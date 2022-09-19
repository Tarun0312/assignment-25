# 10. Write a python script to add the new method in SmartPhone class which accepts
# Truecaller object as a parameter and call the fetch method of Truecaller.

from q9 import *



class SmartPhone:

    def fetchTrucallerMethod(self,obj):
        obj.set__number(8470121419,"Harish")
        print(obj.get_name())

t1=Truecaller()
s1=SmartPhone()
s1.fetchTrucallerMethod(t1)

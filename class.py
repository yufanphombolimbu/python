#!/bin/python3


# class yufan 
# making class yufan  
# class is a blueprint of an object.

class yufan:
    
    # initization or construction has been used in these class
    def __init__(self,a):
        
        #example of an instance variable 
        self.a = a

    # defining function inside an called limbu

    def function(self):
        print(f"My name is {self.a}")

# calling an object 
a = yufan("Yufan LImbu")
a.function()


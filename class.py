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
    
    # adding another function or we called it method 

    def limbu(self):
        
        self.b = 123
        self.c = 234
        return "The value of b and c is {}".format(self.b * self.c)

# calling an object 
a = yufan("Yufan LImbu")
a.function()
print(a.limbu())

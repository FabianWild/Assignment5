# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 14:26:10 2019

@author: ru79vip
IMPROVING STRATEGIES FOR PYTHON
"""
""" Avoid concenating in a loop """
stuff = [str(x) for x in range(100000)] 
s = "" 
for substring in stuff:    
    s += substring 
    
#This is better    
s = "".join(stuff)

""" use list comprehension instead of loop """
stuff = [str(x) for x in range(100000)]
newlist = [] 
for word in stuff:    
    newlist.append(word.upper())
    
#This is better    
newlist = [s.upper() for s in stuff]

""" Use Functions """
def main():
    for i in range(10**8):
        pass
main() 

#This is better
for i in range(10**8):    
    pass

""" Numpy is faster than normal python """
import numpy as np
#This is faster
stuff = np.arange(10000000) 
np.sum(stuff) 

#This is slow
stuff = [x for x in range(10000000)] 
sum(stuff)

""" Import a module """
import functions 
functions.do_thing() 
print(functions.value)
if __name__ =="__main__":
    functions.do_thing() 
    print(functions.value)
    



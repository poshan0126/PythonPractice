# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 20:01:29 2019

@author: Poshan Pandey
"""

print ("Hello World!\n")


class Stack:

    def __init__(self):
        self.items=[]
    
    def isEmpty(self):
        self.items==[]
        
    def push(self,value):
        self.items.append(value)
        
    def pop(self):
        
        return self.items.pop()
    
    
    def peek(self):
        return self.items[len(self.items)-1]
        
    def size(self):
        return len(self.items)
        
    
    def __str__(self):
        return  str(self.items)

st=Stack()

st.push(5)
st.push(6)



print st.peek()

st.pop()

print st


st.pop()

print(st)
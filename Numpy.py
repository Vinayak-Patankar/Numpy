# -*- coding: utf-8 -*-
"""
Created on Thu May 11 12:55:04 2023

@author: user
"""
'''numpy:- Numerical Python
it will perform mathematical operation
it will use in solve integration,derivative,Trignometry
matrix and vector

it is fast than list 100x

import numpy as np
a=np.array([11,12,3,4,5])#it will create array  and dimension it is single dimension
a.dtype
a.ndim   #it will show u how many dimension it is
a1=np.array([11,12,3,4,5,'a','b'])
a1.dtype
a2=np.array([[11,12,3,4,5]])#it is 2dimension bcuz of double bracket
a2.dtype
a2.ndim
'''
#a[row_column,col_num]#by like this we have to do operation
'''import numpy as np
a=np.array([[10,20,30],[40,50,60],[70,80,90]])
b=np.array([['Shahrukh Khan',"Usain Bolt","Narendra Modi",'Anurag Kashyap'],['Actor',"Athlete","Politician","Director"],["Male","Male","Male","Male"],["Mumbai","Africa","Gujarat","India"]])                                    
a
a[1:,1:]
a[1:,0:2]
a[0:2,0:2]
a[0:2,1:]
b
b[2:,2:]
b[2:,0:2]
b[0:2,2:]
b[0:2,0:2]

m=np.array([[10,20,30,40,50],[70,80,90,100,110],[120,130,140,150,160],[170,180,190,200,210],[220,230,240,250,260]])
m
#4x4
m[0:4,0:4]
m[1:,1:]
#3x3
m[1:4,1:4]#middle one
m[1:4,2:]
#2x2
m[2:4,2:4]
m[3:,3:]#left corner down
m[:2,3:]#left corner up
m[3:,:2]#right corner down
m[:2,:2]#right corner up
m[1:3,2:4]#middle
m
----------------------------------------------------------------------------------------------------------------------------------------------------------------

import numpy as np
a=np.array([[10,20,30],[40,50,60],[70,80,90]])
b=np.array([[1,2,3],[4,5,6],[7,8,9]])
#Function of numpy
np.max(a)
np.min(a)
np.sqrt(a)
np.exp(a)
np.add(a,b)
np.subtract(a,b)
np.divide(a,b)
np.multiply(a,b)
#np.arange(start, stop)
a1=np.arange(5)#arange is similar like range it will give number upto 5
a1=np.arange(5,15)#in this we are giving start and stop so start is 5 and stop is 15
a1=np.arange(5,15,3)#in this we are giving start and stop so start is 5 and stop is 15 and also step is between 3
a1
#np.linspace(start,stop,how much part)
np.linspace(1,4,5)#linspace means we are giving 1 to 4 number we need 5 parts of it
np.linspace(1,4,9)#linspace means we are giving 1 to 4 number we need 9 parts of it

x=np.zeros(5)#in this all elements will be zero
x=np.zeros((6,6))
x=np.ones((6,6)))#in this all elements will be one
x
x.size
x.shape
x.reshape((-1))
x.reshape((4,9))#not flexible, all 36 element should be there in matrix
np.resize(x,(7,7))
#-------------------------------------------------------------------------------------------
m=np.arange(49)
m=np.resize(m,(7,7))
m.reshape((6,6))
np.max(m)
np.min(m)
np.sqrt(m)
m[2:5,2:5]
m[0:,0]
m[0:3,0:3]
m[0:2,0:2]
m
m[:,[0,6]]#slicing like iloc
np.argmax(m)#giving index of maximum number
np.argmin(m)#giving index of minimum number
np.argmax(m,axis=0)#giving index of maximum number column wise
np.argmin(m,axis=1)#giving index of minimum number row wise
# -----------------------------------------------------------------

import numpy as np
a=np.array([[0,22,555,6],[22,33,4,5]])
np.where(a%11,'even','odd')#if Condition is True then give x and false then give y at that place in matrix
a
np.array([[0,22,555,6],[22,33,4,5],[11,56,54,5]],ndmin=4)#ndmin is use to give dimension
# ------------------------------------------------------------------------------------------------------------
#typecasting and giving storage to it
#homework 
a=np.array([5,5,145,65215],dtype=np.int8)#why this happening and how to solve it do task
#int 8 bit =2^8=0 to 255
a
b=np.array([5,6,7],np.float16)#here we are giving 16 storage 
b
c=np.array([[5,6,7],[8,9,45645461]],dtype=np.str)# it will take maximum number length in string this happens
c
--------------------------------------------------------------------------------------------------------
#sorting
import numpy as np
a=np.array([[0,22,555,6],[22,33,4,5]])
np.sort(a,axis=1)#sorting in row wise
np.sort(a,axis=0)#sorting in column wise
np.argsort(a,axis=1)#index will show which index is there in sort values in row
np.argsort(a,axis=0)#index will show which index is there in sort values in column

import numpy as np
a=np.array([5,5,145,-254],dtype=np.int8)#put there int32 bcuz the given number are large and it will overflow and it is not in range of int8 & int16
np.abs(a)#it will convert data in positive
b=np.uint8(a)#unsigned integer it will give same data and all data in positive 
print(b)
a
# -------------------------------------------------------------------------------------------------------------------
a=np.array([2,45,6,6,64,8,84,5])
np.split(a,[1,3])#here in split function it will split array from 0 to 1 then 1 to 3 and then 3 to all data.
np.split(a,[2,5,3])#here in split function it will split array from 0 to 2 then 2 to 5 and then 5 to 3, but 5 to 3 it will go in reverse thats why emptyafter that 3 to all data 

b=np.array([[2,4,5],[6,7,8],[9,10,11]])
np.split(b,[1])#in this u will get 0 to 1 and 1 to all data
b
'''






























































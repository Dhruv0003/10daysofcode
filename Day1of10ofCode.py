#!/usr/bin/env python
# coding: utf-8

# In[1]:



print(2 + 3)   # addition(+)
print(3 - 1)   # subtraction(-)
print(2 * 3)   # multiplication(*)
print(3 / 2)   # division(/)
print(3 ** 2)  # exponential(**)
print(3 % 2)   # modulus(%)
print(3 // 2)  # Floor division operator(//)

# Checking data types

print(type(10))                  # Int
print(type(3.14))                # Float
print(type(1 + 3j))              # Complex
print(type('Dhruv'))          # String
print(type([1, 2, 3]))           # List
print(type({'name':'Dhruv'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Tuple


# In[2]:


#Python Program to Print Hello world!
print("Hello Word")


# In[5]:


#Python Program to Add Two Numbers
a,b = 2,3
print(a+b)

def adder(a,b):
    return a+b

print(adder(2,3))

#Adding using Python lambda
x=(lambda a,b:a+b)
print(x(2,3))


# In[8]:


# Python Program to calculate the square root

d =(lambda x,y:x**y)
print(d(3,3))


def square_root(x,y):
    return x**y

print(square_root(3,3))


# In[14]:


#Python Program to Calculate the Area of a Triangle

base =  int(input("Enter a number "))
height = int(input("Enter a height "))

print(1/2*base*height)


def area_triangle(base,height):
    return 1/2*base*height

print(area_triangle(5,12))


f = (lambda x,y: 1/2*x*y)
print(f(5,12))


# In[25]:


#Python Program to Swap Two Variables

a,b = 3,5
a,b = b,a
print(a)
print(b)

print("\n")

def swap_program(a,b):
    print("Value before a: "+str(a)+' b: '+str(b))
    temp = a
    a = b
    b = temp
    return a,b


x,y = swap_program(3,5)
print("Value before a: "+str(x)+' b: '+str(y))  


print("\n")

#swap using addition and substraction

d = 9
r = 8
print("Swap value using addition and substraction Value before a: "+str(d)+' b: '+str(r))  
s = d+r
r = s-r
d = s-r
print("Swap value using addition and substraction Value before a: "+str(d)+' b: '+str(r))  


print("\n")

#swap using addition and substraction

d = 9
r = 8
print("Swap value using division and multiplication Value before a: "+str(d)+' b: '+str(r))  
s = d*r
r = s/r
d = s/r
print("Swap value using division and multiplication Value before a: "+str(d)+' b: '+str(r))  


# In[44]:


import random
  
random.seed(10) 
  
# print a random number between 1 and 1000. 
print(random.randint(1, 10))

print(random.getstate())

print(random.randint(1, 10))

#Same number is generated as we are using same seed value
random.seed(10) 
print(random.randint(1, 10))

print(random.randint(1, 10))

print(random.randint(1, 10))

print(random.getrandbits(8))


# In[47]:


#Python Program to Convert Kilometers to Miles

x = (lambda a :0.621371*a)
print(x(3))


def km_to_miles(a):
    return 0.621371*a

print(km_to_miles(10))


# Taking kilometers input from the user
kilometers = float(input("Enter value in kilometers: "))

# conversion factor
conv_fac = 0.621371

# calculate miles
miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))


# In[52]:


#Python Program to Convert Celsius To Fahrenheit


# change this value for a different result
celsius = 37.5

# calculate fahrenheit
fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))



def frahtocel(celsius):
    return (celsius * 1.8) + 32

def celtofrah(fahrenheit):
    return (fahrenheit - 32) / 1.8


print(frahtocel(37.5))
print('Fahrenheit to Celsius')
print(celtofrah(99.5))


# In[59]:


#Python Program to Check if a Number is Positive, Negative or 0

number = int(input("Enter a number "))

def number_check(number):
    
    if number > 0:
        return 'positive'
    else:
        return 'negative'

    
print(number_check(number))


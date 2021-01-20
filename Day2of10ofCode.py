#!/usr/bin/env python
# coding: utf-8

# In[13]:


#Python Program to Check if a Number is Odd or Even


def check_number(number):

    if type(number) == int:
        if number%2==0:
            return 'even'
        else:
            return 'odd'
    else:
        return "Please provide valid number"

print(check_number('ab'))


#oneliner lambda function

s = (lambda x : 'even' if x%2==0 else 'odd'  )

print(s(4))


# In[17]:


#Python Program to Check Leap Year

"""
Leap year is a year which is divisible by 4 
except the Centurian year (ending with 00 )

1900 is a not leap year
2012 is a leap year
2000 is a leap year

"""

def check_year(x):
     if type(x) == int:
            if x%4 == 0 and x%100 ==0:
                return print("{0} is a leap year".format(x))
            else:
                return print("{0} is a not leap year".format(x))
                
check_year(1900)


# In[22]:


#Python Program to Find the Largest Among Three Numbers

a = [1,833,9]

max = a[0]

for x in a:
    if x > max:
        max = x
print(max)


#largestfunction using args

def function_largest(*args):
    
    max = args[0]
    
    for x in args:
        if x > max:
            max = x
    
    return max

function_largest(6,89,55,2000)


# In[60]:


# Program to check if a number is prime or not

num = int(input("Enter a integer number "))

if num > 1:
    for x in range(2,num):
        if num%x==0:
            print(str(num)+" is not prime number")
            break
        else:
            print(str(num)+" is the prime number")
            break
else:
    print("Number should be greater than one ")
        


# In[72]:


#Python Program to Print all Prime Numbers in an Interval

start = int(input("Enter a starting number "))
end = int(input("Enter a ending number "))


for x in range(start,end+1):
    for i in range(2, x):
        if (x % i) == 0:
            break
    else:
        print(i)
    
    


# In[83]:


#Python Program to Find the Factorial of a Number





def fact(n):
    fact = 1
    if n < 0:
        return "factorial does not exist for negative numbers"
    elif n == 0:
        return "The factorial of 0 is 1"
    else:
        for i in range(1,n + 1):
            fact = fact*i
        
        return fact
        


print(fact(5))


#usingrecursion

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

factorial(5)


# In[90]:


#Python Program to Display the multiplication Table

number = int(input("Enter a number for multiplcation "))


for i in range(1,11):
    print('\n The {} number is multiplied by {} and there multipliaction is {}'.format(number,i,number*i))
    


# In[102]:


#Python Program to Print the Fibonacci sequence

n = 0
p = 1

c = 0
count = 7
while c < count:
    print('The number {} n and p is {} after swap'.format(n,p))
    s = n + p
    n = p
    p = s
    c = c + 1
    
    
print(s)
    


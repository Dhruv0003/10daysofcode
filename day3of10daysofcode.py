#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Python Program to Find the Sum of Natural Numbers

start = int(input("Enter a start number "))
end   = int(input("Enter a end number "))

sum = 0
for i in range(start,end+1):
    sum = sum + i
    print(sum)
    
print('the total sum is {}'.format(sum) )    


# In[7]:


# Sum of natural numbers up to num

num = 5

if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   # use while loop to iterate until zero
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)


# In[18]:


# Display the powers of 2 using anonymous function

terms = 5

res = list(map(lambda x: 2 ** x, range(terms)))

print("The total terms are:",terms)

for i in range(terms):
   print("2 raised to power",i,"is",res[i])


# In[31]:


#Python Program to Find Numbers Divisible by Another Number

number = int(input("enter a number "))

for x in range(2,11):
    if number%x==0:
        print('The number is divisible by {}'.format(x))
else:
    print('The number {} is divisible by itself'.format(number))


# In[34]:


#Python Program to Convert Decimal to Binary, Octal and Hexadecimal


num = 566

print("The decimal value of {} is:".format(num))
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")


# In[36]:


# Program to find the ASCII value of the given character

c = 'a'
print("The ASCII value of '" + c + "' is", ord(c))


# In[42]:


#Python Program to Make a Simple Calculator

def sum_two(*args):
    sum = 0
    for i in args:
        sum = sum+i
    return sum

def mul_two(*args):
    mul = 1
    for i in args:
        mul = mul*i
        
    return mul

def div_two(x,y):
    if x < 0 or y < 0:
        return 'Both Number should be greater than zero'
    else:
        return x/y
        


print(mul_two(2,3))
print(sum_two(1,2,3,4,5,6,7,8,9,10))
print(div_two(10,2))


# In[48]:


#Python Program to Display Calendar


# importing calendar module
import calendar

yy = 2020  # year
mm = 11    # month

# display the calendar
print(calendar.month(yy, mm))


# In[49]:


print(calendar.calendar(2020))


# In[53]:


# Python program to display the Fibonacci sequence

def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10

# check if the number of terms is valid
if nterms <= 0:
    print("Plese enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(recur_fibo(i))


# In[63]:


#Python Program to Find Sum of Natural Numbers Using Recursion

sum1= 0
def sum_func(n):
    if n == 1:
        return n
    else:
        return n+sum_func(n-1)

sum_func(16)


# In[76]:


# Program to add two matrices using nested loop


X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]


# In[72]:


for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]


# In[74]:


for x in range(len(result)):
    print(result[x])


# In[75]:


#Program to transpose a matrix using a nested loop

X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)


# In[78]:


for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j]= X[i][j]*Y[i][j]


# In[79]:


for x in result:
    print(x)


# In[91]:


#Python Program to Check Whether a String is Palindrome or Not


def pal_str(s):
    p = ''
    
    for w in s:
        p = w+p
    
    if s==p:
        return True
    else:
        return False


pal_str('dad')


# In[93]:


def pal_str2(s):
    
    if s==s[::-1]:
        return True
    else:
        return False
    
pal_str2('dad')


# In[98]:


# Python code to reverse a string 
# using recursion 

def reverse(s): 
    if len(s) == 0: 
        return s 
    else: 
        return reverse(s[1:]) + s[0] 

s = "start"

print ("The original string is : ",end="") 
print (s) 

print ("The reversed string(using recursion) is : ",end="") 
print (reverse(s)) 


#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Python Program to Accept Three Digits and Print all Possible Combinations from the Digits


a = input("Enter first number \n")
b = input("Enter second number \n")
c = input("Enter third number \n")

d = []

d.append(a)
d.append(b)
d.append(c)

for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if(i!=j&j!=k&k!=i):
                print(d[i],d[j],d[k])


# In[2]:


#4 number


a = input("Enter first number \n")
b = input("Enter second number \n")
c = input("Enter third number \n")
d = input("Enter fourth number \n")

e = []

e.append(a)
e.append(b)
e.append(c)

for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            for l in range(0,3):
                if(i!=j&j!=k&k!=i):
                    print(e[i],e[j],e[k],e[l])


# In[3]:


#Python Program to Print Odd Numbers Within a Given Range


start = int(input("Enter the first number"))
end = int(input("Enter the second number"))

for i in range(start,end):
    if i%2==0:
        pass
    else:
        print(i)


# In[8]:


#Python Program to Find the Sum of Digits in a Number


#wrong approach

t = 123

sum = 0

for i in str(t):
    sum = sum+int(i)
    


# In[9]:


print(sum)


# In[12]:


#rightapproach

t = 999
s = 0
while t > 0:
    dig = t%10
    s = s+dig
    t = t//10
    


# In[13]:


print(s)


# In[15]:


#Python Program to Read a Mumber n and Compute n+nn+nnn


def compute(n):
    return n+n+n+n+n+n

print(compute(5))


# In[18]:


n=int(input("Enter a number n: \n"))
temp=str(n)
t1=temp+temp
print(t1)
t2=temp+temp+temp
print(t2)
comp=n+int(t1)+int(t2)
print("The value is:",comp)


# In[22]:


#Python Program to Find the Smallest Divisor of an Integer

n=int(input("Enter an integer:"))

a=[]

for i in range(2,n+1):
    if(n%i==0):
        a.append(i)

a.sort()

print("Smallest divisor is:",a[0])


# In[27]:


#Python Program to Count the Number of Digits in a Number

digit = int(input("Enter a digit :  "))

count = 0
while digit>0:
    
    count = count+1
    digit = digit//10


# In[28]:


print(count)


# In[44]:


#check if number is palimdrome

"""
palimdrome is a number which is equal to its reverse number

121 = 121 is palimdrone
321 = 123 is not palimdrone

"""


        
def check_palindrone(n):
    dig =0 
    
    while(n>0):
        rem = n % 10
        dig = dig*10+rem
        n = n//10
    
    return dig



n = int(input("Enter a number"))
m = check_palindrone(n)


if m==n:
    print('It is palindrome')
else:
    print('It is not palindrome')        


# In[33]:


print(dig)


# In[51]:


#Python Program to Print all Integers that Aren't Divisible by Either 2 or 3 and Lie between 1 and 50.


for i in range(0,50):
    if i%2!=0 and i%3!=0:
        print('These numbers are {}'.format(i))
        


# In[78]:


#Python Program to Read a Number n And Print the Series "1+2+…..+n= "


n=int(input("Enter a number: "))
q=[]
su = 0
for i in range(1,n+1):
    if(i<n+1):
        print(su)
        print(i)
        su = su+i
        
        
print("\n")
print(su)


# In[77]:


print(su)


# In[82]:


n = 4
for i in range(0,n):
    for j in range(0,n):
        if i==j:
            print("1",sep=" ",end=" ")
        else:
            print("0",sep=" ",end=" ")
    print()


# In[91]:


#Python Program to Print an Inverted Star Pattern



n=int(input("Enter number of rows: "))
for i in range (n,0,-1):
    print((n-i) * ' ' + i * '*')
    

    


# In[92]:


#Python Program to Check if a Date is Valid and Print the Incremented Date if it is


date=input("Enter the date: ")

dd,mm,yy=date.split('/')

dd=int(dd)

mm=int(mm)

yy=int(yy)

if(mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
    max1=31
elif(mm==4 or mm==6 or mm==9 or mm==11):
    max1=30
elif(yy%4==0 and yy%100!=0 or yy%400==0):
    max1=29
else:
    max1=28
if(mm<1 or mm>12):
    print("Date is invalid.")
elif(dd<1 or dd>max1):
    print("Date is invalid.")
elif(dd==max1 and mm!=12):
    dd=1
    mm=mm+1
    print("The incremented date is: ",dd,mm,yy)
elif(dd==31 and mm==12):
    dd=1
    mm=1
    yy=yy+1
    print("The incremented date is: ",dd,mm,yy)
else:
    dd=dd+1
    print("The incremented date is: ",dd,mm,yy)


# In[93]:


#Python Program to Compute Simple Interest Given all the Required Values

principle=float(input("Enter the principle amount:"))
time=int(input("Enter the time(years):"))
rate=float(input("Enter the rate:"))





def si(a,b,c):
    return a*b*c/100

s = si(principle,time,rate)

print("The simple interest is:",s)

 









# In[95]:


#Python Program to Check Whether a Given Year is a Leap Year

year=int(input("Enter year to be checked:"))

if(year%4==0 and year%100!=0 or year%400==0):
    print("The year is a leap year!")
else:
    print("The year isn't a leap year!")


# In[96]:


#Python Program to Read Height in Centimeters and then Convert the Height to Feet and Inches

cm=int(input("Enter the height in centimeters:"))
inches=0.394*cm
feet=0.0328*cm
print("The length in inches",round(inches,2))
print("The length in feet",round(feet,2))


# In[99]:


#Python Program to Find the Largest Number in a List

a = [1,5,8,900,10]

mx = 0

for i in a:
    if i > mx:
        mx = i
        


# In[100]:


print(mx)


# In[101]:


#Python Program to Find the Second Largest Number in a List

a = [1,5,8,900,10]

a.sort()

a[-2]


# In[104]:


#Python Program to Put Even and Odd elements in a List into Two Different Lists


a = [1,5,8,900,10,2,6,9,3,2,5,10,23,44,55]

elist = []
olist = []

for i in a:
    if i%2==0:
        elist.append(i)
    else:
        olist.append(i)
        


# In[107]:


print("The even list",elist)
print("The odd list",olist)


# In[110]:


#Python Program to Merge Two Lists and Sort it

a = [8, 900, 10, 2, 6, 2, 10, 44]
b = [1, 5, 9, 3, 5, 23, 55]

c = a+b
print("Merging rows")
print(c)
print("Merging rows and sorting")
c.sort()
print("After sort")
print(c)


# In[111]:


a=[]

n=int(input("Enter number of elements:"))

for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
for i in range(0,len(a)):
    for j in range(0,len(a)-i-1):
        if(a[j]>a[j+1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp 


print('Second largest number is:',a[n-2])


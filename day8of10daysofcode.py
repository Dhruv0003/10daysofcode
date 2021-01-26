#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Python Programming Examples on Strings

s = 'This is a program which is part of 10 days of course '
#Python Program to Replace all Occurrences of ‘a’ with $ in a String

print("String before {}".format(s))

s = s.replace('a','$')

print("String after {}".format(s))


# In[ ]:


#Python Program to Remove the nth Index Character from a Non-Empty String


w = 'Hello'

print(w[:3])
print(w[4:])


print(w[:4]+w[4:])


# In[ ]:


p1 = input("enter first string \n")
p2 = input("enter second string \n")

if (sorted(p1)==sorted(p2)):
    print("The strings are anagrams")
else:
    print("The strings aren't anagrams")


# In[ ]:


#Python Program to Form a New String where the First Character and the Last Character have been Exchanged


s = "hello w orld"

print(s[-1]+s[1:-1]+s[0])

#or 

print(s[-1:] + s[1:-1] + s[:1])


# In[ ]:


#Python Program to Count the Number of Vowels in a String

s=  "welcome"
vowels = ["a","e","i","o","u"]
count = 0
for i in s.lower():
    if i in vowels:
        count += 1
        
print(count)


# In[ ]:


#2nd approach
for i in s:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        count=count+1


# In[ ]:


#Python Program to Take in a String and Replace Every Blank Space with Hyphen

d = "Hello World"

d = d.replace(" ","-")


# In[ ]:


d


# In[ ]:


#Python Program to Calculate the Length of a String Without Using a Library Function


r = input("Enter a string \n")

count = 0

for i in r:
    count += 1

#print(count)


# In[ ]:


print(count)


# In[ ]:


#Python Program to Remove the Characters of Odd Index Values in a String
old_string = "Hello"

def new_st(old_string):
    p = ""
    
    for i in range(len(old_string)):
  
        if i%2==0:
            p = p+old_string[i]
            
    
    return p

w = new_st(old_string)
print(w)


# In[ ]:


#Python Program to Calculate the Number of Words and the Number of Characters Present in a String

s = "This is my code which is part of my goal"

list_words = s.split(" ")

print('These are the list of words {}'.format(list_words))
count = 0 
for i in list_words:
    for j in i:
        count += 1
    
print('These are the characters in these words {}'.format(count))    
    


# In[ ]:


#Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions

s = "This is my code which is part of my goal"
d = "Hello world"

def larger_string(s,d):
    s1_list_words =  s.strip()
    d1_list_words =  d.strip()
    
    s1_count = 0
    d1_count = 0
    
    for i in s1_list_words:
        s1_count += 1
        
    for i in d1_list_words:
        d1_count += 1
    
    if d1_count>s1_count:
        print("This string is greater : {0} with words {1} ".format(d,d1_count))
    else:
         print("This string is greater : {0} with words {1} ".format(s,s1_count))
            
            
larger_string(s,d)


# In[ ]:


#Python Program to Count Number of Lowercase Characters in a String

f = "heLLo woRLd"
count = 0

for i in f:
    if i.islower()==True:
        count += 1
    
print(count)


# In[ ]:


#Python Program to Check if a String is a Palindrome or Not


s = "dad"
p = ""
for i in s[::-1]:
    p = p+i
    
if s==p:
    print('The string is palindrome {0}'.format(p))
else:
    print('The string is not palindrome {0}'.format(s))


# In[ ]:


#Python Program to Calculate the Number of Upper Case Letters and Lower Case Letters in a String

f = "heLLo woRLd" 

u_count = 0
l_count = 0


for i in f:
    if i.islower()==True:
        l_count += 1
    elif i.islower()==False and i != " ":
        u_count += 1
    else:
        pass
    
    
        
print("The numbers of letter in string , uppercase : {0} , lowercase : {1}".format(l_count,u_count))


# In[ ]:


#Python Program to Check if a String is a Pangram or Not

from string import ascii_lowercase as asc_lower
def check(s):
    return set(asc_lower) - set(s.lower()) == set([])

strng = input("Enter string:")
if(check(strng)==True):
      print("The string is a pangram")
else:
      print("The string isn't a pangram")


# In[ ]:


#Python Program to Accept a Hyphen Separated Sequence of Words as Input and Print the Words in a Hyphen-Separated Sequence after Sorting them Alphabetically



r = input("Enter a hypen separeted string \n")

list_r = r.split("-")

list_r.sort()

print("-".join(list_r))


# In[ ]:


#Python Program to Calculate the Number of Digits and Letters in a String

#Hello123
p = input("Enter a string with digits \n")

count_d = 0
count_c = 0

for i in p:
    if i.isdigit() == True:
        count_d += 1
    else:
        count_c += 1


print(count_c)
print(count_d)


# In[ ]:


#Python Program to Form a New String Made of the First 2 and Last 2 characters From a Given String

string_o = "Hello"


def change(s):
    return s[:2]+s[-2:]

new_string = change(string_o)
print(new_string)


# In[2]:


#Python Program to Count the Occurrences of Each Word in a Given String Sentence


f =  input("enter string \n")

d = {}

def change(f):
    
    f_list = f.split(" ")

    for i in f_list:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    print(d)

change(f)


# In[6]:


##Python Program to Count the Occurrences of Each Word in a Given String Sentence
"""
if user inputs the string and word
"""

#Python Program to Count the Occurrences of Each Word in a Given String Sentence


f =  input("enter string \n")

p = input("enter word \n")

count = 0

for i in f.split(" "):
    if i == p:
        count += 1
    
    

print(count)


# In[8]:


#Python Program to Check if a Substring is Present in a Given String


string =  input("enter a string")

sub =  input("enter a substring")

if(string.find(sub)==-1):
      print("Substring not found in string!")
else:
      print("Substring in string!")


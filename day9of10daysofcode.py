#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Python Program to Add a Key-Value Pair to the Dictionary

key =  input("Enter a student name")
value =  int(input("Enter marks"))
d= {}
d.update({key:value})
print(d)


# In[4]:


#Python Program to Concatenate Two Dictionaries Into One

d = {"Kilo":100,"Yoki":200}
l = {"Milo":100,"Loki":200}

d.update(l)

print(d)


# In[8]:


#Python Program to Check if a Given Key Exists in a Dictionary or Not

d = {"Kilo":100,"Yoki":200}

p = input("Enter key you want to search")

for x,y in d.items():
    if x == p:
        print("Value exists")



# In[9]:


#2nd appprach using key method

if p in d.keys():
    print("Value exists and it is value ")
    print(d[p])
else:
    print('Value not found')


# In[11]:


#Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).
n = int(input("Enter n number "))

d = {}
for x in range(1,n+1):
    d[x]=x*x
    
    
print(d)


# In[13]:


{x:x*x*x for x in range(1,n)}


# In[20]:


#Python Program to Sum All the Items in a Dictionary
d = {"Kilo":100,"Yoki":200}

sum = 0

for x in d.values():
    print(x)
    sum = sum+x
    
print(sum)


# In[22]:


#Python Program to Multiply All the Items in a Dictionary

d = {"Kilo":100,"Yoki":200,"koki":900}

mul = 1 

for x in d.values():
    mul = mul*x
    
print(mul)


# In[28]:


#Python Program to Remove the Given Key from a Dictionary

m = {"Kilo":100,"Yoki":200,"koki":900}

m.pop("koki")


# In[29]:


m


# In[27]:


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964}
thisdict.pop("model")
print(thisdict)


# In[30]:


del thisdict['year']


# In[31]:


thisdict


# In[36]:


#Python Program to Form a Dictionary from an Object of a Class


class B:
    """
    Code runs well
    """
    def __init__(self):
        self.A = "Coderun003"
        self.B = "Loop"

B()
print(B.__dict__)
print(B.__doc__)


# In[38]:


#Python Program to Map Two Lists into a Dictionary

r = [1,3,4,5,6,7,8,100,9]

e = [1,32,43,54,68,78,89,10]

dw = dict(zip(r,e))
print("The dictionary is:")
print(dw)


# In[40]:


#Enter a string 


s = input("Enter a string \n")

t = s.split(" ")
f = {}

for x in t:
    if x not in f:
        f[x]=1
    else:
        f[x]=f[x]+1
        
print(f)


# In[42]:


test_string=input("Enter string:")
l=[]
l=test_string.split()
wordfreq=[l.count(p) for p in l]
print(dict(zip(l,wordfreq)))


# In[44]:


#Python Program to Create a Dictionary with Key as First Character and Value as Words Starting with that Character

test_string=input("Enter string:")
l=test_string.split()
d={}
for word in l:
    if(word[0] not in d.keys()):
        d[word[0]]=[]
        d[word[0]].append(word)
    else:
        if(word not in d[word[0]]):
          d[word[0]].append(word)
for k,v in d.items():
        print(k,":",v)


# In[49]:


#Python Program to Read the Contents of a File


a=input("Enter the name of the file with .txt extension:")
file2=open(a,'r')
line=file2.readline()

while(line!=""):
    print(line)
    line=file2.readline()
file2.close()


# In[53]:


#Python Program to Count the Number of Words in a Text File
fname = input("Enter file name: ")
 
num_words = 0
 
with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)
        
print("Number of words:")
print(num_words)


# In[55]:


#Python Program to Count the Number of Lines in a Text File

a=input("Enter the name of the file with .txt extension:")
file2=open(a,'r')
line=file2.readline()
count = 0
while(line!=""):
    print(line)
    line=file2.readline()
    count += 1
    

print(count)
file2.close()


# In[56]:


fname = input("Enter file name: ")
num_lines = 0
with open(fname, 'r') as f:
    for line in f:
        num_lines += 1
print("Number of lines:")
print(num_lines)


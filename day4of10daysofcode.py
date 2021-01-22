#!/usr/bin/env python
# coding: utf-8

# In[1]:


#List Comprehension

"""
List comprehensio  means performing the opertions on the list to create a new list
"""


List1 = [1,3,54,56,6,6]

list1_double1 = [x*2 for x in List1 ]


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


# In[2]:


list1_double1


# In[4]:


newlist = [x for x in range(10) if x%2==0]


# In[5]:


newlist


# In[6]:


newlist = [x.upper() for x in fruits]


# In[7]:


newlist


# In[8]:


#if we want to setup all values to flowers in list


newlist = ['Tomato' for x in fruits]


# In[9]:


newlist


# In[10]:


newlist = [x if x != "banana" else "Good" for x in fruits]


# In[12]:


#List variable can be accessed by index
newlist[1]


# In[13]:


#Access last variable
newlist[-2]


# In[16]:


#access 2 index to 5 index value
newlist[2:5]


# In[17]:


#second list from last
newlist[:4]


# In[20]:


#complete list
newlist[:5]


# In[22]:


newlist[1] = 'Team'


# In[23]:


newlist


# In[24]:


#changing multiple value simuntaneoulsy

newlist[1:3] = ['AB','DF','HJ']


# In[25]:


newlist


# In[26]:



#replacing second value
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)


# In[27]:


thislist = ["apple", "banana", "cherry"]


# In[29]:


thislist.insert(2, "watermelon")
print(thislist)
#insert method takes the index number and value that needs to be replaced


# In[39]:


#append method appends the value at the end of the list

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


# In[31]:


#using pop to remove the value by passing the index no.

thislist.pop(1)


# In[32]:


#using pop to remove the last value by passing no value
thislist.pop()


# In[33]:


thislist[0]


# In[34]:


#to delete the entire list

del newlist


# In[35]:


#using clear functiont to empty the list

newlist=  thislist


# In[36]:


newlist.clear()


# In[42]:


#loopusinglist 1) For


thislist = ["apple", "banana", "cherry","watermelon"]

for x in thislist:
    print(x)


# In[45]:


for i in range(len(thislist)):
    print(thislist[i])


# In[47]:


slist = ["Pp", "Lpa", "cherry"]
i = 0
while i < len(slist):
  print(slist[i])
  i = i + 1


# In[49]:


i = len(slist)
while i > 0:
  i = i - 1
  print(slist[i])
 


# In[50]:


slist


# In[55]:


#how to reverse the list 

i = len(slist)
reverse_list = []

while i > 0:
    i = i - 1
    #print(slist[i])
    reverse_list.append(slist[i])


# In[56]:


reverse_list


# In[60]:


reverse_list.sort()


# In[62]:


reverse_list.sort(reverse=True)


# In[63]:


#sort the list by how close the number is to 10 
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


# In[65]:


thislist = ["Banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)


# In[66]:


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


# In[68]:


#we cannot simply use list1=list2 because list2 will be referencing to old code

mylist = thislist.copy()
print(mylist)

#or using list method
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)


# In[69]:


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


# In[73]:


list1 = ["123"]
list2 =  ["435"]
print(int(list1[0])+int(list2[0]))


# In[79]:


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)


# In[80]:


list1


# In[76]:


list1.extend(list2)


# In[77]:


list1


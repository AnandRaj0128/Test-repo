#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.Manipulating the list
#1i.to add new elements to the end of the list
l = [1,2,3,4,5]
l
l.append(6)
l


# In[2]:


#1ii. to reverse elements in the list
l.reverse()
l


# In[4]:


#1iii. to display same list of elements multiple times
m = l * 2 
m


# In[5]:


#1iv. to sort list in ascending order
nl = [3,5,7,35,50,1,9]
nl.sort()
nl


# In[6]:


#2.write a python program to do in the tuples.
#2i. manipulate using tuples
t = (1,4,5,1,4,'Python','Anand','Pawan','Darshan','Shrini')
t


# In[7]:


i = t.index('Shrini')
i


# In[8]:


c = t.count(1)
c


# In[9]:


l = len(t)
l


# In[12]:


#2ii.to add elements at the end of tuple
y = list(t)
y.append('Govind')
y


# In[13]:


#2iii.to reverse elements in the list
z = list(t)
z = z[::-1]
z


# In[14]:


#2iv. to displey elements of same tuple multiple times
ll = list(t)
lla = ll*3


# In[15]:


#2v.to concatenate two tuples
t1 = ('Anand','Raj')
t2 = ('Shrinivasan','Shridharan')
t3 = t1+t2
t3


# In[19]:


#2vi.sort the tuple elements in ascending order 
tup = (3,18,2,1,5,4,70,29)
res = sorted(tup)
res


# In[20]:


#3.write a python program to implement the following using list
#3i.create a list with integers(10characters)
l_int = [1,9,2,8,3,6,5,4,8,17,0]
l_int


# In[23]:


#3ii. display last element inth list
n = len(l_int)
last = l_int[n-1:]
last


# In[24]:


#3iii. command for displaying the values from[0:4]
print(l_int[0:4])


# In[25]:


#3iv. command for displaying the values from[0:4]
print(l_int[2:])


# In[26]:


#3v. command for displaying the values from[:6]
print(l_int[:6])


# In[27]:


#4.write a python program : tuple1 = (10,50,20,40,30)
tuple1 = (10,50,20,40,30)
tuple1


# In[28]:


#4i.display elements 10,50 from tuple1
tuple1[:2]


# In[29]:


#4ii.dislpay length of tuple1
print(len(tuple1))


# In[31]:


#4iii. find minimum element in tuple1
m = min(tuple1)
m


# In[34]:


#4iv. display same tuple1 elements multiple times
xyz = list(tuple1)
a =xyz*3
print(tuple(a))


# In[36]:


#5.write a python program
#5i.clculate the length of string
s ='Anand'
len(s)


# In[40]:


#5ii.reverse words in string
string = "Kohli Goes down He goes out of the ground"
s = string.split()[::-1]
l = []
for i in s:
    l.append(i)
print(" ".join(l))


# In[41]:


#5iv.concatenate two strings
s1 = "Sachin"
s2 = "Tendulkar"
print(s1+s2)


# In[42]:


#5v.str1 = "South India" usinng slicing print "India"
str1 = "South India"
print(str1[5:])


# In[45]:


#5iii.Display same string  multiple times
str3 = "PAWAN KALYAN  "
str3*3


# In[46]:


#6.perform the following 
#6i.Creating the dictionary
dic1 = {'Anand','Pawan',123,23.5,'Kalyan'}
dic1


# In[48]:


#6ii.accessing keys and values in dictionary
dic2 = {'name':'Anand','age':'22','gender':'male','id':'2575814'}
dic2


# In[49]:


len(dic2)


# In[52]:


dic2['name']


# In[53]:


dic2.get('age')


# In[60]:


#6iii.update dictionary using function
dic2.update({'age':10})
dic2


# In[65]:


#6iv.clear and delete the values of dictionary
dic2.clear()
dic2


# In[70]:


dic2.pop('age')
#again re-entered the values


# In[71]:


dic2


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# # Functions

# In[5]:


#1.write a function to list even and odd numbers
def even_or_odd(x,y):
    ev=[]
    odd=[]
    for i in range(x,y+1):
        if(i%2==0):
            ev.append(i)
        else:
            odd.append(i)
    print("Even:",ev)
    print("Odd:",odd)
print(even_or_odd(1,10))


# In[10]:


#2.print the count of even numbers from the input of 8 integers(1 at a time)
def even_count():
    c = 0
    for i in range(8):
        j = int(input("enter digit:"))
        if(j%2==0):
            c = c+1
    print(c)
even_count()


# In[13]:


#3.take positive integer n,if n is even - n/2.if nis odd 3n+1 repeat the process until you reach 1
def reach(n):
    seq = [n]
    if(n<1):
        return []
    while(n>1):
        if(n%2==0):
            n = n/2
        else:
            n = (3*n)+1
            seq.append(n)
    return seq
print(reach(12))


# In[ ]:


#4.calculte all the multiples of  3 or 5 below 500
def count():
    sum = 0
    for i in range(1,501):
        if(i%3==0 or i%5==0):
            sum = sum+i
    print(sum)
count()


# In[ ]:


#5.find first n prime  numbers from list of given numbers
for i in range(2,100):
    for j in range(2,i):
        if(j%i==0):
            break
    esle:
        print(j)
            


# ###### 

# In[ ]:





# In[ ]:





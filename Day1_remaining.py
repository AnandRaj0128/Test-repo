#!/usr/bin/env python
# coding: utf-8

# In[3]:


#7.create a python program to insert a number to any position of list
new_list = [1,2,3,4,7,8,9]
new_list.insert(5,50)
new_list


# In[5]:


#8.delete an element by index from list
new_list.pop(4)
new_list


# In[8]:


#9.display number from 1 to 100
for i in range(1,101): 
    print(i)


# In[9]:


#10.sum of all elements in a tuple
tup = (1,4,3,9)
sum = 0 
l = list(tup)
for i in range(len(l)):
    sum = sum+l[i]
print(sum)


# # control structures

# In[14]:


#1.python program to find first N prime numbers
n = int(input("Enter number:"))
for num in range (1,n):
    for i in range(2,num):
        if(num%i==0):
            break
    else:
        print(num)
    


# In[19]:


#2.python program to calculate salary of an employee #

basic=float(input("Enter Basic Salary :"))
da=float(basic*0.25)
hra=float(basic*0.15)
pf=float((basic+da)*0.12)
ta=float(basic*0.075)
netpay=float(basic+da+hra+ta)
grosspay=float(netpay-pf)

print("\n")
print(" BASIC SALARY : ",basic)
print(" DEARNESS ALLOW. : ",da)
print(" HOUSE RENT ALLOW.: ",hra)
print(" TRAVEL ALLOW. : ",ta)
print(" NET SALARY PAY : ",netpay)
print(" PROVIDENT FUND : ",pf)


# In[22]:


#3.python program to find a string from a list
l1 = ['A', 'B', 'C', 'D', 'A', 'A', 'C']
s = 'A'
m = []
i = 0
length = len(l1)

while i < length:
    if s == l1[i]:
        m.append(i)
    i = i+1

print(f'{s} is present in {l1} at indexes {m}')


# In[23]:


#4.find no. of uppecase letters from a string
s = "Anand RAj PspK"
c = 0
for i in s:
    if(i.isupper()):
        c = c+1
print(c)


# In[ ]:





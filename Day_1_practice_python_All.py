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


# In[3]:


#1iii. to display same list of elements multiple times
m = l * 2 
m


# In[4]:


#1iv. to sort list in ascending order
nl = [3,5,7,35,50,1,9]
nl.sort()
nl


# In[5]:


#2.write a python program to do in the tuples.
#2i. manipulate using tuples
t = (1,4,5,1,4,'Python','Anand','Pawan','Darshan','Shrini')
t


# In[6]:


i = t.index('Shrini')
i


# In[13]:


c = t.count(1)
c


# In[8]:


#2ii.to add elements at the end of tuple
y = list(t)
y.append('Govind')
y


# In[9]:


#2iii.to reverse elements in the list
z = list(t)
z = z[::-1]
z


# In[12]:


#2iv. to displey elements of same tuple multiple times
ll = list(t)
lla = ll*3


# In[14]:


#2v.to concatenate two tuples
t1 = ('Anand','Raj')
t2 = ('Shrinivasan','Shridharan')
t3 = t1+t2
t3


# In[15]:


#2vi.sort the tuple elements in ascending order 
tup = (3,18,2,1,5,4,70,29)
res = sorted(tup)
res


# In[16]:


#3.write a python program to implement the following using list
#3i.create a list with integers(10characters)
l_int = [1,9,2,8,3,6,5,4,8,17,0]
l_int


# In[17]:


#3ii. display last element inth list
n = len(l_int)
last = l_int[n-1:]
last


# In[18]:


#3iii. command for displaying the values from[0:4]
print(l_int[0:4])


# In[19]:


#3iv. command for displaying the values from[0:4]
print(l_int[2:])


# In[20]:


#3v. command for displaying the values from[:6]
print(l_int[:6])


# In[21]:


#4.write a python program : tuple1 = (10,50,20,40,30)
tuple1 = (10,50,20,40,30)
tuple1


# In[22]:


#4i.display elements 10,50 from tuple1
tuple1[:2]


# In[23]:


#4ii.dislpay length of tuple1
print(len(tuple1))


# In[24]:


#4iii. find minimum element in tuple1
m = min(tuple1)
m


# In[25]:


#4iv. display same tuple1 elements multiple times
xyz = list(tuple1)
a =xyz*3
print(tuple(a))


# In[26]:


#5.write a python program
#5i.clculate the length of string
s ='Anand'
len(s)


# In[27]:


#5ii.reverse words in string
string = "Kohli Goes down He goes out of the ground"
s = string.split()[::-1]
l = []
for i in s:
    l.append(i)
print(" ".join(l))


# In[28]:


#5iv.concatenate two strings
s1 = "Sachin"
s2 = "Tendulkar"
print(s1+s2)


# In[29]:


#5v.str1 = "South India" usinng slicing print "India"
str1 = "South India"
print(str1[5:])


# In[30]:


#5iii.Display same string  multiple times
str3 = "PAWAN KALYAN  "
str3*3


# In[31]:


#6.perform the following 
#6i.Creating the dictionary
dic1 = {'Anand','Pawan',123,23.5,'Kalyan'}
dic1


# In[32]:


#6ii.accessing keys and values in dictionary
dic2 = {'name':'Anand','age':'22','gender':'male','id':'2575814'}
dic2


# In[33]:


dic2.get('age')


# In[34]:


dic2['name']


# In[35]:


len(dic2)


# In[36]:


#6iii.update dictionary using function
dic2.update({'age':10})
dic2


# In[37]:


#6iv.clear and delete the values of dictionary
dic2.clear()
dic2


# In[38]:


dic2 = {'name':'Anand','age':'22','gender':'male','id':'2575814'}


# In[39]:


dic2.pop('age')


# In[40]:


#7.create a python program to insert a number to any position of list
new_list = [1,2,3,4,7,8,9]
new_list.insert(5,50)
new_list


# In[41]:


#8.delete an element by index from list
new_list.pop(4)
new_list


# In[42]:


#9.display number from 1 to 100
for i in range(1,101): 
    print(i)


# In[43]:


#10.sum of all elements in a tuple
tup = (1,4,3,9)
sum = 0 
l = list(tup)
for i in range(len(l)):
    sum = sum+l[i]
print(sum)


# In[ ]:


#11.create a directory three lsmbda funtions square,cube,square root
celsius = int(input("Celsius :"))
fahrenheit = (1.8 * celsius) + 32
print("Fahrenheit :", fahrenheit)


# In[ ]:





# In[ ]:





# In[ ]:





# # CONTROL STRUCTURES

# In[ ]:


#1.python program to find first N prime numbers
n = int(input("Enter number:"))
for num in range (1,n):
    for i in range(2,num):
        if(num%i==0):
            break
    else:
        print(num)
    


# In[ ]:


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


# In[ ]:


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


# In[ ]:


#4.find no. of uppecase letters from a string
s = "Anand RAj PspK"
c = 0
for i in s:
    if(i.isupper()):
        c = c+1
print(c)


# In[ ]:


#5. sum odd numbers and even numbers between 12 and 37
sum1 = 0
sum2 = 0
for i in range(12,38):
    if(i%2==0):
        sum1 = sum1+i
    else:
        sum2 = sum2+i
print("even sum:",sum1)
print("odd sum:",sum2)


# In[ ]:


#6.print the table of any number
n = int(input("enter any number:"))
for i in range(1,11):
    print(str(n)+"*"+str(i)+"=",n*i)


# In[ ]:


#7.sum of frist prime numbers
sum = 0
n = 10
for i in range(2,11):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        sum = sum + i
print(sum)
    


# In[ ]:


#8.arithmetic operatoins using nested if
a = 10
b = 15
o = (input("enter operator : "))
if(o=="+"):
    print(a+b)
elif(o=="-"):
    print(b-a)
elif(o=="*"):
    print(a*b)
elif(o=="/"):
    print(b/a)
elif(o=="%"):
    print(a%b)
    


# In[ ]:


#9.celsius to fahrenheit
celsius = int(input("Celsius :"))
fahrenheit = (1.8 * celsius) + 32
print("Fahrenheit :", fahrenheit)


# In[ ]:


#10.find min&max of a list without using built_in function
my_list = [2, 8, 4, 1, 7]
l = None
for n in my_list:
    if l is None or l<n:
        l = n
print("MAX:",l)  
m = None
for num in my_list:
    if m is None or num < m:
        m = num
print("MIN:",m)  


# In[ ]:


#12.print no.of seconds in an year
days=365
hours=24
minutes=60
seconds=60
print("Number of seconds in a year : ",days*hours*minutes*seconds)


# In[ ]:


#13.
s = 150 
d = 414
time = d/s 
print(time,"hrs")


# In[ ]:


#14.print the total hours spent from years 7-11
years = int(input) 
days = years*192
hours = days*6
print(days)


# In[ ]:


#15.print youngest among ram,sam and khan
ram = int(input("ram:"))
sam = int(input("sam:"))
khan = int(input("khan:"))
if(ram>sam and khan>sam):
    print("sam")
elif(khan>ram and sam>ram):
    print("ram")
else:
    print("khan")


# In[ ]:


#16.rotate a list right without using slicing
import numpy as np

if __name__ == '__main__':
    nums = [11, 4, 6, 7, 8, 33]
    k = 1
    x = np.roll(nums, k)
    print(x)


# In[ ]:


#17.i. print pascal trangle
# Print Pascal's Triangle in Python
from math import factorial

# input n
n = 5
for i in range(n):
    for j in range(n-i+1):
        print(end=" ")
    for j in range(i+1):
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
    print()


# In[ ]:


#17ii.
n = int(input())
for i in range(1,n+1):
    print("*"*i)


# In[ ]:


#17iii.
#17iii.
n = 5
for i in range(1,n+1):
    print("  "+" *"*i)


# In[ ]:


#17.iv.
string = input()
sp =""
for i in range(1,len(string)+1):
    print(sp+string[:i])


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


#6.matrix multiplication
A = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]
    

B = [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]

result = [[sum(a * b for a, b in zip(A_row, B_col))
           for B_col in zip(*B)]
          for A_row in A]

for r in result:
    print(r)


# In[2]:


#7.program to count the vowels in a string
string = "Hii Hello How are you"
vowels = "aeiouAEIOU"

count = sum(string.count(vowel) for vowel in vowels)
print(count)


# In[4]:


#8.find factorial using recursive funtion
def recur_factorial(n):
    if n == 1:
       return n
    else:
       return n*recur_factorial(n-1)

num = int(input("enter num:"))

# check if the number is negative
if num < 0:
   print("no factorial")
elif num == 0:
   print("The factorial  is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))


# In[6]:


#9.find fibinacci series using function
def fib():
    n = 10
    num1 = 0
    num2 = 1
    next_number = num2
    count = 1

    while count <= n:
        print(next_number, end=" ")
        count += 1
        num1, num2 = num2, next_number
        next_number = num1 + num2
        print()
fib()


# In[ ]:


#10.reverse a number without using built-in function
def rev():
    n = int(input("Enter Number : "))
    n = str(n)
    print(n[::-1])
rev()


# In[ ]:





# In[ ]:





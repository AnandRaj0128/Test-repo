#!/usr/bin/env python
# coding: utf-8

# # day-9

# In[8]:


#1.3x3x3 array
import numpy as n
r = n.random.rand(3, 4, 3)
print(r)


# In[2]:


#2.create a 5x5 matrix with values 1,2,3,4 just below the diagonal
import numpy as np
matrix = np.zeros((5, 5))
np.fill_diagonal(matrix[1:], [1, 2, 3, 4])
print(matrix)


# In[3]:


#3.create a 8x8 matrix and fill it with a checkboard pattern
import numpy as np
matrix = np.zeros((8, 8), dtype=int)
matrix[1::2, ::2] = 1
matrix[::2, 1::2] = 1  
print(matrix)


# In[4]:


#4.normalize a 5x5 random matrix

import numpy as np
matrix = np.random.rand(5, 5)
mean = np.mean(matrix)
std_dev = np.std(matrix)
normalized_matrix = (matrix - mean) / std_dev
print("Original Matrix:")
print(matrix)
print("\nNormalized Matrix:")
print(normalized_matrix)


# In[5]:


#5.how can you find common values between two arrays

import numpy as np

array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([3, 4, 5, 6, 7])
common_values = np.intersect1d(array1, array2)
print(common_values)


# In[6]:


#6.how to get the dates of yesterday,today and tomorrow

from datetime import datetime, timedelta
today = datetime.now().date()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
today_str = today.strftime("%Y-%m-%d")
yesterday_str = yesterday.strftime("%Y-%m-%d")
tomorrow_str = tomorrow.strftime("%Y-%m-%d")
print("Yesterday:", yesterday_str)
print("Today:", today_str)
print("Tomorrow:", tomorrow_str)



# In[7]:


#7.consider two random array A and B,check if they are equal.

import numpy as np
A = np.random.rand(5, 5)
B = np.random.rand(5, 5)

are_equal = np.array_equal(A, B)

if are_equal:
    print("Arrays A and B are equal.")
else:
    print("Arrays A and B are not equal.")


# In[8]:


#8.create a random vector of size 10 and replace the maximum value with 0

import numpy as np

# Create a random vector of size 10
vector = np.random.rand(10)

# Find the index of the maximum value in the vector
max_index = np.argmax(vector)

# Replace the maximum value with 0
vector[max_index] = 0


print("Original Vector:")
print(vector)


# In[9]:


#9.how to print all the values of an array

my_array = [1, 2, 3, 4, 5]

print(my_array)


# In[10]:


#10.subtract the mean of each row of matrix

import numpy as np

matrix = np.random.rand(3, 4)

row_means = np.mean(matrix, axis=1, keepdims=True)

matrix_minus_means = matrix - row_means

print("Original Matrix:")
print(matrix)
print("\nMatrix with Row Means Subtracted:")
print(matrix_minus_means)


# In[11]:


#11.consider a given vector,how to add 1 to each element indexed by a second vector 
import numpy as np

vect = np.array([1, 2, 3, 4, 5])
index_vector = np.array([1, 3, 4])  

vect[index_vector] += 1

print("Modified Vector:")
print(vect)


# In[12]:


#12.how to get the diagonal of a dot product

import numpy as np

matrix1 = np.random.rand(3, 3)
matrix2 = np.random.rand(3, 3)

pro = np.dot(matrix1, matrix2)
diagonal = np.diag(pro)
print("Diagonal of Dot Product:")
print(diagonal)


# In[13]:


#13.how to find most frequent value in an array

import numpy as np
my_array = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
unique_values, counts = np.unique(my_array, return_counts=True)
most_common_index = np.argmax(counts)
most_common_value = unique_values[most_common_index]
frequency = counts[most_common_index]
print(f"The most frequent value is {most_common_value} with a frequency of {frequency}.")


# In[14]:


#14.how to get the n largest values of an array

import numpy as np
my_array = [4, 8, 1, 6, 10, 7, 5, 3]
n = 3
sorted_indices = np.argsort(my_array)
n_largest_values = my_array[sorted_indices[-n:]]
n_largest_indices = sorted_indices[-n:]
print(f"The {n} largest values are: {n_largest_values}")
print(f"The indices of the {n} largest values are: {n_largest_indices}")


# In[15]:


#15.how to create a record array from a regular array

import numpy as np

regular_array = [(1, 'Anand', 25),
                (2, 'pawan', 50),
                (3, 'shrini', 45)]

dtype = [('ID', int), ('Name', 'U10'), ('Age', int)]
record_array = np.array(regular_array, dtype=dtype)
print("Record Array:")
print(record_array)
print("\nAccessing Elements by Field Name:")
print("ID:", record_array['ID'])
print("Name:", record_array['Name'])
print("Age:", record_array['Age'])


# In[16]:


#16.how to swap two rows of an array

import numpy as np

array = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

row1_index = 0
row2_index = 2  
array[[row1_index, row2_index]] = array[[row2_index, row1_index]]
print("Array with Rows Swapped:")
print(array)


# In[17]:


#17.write a python code to reshape to the next dimension of numpy array
import numpy as np
array = np.array([[23, 34, 121],
                  [23, 22, 67],
                  [686, 434, 123]])
reshaped_array = array.reshape(-1, 1)
print("Reshaped Array:")
print(reshaped_array)


# In[ ]:





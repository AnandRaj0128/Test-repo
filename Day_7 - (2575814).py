#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


#1.Write a pyhton program to  find a tagret using lenear search
# Initialize the list to store the input elements
input_list = []

# Initialize found to False
found = False

# Input elements into the list
num_elements = int(input("Enter the number of elements in the list: "))
for i in range(num_elements):
    element = input("Enter element {}: ".format(i + 1))
    input_list.append(element)

# Enter the item to be searched 
match_item = input("Enter the item to be searched: ")

# Linear search
for index, value in enumerate(input_list):
    if value == match_item:
        found = True
        position = index + 1  # Adding 1 to make it 1-based index
        break

# Check 
if found:
    print(f"{match_item} found at position {position}.")
else:
    print(f"{match_item} is not found in the list.")


# In[2]:


#2.Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  

        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            left = mid + 1  # Target is on the right side
        else:
            right = mid - 1  # Target is on the left side

    return -1  

# Get the number of inputs from the user
num_inputs = int(input("Enter the number of elements: "))

# Store the inputs individually in a list
input_list = []
for i in range(num_inputs):
    element = int(input("Enter element {} (in sorted order): ".format(i + 1)))
    input_list.append(element)

# Get the target value from the user
target = int(input("Enter the target value to search for: "))

# Call the binary_search function
result = binary_search(input_list, target)

# Check if the target value was found
if result != -1:
    print(f"{target} found at position {result + 1}.")  # Adding 1 to make it 1-based index
else:
    print(f"{target} is not found in the list.")


# In[3]:


#3.Selection sort

def selection_sort(arr):
    sorted_list = []  # Initialize the sorted list as empty

    while arr:  # Continue until the unsorted list is not empty
        min_index = 0  # Assume the first element is the minimum
        for i in range(1, len(arr)):
            if arr[i] < arr[min_index]:
                min_index = i  # Update the minimum index

        # Add the minimum element to the sorted list and remove it from the unsorted list
        sorted_list.append(arr.pop(min_index))

    return sorted_list

# Input the unsorted list
input_list = input("Enter a list of elements separated by spaces: ").split()
input_list = [int(x) for x in input_list]  # Convert input elements to integers

# Call the selection_sort function
sorted_list = selection_sort(input_list)

# Display the sorted list
print("Sorted list:", sorted_list)


# In[4]:


#4.Insertion sort
# Function to perform insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

# Input the unsorted list
input_list = input("Enter a list of elements separated by spaces: ").split()
input_list = [int(x) for x in input_list]  # Convert input elements to integers

# Call the insertion_sort function
insertion_sort(input_list)

# Display the sorted list
print("Sorted list:", input_list)


# In[5]:


#5.Merge Sort

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide the input list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort the two halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Combine the sorted halves into a single sorted list
    result = merge(left_half, right_half)
    return result

def merge(left, right):
    merged = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    # Add remaining elements from both lists, if any
    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])

    return merged

# Ex
if __name__ == "__main__":
    input_list = [12, 11, 13, 5, 6, 7]
    sorted_list = merge_sort(input_list)
    print("Sorted list:", sorted_list)


# In[ ]:





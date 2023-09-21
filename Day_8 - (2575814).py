#!/usr/bin/env python
# coding: utf-8

# In[1]:


#6.Singly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    
    def find_smallest(self):
        if not self.head:
            return None

        current = self.head
        smallest = current.data

        while current:
            if current.data < smallest:
                smallest = current.data
            current = current.next

        return smallest

    
    def insert_if_not_duplicate(self, data):
        if not self.head:
            self.insert(data)
            return

        current = self.head

        while current:
            if current.data == data:
                return
            if not current.next:
                break
            current = current.next

        current.next = Node(data)

    
    def display_reverse(self):
        stack = []
        current = self.head

        while current:
            stack.append(current.data)
            current = current.next

        while stack:
            print(stack.pop(), end=" -> ")
        print("None")

# Create an instance of LinkedList
linked_list = LinkedList()

# Create a list (insert elements)
elements = [5, 2, 8, 2, 1, 3, 5]
for element in elements:
    linked_list.insert(element)

# Find the smallest element
smallest = linked_list.find_smallest()
print("Smallest element:", smallest)

# Insert an element if it's not a duplicate
linked_list.insert_if_not_duplicate(4)
linked_list.insert_if_not_duplicate(2)  # This won't be inserted as a duplicate

# Display elements in reverse order
print("Elements in reverse order:")
linked_list.display_reverse()



# In[2]:


#7.Stack ADT

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None  # Stack is empty

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        if not self.is_empty():
            for item in reversed(self.items):
                print(item)
        else:
            print("Stack is empty")



stack = Stack()

while True:
    print("\nStack Operations:")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        item = input("Enter an item to push: ")
        stack.push(item)
        print(f"{item} pushed onto the stack.")

    elif choice == '2':
        popped_item = stack.pop()
        if popped_item is not None:
            print(f"Popped item: {popped_item}")
        else:
            print("Stack is empty.")

    elif choice == '3':
        print("Stack contents:")
        stack.display()

    elif choice == '4':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")


# In[4]:


#8.stack (infix to postfix)

def has_higher_precedence(op1, op2):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    return precedence[op1] >= precedence[op2]


def infix_to_postfix(expression):
    stack = []
    postfix = []
    
    for char in expression:
        if char.isalnum():
            postfix.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()  # Pop the opening parenthesis
        else:  # char is an operator
            while stack and stack[-1] != '(' and has_higher_precedence(char, stack[-1]):
                postfix.append(stack.pop())
            stack.append(char)
    
    while stack:
        postfix.append(stack.pop())
    
    return ''.join(postfix)

infix_expression_a = "a A/B C D'E-FG"
infix_expression_b = "(B^2-4*A*C)^(1/2)*(100)"

postfix_a = infix_to_postfix(infix_expression_a)
postfix_b = infix_to_postfix(infix_expression_b)

print("Infix Expression A:", infix_expression_a)
print("Postfix Expression A:", postfix_a)

print("\nInfix Expression B:", infix_expression_b)
print("Postfix Expression B:", postfix_b)


# In[ ]:





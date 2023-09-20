#!/usr/bin/env python
# coding: utf-8

# # OBJECT ORIIENTED PROGRAMMING IN PYTHON

# In[2]:


#1.class shape,quiz...

import math

# Define the base class "Shape"
class Shape:
    def calculate_area(self):
        pass
    
    def calculate_perimeter(self):
        pass

# Derived class "Circle"
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius**2
    
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

# Derived class "Rectangle"
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

# Demonstrate usage of the Shape, Circle, and Rectangle classes
circle = Circle(5)
print("Circle Area:", circle.calculate_area())
print("Circle Perimeter:", circle.calculate_perimeter())

rectangle = Rectangle(4, 6)
print("Rectangle Area:", rectangle.calculate_area())
print("Rectangle Perimeter:", rectangle.calculate_perimeter())

####################################################################################################

class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option

class Quiz:
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions

    def take_quiz(self):
        score = 0
        for question in self.questions:
            print(question.text)
            for i, option in enumerate(question.options):
                print(f"{i + 1}. {option}")
            
            user_answer = int(input("Your answer: ")) - 1  # Adjust for 0-based index
            if user_answer == question.correct_option:
                print("Correct!\n")
                score += 1
            else:
                print("Incorrect.\n")
        
        print(f"Quiz completed! Your score: {score}/{len(self.questions)}")

# Ex
question1 = Question("What is the capital of France?", ["London", "Berlin", "Paris"], 2)
question2 = Question("Which planet is known as the Red Planet?", ["Earth", "Mars", "Venus"], 1)

quiz = Quiz("General Knowledge Quiz", [question1, question2])
quiz.take_quiz()
 
    
#####################################################################################################

class User:
    def __init__(self, username):
        self.username = username
        self.quiz_history = {}  # Dictionary to store quiz history and scores

    def take_quiz(self, quiz, score):
        self.quiz_history[quiz.name] = score

# Create users and track their progress
user1 = User("User1")
user2 = User("User2")

quiz1 = Quiz("General Knowledge Quiz", [question1, question2])
quiz2 = Quiz("Science Quiz", [question1])

user1.take_quiz(quiz1, 1)
user1.take_quiz(quiz2, 0)

user2.take_quiz(quiz1, 2)

# To retrieve a user's progress and scores:
print(user1.username, "Quiz History:", user1.quiz_history)
print(user2.username, "Quiz History:", user2.quiz_history)


# In[5]:


#2.
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age  

    def calculate_voting_eligibility(self):
        if self.__age >= 18:
            return f"{self.__name} is eligible to vote."
        else:
            return f"{self.__name} is not eligible to vote."

    
    def get_age(self):
        return self.__age

    
    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Age cannot be negative.")


person = Person("pavan", 25)


print(f"{person._Person__name}'s age is {person.get_age()}")

# Calculate voting eligibility
print(person.calculate_voting_eligibility())


# In[7]:


#3.Bank Account

class BankAccount:
    def __init__(self, account_number, account_holder_name, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder_name, balance, interest_rate):
        super().__init__(account_number, account_holder_name, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        print(f"Interest calculated and added: ${interest}. New balance: ${self.balance}")

class CheckingAccount(BankAccount):
    def __init__(self, account_number, account_holder_name, balance, overdraft_limit):
        super().__init__(account_number, account_holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0 and amount <= (self.balance + self.overdraft_limit):
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")


# Create a Savings Account
savings_account = SavingsAccount("SA123", "Alice", 1000, 5)
savings_account.calculate_interest()

# Create a Checking Account
checking_account = CheckingAccount("CA456", "Bob", 500, 200)
checking_account.withdraw(600)  

####################################################################################################



# In[8]:


#4.Employee management

class Employee:
    def __init__(self, name, employee_id):
        self.__name = name
        self.__employee_id = employee_id
        self.__salary = 0

    # Getter and setter methods for name
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    # Getter and setter methods for employee ID
    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    # Getter method for salary (no setter as salary will be calculated differently for subclasses)
    def get_salary(self):
        return self.__salary

class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, annual_salary):
        super().__init__(name, employee_id)
        self.__annual_salary = annual_salary

    # Override the salary calculation method
    def calculate_salary(self):
        self._Employee__salary = self.__annual_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hours_worked, hourly_rate):
        super().__init__(name, employee_id)
        self.__hours_worked = hours_worked
        self.__hourly_rate = hourly_rate

    # Override the salary calculation method
    def calculate_salary(self):
        self._Employee__salary = self.__hours_worked * self.__hourly_rate


# Full-Time emp
full_time_employee = FullTimeEmployee("John Doe", "FT123", 60000)
full_time_employee.calculate_salary()

#part time
part_time_employee = PartTimeEmployee("Jane Smith", "PT456", 20, 15)
part_time_employee.calculate_salary()

# Display emp info
print(f"{full_time_employee.get_name()} ({full_time_employee.get_employee_id()}): Salary ${full_time_employee.get_salary()} per year")
print(f"{part_time_employee.get_name()} ({part_time_employee.get_employee_id()}): Salary ${part_time_employee.get_salary()} per month")


# In[9]:


#5.Library management

from datetime import datetime, timedelta

# Base class for books
class Book:
    def __init__(self, title, author, publication_date, ISBN, available=True):
        self.__title = title
        self.__author = author
        self.__publication_date = publication_date
        self.__ISBN = ISBN
        self.__available = available

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_publication_date(self):
        return self.__publication_date

    def get_ISBN(self):
        return self.__ISBN

    def is_available(self):
        return self.__available

    def set_available(self, available):
        self.__available = available

# Subclasses for different types of books
class FictionBook(Book):
    def __init__(self, title, author, publication_date, ISBN, available=True, genre=""):
        super().__init__(title, author, publication_date, ISBN, available)
        self.__genre = genre

    def get_genre(self):
        return self.__genre

class NonFictionBook(Book):
    def __init__(self, title, author, publication_date, ISBN, available=True, topic=""):
        super().__init__(title, author, publication_date, ISBN, available)
        self.__topic = topic

    def get_topic(self):
        return self.__topic

# Patron class
class Patron:
    def __init__(self, name, patron_id):
        self.__name = name
        self.__patron_id = patron_id

    def get_name(self):
        return self.__name

    def get_patron_id(self):
        return self.__patron_id

# Transaction class
class Transaction:
    def __init__(self, book, patron, transaction_type):
        self.__book = book
        self.__patron = patron
        self.__transaction_type = transaction_type
        self.__due_date = datetime.now() + timedelta(days=14)

    def get_book(self):
        return self.__book

    def get_patron(self):
        return self.__patron

    def get_transaction_type(self):
        return self.__transaction_type

    def get_due_date(self):
        return self.__due_date

# Library class for managing transactions, overdue books, etc.
class Library:
    def __init__(self):
        self.__transactions = []

    def check_out_book(self, book, patron):
        if book.is_available():
            book.set_available(False)
            transaction = Transaction(book, patron, "Check Out")
            self.__transactions.append(transaction)
            return transaction
        else:
            return "Book is not available for check out."

    def return_book(self, transaction):
        if transaction.get_transaction_type() == "Check Out":
            transaction.get_book().set_available(True)
            self.__transactions.remove(transaction)
            return "Book successfully returned."
        else:
            return "Invalid return transaction."

    def get_overdue_books(self):
        today = datetime.now()
        overdue_books = []
        for transaction in self.__transactions:
            if transaction.get_due_date() < today:
                overdue_books.append(transaction)
        return overdue_books


# Create books and patrons
fiction_book = FictionBook("The Great Gatsby", "F. Scott Fitzgerald", "1925", "978-0743273565", genre="Classic")
non_fiction_book = NonFictionBook("Sapiens: A Brief History of Humankind", "Yuval Noah Harari", "2014", "978-0062316097", topic="History")
patron1 = Patron("Alice", "P001")
patron2 = Patron("Bob", "P002")

# Create a library and perform transactions
library = Library()
transaction1 = library.check_out_book(fiction_book, patron1)
transaction2 = library.check_out_book(non_fiction_book, patron2)
transaction3 = library.check_out_book(non_fiction_book, patron1)
print(transaction1.get_transaction_type())  # Output: "Check Out"
print(transaction2.get_transaction_type())  # Output: "Check Out"
print(transaction3)  # Output: "Book is not available for check out."

# Return a book
print(library.return_book(transaction1))  # Output: "Book successfully returned"

# Get overdue books
overdue_books = library.get_overdue_books()
for transaction in overdue_books:
    print(f"Overdue Book: {transaction.get_book().get_title()} - Due Date: {transaction.get_due_date()}")


# In[10]:


#6.Shopping Cart

from datetime import datetime, timedelta

# Base class for books
class Book:
    def __init__(self, title, author, publication_date, ISBN, available=True):
        self.__title = title
        self.__author = author
        self.__publication_date = publication_date
        self.__ISBN = ISBN
        self.__available = available

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_publication_date(self):
        return self.__publication_date

    def get_ISBN(self):
        return self.__ISBN

    def is_available(self):
        return self.__available

    def set_available(self, available):
        self.__available = available

# Subclasses for different types of books
class FictionBook(Book):
    def __init__(self, title, author, publication_date, ISBN, available=True, genre=""):
        super().__init__(title, author, publication_date, ISBN, available)
        self.__genre = genre

    def get_genre(self):
        return self.__genre

class NonFictionBook(Book):
    def __init__(self, title, author, publication_date, ISBN, available=True, topic=""):
        super().__init__(title, author, publication_date, ISBN, available)
        self.__topic = topic

    def get_topic(self):
        return self.__topic

# Patron class
class Patron:
    def __init__(self, name, patron_id):
        self.__name = name
        self.__patron_id = patron_id

    def get_name(self):
        return self.__name

    def get_patron_id(self):
        return self.__patron_id

# Transaction class
class Transaction:
    def __init__(self, book, patron, transaction_type):
        self.__book = book
        self.__patron = patron
        self.__transaction_type = transaction_type
        self.__due_date = datetime.now() + timedelta(days=14)

    def get_book(self):
        return self.__book

    def get_patron(self):
        return self.__patron

    def get_transaction_type(self):
        return self.__transaction_type

    def get_due_date(self):
        return self.__due_date

# Library class for managing transactions, overdue books, etc.
class Library:
    def __init__(self):
        self.__transactions = []

    def check_out_book(self, book, patron):
        if book.is_available():
            book.set_available(False)
            transaction = Transaction(book, patron, "Check Out")
            self.__transactions.append(transaction)
            return transaction
        else:
            return "Book is not available for check out."

    def return_book(self, transaction):
        if transaction.get_transaction_type() == "Check Out":
            transaction.get_book().set_available(True)
            self.__transactions.remove(transaction)
            return "Book successfully returned."
        else:
            return "Invalid return transaction."

    def get_overdue_books(self):
        today = datetime.now()
        overdue_books = []
        for transaction in self.__transactions:
            if transaction.get_due_date() < today:
                overdue_books.append(transaction)
        return overdue_books


# Create books and patrons
fiction_book = FictionBook("The Great Gatsby", "F. Scott Fitzgerald", "1925", "978-0743273565", genre="Classic")
non_fiction_book = NonFictionBook("Sapiens: A Brief History of Humankind", "Yuval Noah Harari", "2014", "978-0062316097", topic="History")
patron1 = Patron("Alice", "P001")
patron2 = Patron("Bob", "P002")

# Create a library and perform transactions
library = Library()
transaction1 = library.check_out_book(fiction_book, patron1)
transaction2 = library.check_out_book(non_fiction_book, patron2)
transaction3 = library.check_out_book(non_fiction_book, patron1)
print(transaction1.get_transaction_type())  # Output: "Check Out"
print(transaction2.get_transaction_type())  # Output: "Check Out"
print(transaction3)  # Output: "Book is not available for check out."

# Return a book
print(library.return_book(transaction1))  # Output: "Book successfully returned"

# Get overdue books
overdue_books = library.get_overdue_books()
for transaction in overdue_books:
    print(f"Overdue Book: {transaction.get_book().get_title()} - Due Date: {transaction.get_due_date()}")


# In[ ]:





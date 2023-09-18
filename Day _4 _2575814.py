#!/usr/bin/env python
# coding: utf-8

# # EXCEPTIONS AND COMMAND LINE ARGUMENTS

# In[1]:


#1.calculate percentage and grade
try:
    # Initialize variables for marks in each subject
    physics = float(input("Enter Physics marks: "))
    chemistry = float(input("Enter Chemistry marks: "))
    biology = float(input("Enter Biology marks: "))
    mathematics = float(input("Enter Mathematics marks: "))
    computer = float(input("Enter Computer marks: "))

    # Calculate the total marks
    total_marks = physics + chemistry + biology + mathematics + computer

    # Calculate the percentage
    percentage = (total_marks / 500) * 100

    # Determine the grade based on percentage
    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    elif percentage >= 60:
        grade = "D"
    elif percentage >= 40:
        grade = "E"
    else:
        grade = "F"

    # Print the percentage and grade
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

except ValueError:
    print("Invalid input. Please enter valid numerical marks for each subject.")
except Exception as e:
    print(f"An error occurred: {str(e)}")


# In[2]:


#2.calculate electricity bill

try:
    # Input the electricity unit charges
    units = float(input("Enter the electricity unit charges: "))

    # Initialize variables for bill calculation
    total_bill = 0.0
    surcharge = 0.2  # 20% surcharge

    # Calculate the bill based on the given conditions
    if units <= 50:
        total_bill = units * 0.50
    elif units <= 150:
        total_bill = (50 * 0.50) + ((units - 50) * 0.75)
    elif units <= 250:
        total_bill = (50 * 0.50) + (100 * 0.75) + ((units - 150) * 1.20)
    else:
        total_bill = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((units - 250) * 1.50)

    # Add the surcharge
    total_bill += total_bill * surcharge

    # Print the total electricity bill
    print(f"Total electricity bill: Rs. {total_bill:.2f}")

except ValueError:
    print("Invalid input. Please enter a valid number of electricity units.")
except Exception as e:
    print(f"An error occurred: {str(e)}")


# In[4]:


#3.input week number to print week day

try:
    # Input the week number as an integer
    week_number = int(input("Enter the week number (1-7): "))

    # Define a list of weekdays
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Check if the input is within the valid range
    if 1 <= week_number <= 7:
        # Print the corresponding weekday
        print(f"Weekday {week_number} is {weekdays[week_number - 1]}")
    else:
        print("Invalid input. Week number must be between 1 and 7.")

except ValueError:
    print("Invalid input. Please enter a valid week number as an integer.")
except Exception as e:
    print(f"An error occurred: {str(e)}")


# In[6]:


#4.word count using command line arguments


import sys

def word_count(filename):
    try:
        with open(Untitled5.py, 'r') as file:
            text = file.read()
            words = text.split()
            word_count = {}

            for word in words:
                word = word.lower()  # Convert to lowercase for case-insensitive counting
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

            return word_count

    except FileNotFoundError:
        print(f"File '{Untitled5.py}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

if _name_ == "_main_":
    if len(sys.argv) != 2:
        print("Usage: python wordcount.py <filename>")
    else:
        filename = sys.argv[1]
        result = word_count(Untitled5.py)
        if result:
            for word, count in result.items():
                print(f"{word}: {count}")


# In[7]:


#5.find most frequent words in a text file

import string

def get_most_frequent_words(filename, num_words=10):
    try:
        with open(sorce.txt, 'r') as file:
            text = file.read().lower()  # Read the file and convert text to lowercase
            words = text.split()

            # Remove punctuation from words
            words = [word.strip(string.punctuation) for word in words]

            word_count = {}

            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

            # Sort the words by frequency
            sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

            # Get the most frequent words
            most_frequent_words = sorted_words[:num_words]

            return most_frequent_words

    except FileNotFoundError:
        print(f"File '{sorce.txt}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

if _name_ == "_main_":
    filename = "sorce.txt"  # Replace with your file path
    num_words = 10  # Change this value to get more or fewer frequent words
import sys
import os

def process_text_file(input_file_path, output_file_path):
    try:
        # Check if the input file exists
        if not os.path.isfile(input_file_path):
            raise FileNotFoundError(f"The input file '{input_file_path}' does not exist.")
        
        # Open the input file for reading
        with open(input_file_path, 'r') as input_file:
            # Read the content and process it as needed
            content = input_file.read()

        # Process the content (you can replace this with your processing logic)
        processed_content = content.upper()

        # Open the output file for writing
        with open(output_file_path, 'w') as output_file:
            # Write the processed content to the output file
            output_file.write(processed_content)
        
        print(f"File '{input_file_path}' processed and saved to '{output_file_path}' successfully.")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if _name_ == "_main_":
    if len(sys.argv) != 3:
        print("Usage: python your_script.py <input_file_path> <output_file_path>")
    else:
        input_file_path = sys.argv[1]
        output_file_path = sys.argv[2]
        process_text_file(input_file_path, output_file_path)
    result = get_most_frequent_words(filename, num_words)
    if result:
        print(f"Top {num_words} most frequent words in '{sorce.txt}':")
        for word, count in result:
            print(f"{word}: {count}")


# In[ ]:


#6.file processing with command line arguments


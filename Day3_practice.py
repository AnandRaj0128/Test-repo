#!/usr/bin/env python
# coding: utf-8

# # FILE HANDLING

# In[5]:


#1. python foction that a copies a file reading and writing upto 50 characters at a time
def copy_file"D:\New folder\sorce.txt.txt", destination_path):
    try:
        with open(source, 'rb') as source_file, open(destination_path, 'wb') as destination_file:
            while True:
                chunk = source_file.read(50)
                if not chunk:
                    break
                destination_file.write(chunk)
        print(f"File '{source_path}' copied to '{destination_path}' successfully.")
    except FileNotFoundError:
        print(f"File '{source_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage:
source_file_path = 'sorce.txt'  
destination_file_path = 'destination.txt'  
copy_file(source_file_path, destination_file_path)


# In[ ]:


#2print all the numbers in a file and print number of blank spaces. 
number_count = 0
blank_space_count = 0

# Specify the file path
file_path = 'hi.txt'  # Replace with the path to your file

try:
    with open(file_path, 'r') as file:
        for line in file:
            # Iterate through characters in the line
            for char in line:
                # Check if the character is a digit (number)
                if char.isdigit():
                    number_count += 1
                
                # Check if the character is a blank space
                if char.isspace() and char != '\n':
                    blank_space_count += 1

except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")

# Print the counts
print(f"Total numbers found: {number_count}")
print(f"Total blank spaces found: {blank_space_count}")


# In[ ]:


#3. write  a function called sed that takes as arguments a string.a replacement string and two silenames;it should read the fist file
#and write contents into second file.
def sed(pattern, replacement, source_filename, destination_filename):
    try:
        # Open the source file for reading
        with open(source_filename, 'r') as source_file:
            # Read the entire content of the source file
            content = source_file.read()

        # Replace the pattern with the replacement string
        modified_content = content.replace(pattern, replacement)

        # Open the destination file for writing
        with open(destination_filename, 'w') as destination_file:
            # Write the modified content to the destination file
            destination_file.write(modified_content)

        print(f"File '{source_filename}' processed and saved to '{destination_filename}' successfully.")
    except FileNotFoundError:
        print(f"Error: File '{source_filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage:
pattern_to_replace = 'old_pattern'
replacement_string = 'new_pattern'
source_file_path = 'source.txt'  # Replace with your source file path
destination_file_path = 'destination.txt'  # Replace with your destination file path

sed(pattern_to_replace, replacement_string, source_file_path, destination_file_path)


# In[ ]:


#4.Log file analysys.
def analyze_log_file(log_file_path):
    unique_users = set()
    action_counts = {}

    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            # Assuming each line is in the format: timestamp,user_id,action
            timestamp, user_id, action = line.strip().split(',')

            # Count unique users
            unique_users.add(user_id)

            # Count action occurrences
            action_counts[action] = action_counts.get(action, 0) + 1

    return len(unique_users), max(action_counts, key=action_counts.get)

# Example usage:
log_file_path = 'your_log_file.log'
unique_users_count, most_common_action = analyze_log_file(log_file_path)

print(f"Number of unique users: {unique_users_count}")
print(f"Most common action: {most_common_action}")





# In[ ]:


#5.text file search and replace
#a
def search_and_replace_in_file(input_file_path, output_file_path, search_text, replace_text):
    try:
        with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
            for line in input_file:
                # Replace search_text with replace_text in each line
                modified_line = line.replace(search_text, replace_text)
                output_file.write(modified_line)
        
        print(f"Replacements completed. New content saved to {output_file_path}.")
    except FileNotFoundError:
        print(f"Error: File '{input_file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage:
input_file_path = 'input.txt'
output_file_path = 'output.txt'
search_text = 'old_text'
replace_text = 'new_text'

search_and_replace_in_file(input_file_path, output_file_path, search_text, replace_text)


# In[ ]:


#5b.
def multiple_replacements_in_file(input_file_path, output_file_path, replacements):
    try:
        with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
            for line in input_file:
                for search_text, replace_text in replacements.items():
                    line = line.replace(search_text, replace_text)
                output_file.write(line)

        print(f"Multiple replacements completed. New content saved to {output_file_path}.")
    except FileNotFoundError:
        print(f"Error: File '{input_file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage:
input_file_path = 'input.txt'
output_file_path = 'output.txt'
replacements = {
    'old_text_1': 'new_text_1',
    'old_text_2': 'new_text_2',
    # Add more replacement pairs as needed
}

multiple_replacements_in_file(input_file_path, output_file_path, replacements)


# In[ ]:


#6.concatenation of multiple text files into a single output file
def concatenate_text_files(input_files, output_file):
    try:
        with open(output_file, 'w') as output:
            for input_file in input_files:
                with open(input_file, 'r') as file:
                    output.write(file.read())
                # Add a separator between file contents, such as a newline
                output.write('\n')

        print(f"Concatenation completed. Merged content saved to {output_file}.")
    except FileNotFoundError as e:
        print(f"Error: {e.filename} not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    input_files = []
    while True:
        file_path = input("Enter the path of an input text file (or 'done' to finish): ")
        if file_path.lower() == 'done':
            break
        input_files.append(file_path)

    if not input_files:
        print("No input files specified. Exiting.")
        return

    output_file = input("Enter the path of the output text file: ")

    concatenate_text_files(input_files, output_file)

if __name__ == "__main__":
    main()


# In[ ]:


#7.you are given a filenamed inpit.text containing a list of words 
def process_words(input_file_path, output_file_path):
    try:
        # Open the input file for reading
        with open(input_file_path, 'r') as input_file:
            words = input_file.read().split()
        
        # Create a dictionary to store word lengths
        word_lengths = {word: len(word) for word in words}

        # Open the output file for writing
        with open(output_file_path, 'w') as output_file:
            # Write the word-length dictionary to the output file
            for word, length in word_lengths.items():
                output_file.write(f'{word}: {length}\n')
        
        print(f"Word-length dictionary written to '{output_file_path}' successfully.")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if _name_ == "_main_":
    input_file_path = "input.txt"  # Replace with the actual input file path
    output_file_path = "output.txt"  # Replace with the desired output file path
    process_words(input_file_path, output_file_path)


# In[ ]:


#8.student gradebook system for school
def process_words(input_file_path, output_file_path):
    try:
        # Open the input file for reading
        with open(input_file_path, 'r') as input_file:
            words = input_file.read().split()
        
        # Create a dictionary to store word lengths
        word_lengths = {word: len(word) for word in words}

        # Open the output file for writing
        with open(output_file_path, 'w') as output_file:
            # Write the word-length dictionary to the output file
            for word, length in word_lengths.items():
                output_file.write(f'{word}: {length}\n')
        
        print(f"Word-length dictionary written to '{output_file_path}' successfully.")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if _name_ == "_main_":
    input_file_path = "input.txt"  # Replace with the actual input file path
    output_file_path = "output.txt"  # Replace with the desired output file path
    process_words(input_file_path, output_file_path)


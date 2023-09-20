#!/usr/bin/env python
# coding: utf-8

# # MODULES AND VIRTUAL ENVIRONMENTS

# In[5]:


#1.Module Import and Management
try:
    
    import math
    import raj_module as cm 
    print("Using functions and variables from the math module:")
    print("Square root of 16:", math.sqrt(16))
    print("Value of pi:", math.pi)
    print()

    print("Using the custom module:")
    print(cm.custom_function())
    print("Custom variable:", cm.custom_variable)

except ModuleNotFoundError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")







# In[6]:


#2.virtual environment management
mport sys
import subprocess

def create_virtual_environment(env_name):
    try:
        subprocess.run([sys.executable, '-m', 'venv', env_name])
        print(f"Virtual environment '{env_name}' created successfully.")
    except Exception as e:
        print(f"Error creating the virtual environment: {e}")

def activate_virtual_environment(env_name):
    try:
        activate_script = f"{env_name}/Scripts/activate" if sys.platform == 'win32' else f"{env_name}/bin/activate"
        subprocess.run([activate_script], shell=True)
        print(f"Activated virtual environment '{env_name}'.")
    except Exception as e:
        print(f"Error activating the virtual environment: {e}")

def deactivate_virtual_environment():
    try:
        subprocess.run(['deactivate'], shell=True)
        print("Deactivated the virtual environment.")
    except Exception as e:
        print(f"Error deactivating the virtual environment: {e}")

def install_package(env_name, package_name):
    try:
        subprocess.run([f'{env_name}/bin/pip', 'install', package_name])
        print(f"Package '{package_name}' installed successfully in '{env_name}'.")
    except Exception as e:
        print(f"Error installing the package: {e}")

def upgrade_package(env_name, package_name):
    try:
        subprocess.run([f'{env_name}/bin/pip', 'install', '--upgrade', package_name])
        print(f"Package '{package_name}' upgraded successfully in '{env_name}'.")
    except Exception as e:
        print(f"Error upgrading the package: {e}")

def uninstall_package(env_name, package_name):
    try:
        subprocess.run([f'{env_name}/bin/pip', 'uninstall', '-y', package_name])
        print(f"Package '{package_name}' uninstalled successfully from '{env_name}'.")
    except Exception as e:
        print(f"Error uninstalling the package: {e}")

def list_installed_packages(env_name):
    try:
        result = subprocess.run([f'{env_name}/bin/pip', 'list'], stdout=subprocess.PIPE, text=True)
        print(f"Installed packages in '{env_name}':\n{result.stdout}")
    except Exception as e:
        print(f"Error listing installed packages: {e}")

if __name__ == "__main__":
    venv_name = "my_virtual_env"  # Change to your preferred virtual environment name
    
    create_virtual_environment(venv_name)
    activate_virtual_environment(venv_name)
    
    install_package(venv_name, 'requests')
    upgrade_package(venv_name, 'requests')
    
    list_installed_packages(venv_name)
    
    uninstall_package(venv_name, 'requests')
    
    deactivate_virtual_environment()
This program does the following:

Creates a virtual environment named my_virtual_env.
Activates the virtual e


# In[7]:


#3.Module dependency resolution
import subprocess

def install_dependencies():
    try:
        with open('requirements.txt', 'r') as requirements_file:
            for line in requirements_file:
                
                package, version = line.strip().split('==')
                
                
                subprocess.run(['pip', 'install', f'{package}=={version}'])
                
        print("All dependencies installed successfully.")
    except FileNotFoundError:
        print("Error: 'requirements.txt' file not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    install_dependencies()


# # DATABASE PROGRAMMING WITH MYSQL
# 

# In[ ]:


#1.implement inventory management in python with mySQL
import mysql.connector

db_connection = mysql.connector.connect(
    host="your_host",
    user="your_username",
    password="your_password",
    database="inventory"
)


cursor = db_connection.cursor()

# add a new product to the inventory
def add_product(product_name, quantity):
    try:
        cursor.execute("INSERT INTO inventory (product_name, quantity) VALUES (%s, %s)",
                       (product_name, quantity))
        db_connection.commit()
        print("Product added to inventory successfully.")
    except Exception as e:
        db_connection.rollback()
        print(f"Error: {e}")

# record a purchase
def record_purchase(product_id, quantity):
    try:
        cursor.execute("INSERT INTO purchases (product_id, purchase_date, quantity) VALUES (%s, NOW(), %s)",
                       (product_id, quantity))
        cursor.execute("UPDATE inventory SET quantity = quantity + %s WHERE id = %s",
                       (quantity, product_id))
        db_connection.commit()
        print("Purchase recorded successfully.")
    except Exception as e:
        db_connection.rollback()
        print(f"Error: {e}")


def record_sale(product_id, quantity):
    try:
        cursor.execute("INSERT INTO sales (product_id, sale_date, quantity) VALUES (%s, NOW(), %s)",
                       (product_id, quantity))
        cursor.execute("UPDATE inventory SET quantity = quantity - %s WHERE id = %s",
                       (quantity, product_id))
        db_connection.commit()
        print("Sale recorded successfully.")
    except Exception as e:
        db_connection.rollback()
        print(f"Error: {e}")

cursor.close()
db_connection.close()


# In[9]:


#2.Customer oder processing
import mysql.connector

# Connect to the MySQL database
db_connection = mysql.connector.connect(
    host="your_host",
    user="your_username",
    password="your_password",
    database="order_processing"
)


cursor = db_connection.cursor()

def place_order(customer_id, product_id, quantity):
    try:
        # Check product availability
        cursor.execute("SELECT available_quantity FROM products WHERE product_id = %s", (product_id,))
        available_quantity = cursor.fetchone()[0]
        if available_quantity >= quantity:
            # Insert order and order item
            cursor.execute("INSERT INTO orders (customer_id, order_date) VALUES (%s, NOW())", (customer_id,))
            order_id = cursor.lastrowid
            cursor.execute("INSERT INTO order_items (order_id, product_id, quantity) VALUES (%s, %s, %s)",
                           (order_id, product_id, quantity))
            
            # Update product quantity
            cursor.execute("UPDATE products SET available_quantity = available_quantity - %s WHERE product_id = %s",
                           (quantity, product_id))
            
            db_connection.commit()
            print("Order placed successfully.")
        else:
            print("Product is not available in sufficient quantity.")
    except Exception as e:
        db_connection.rollback()
        print(f"Error: {e}")

cursor.close()
db_connection.close()
################################
def generate_order_report(order_id):
    try:
        cursor.execute("""
            SELECT o.order_id, c.first_name, c.last_name, p.product_name, oi.quantity, p.unit_price
            FROM orders o
            JOIN customers c ON o.customer_id = c.customer_id
            JOIN order_items oi ON o.order_id = oi.order_id
            JOIN products p ON oi.product_id = p.product_id
            WHERE o.order_id = %s
        """, (order_id,))
        
        report = cursor.fetchall()
        if report:
            total_cost = sum(item[4] * item[5] for item in report)
            print(f"Order Report for Order ID {order_id}")
            print("-------------------------------")
            for item in report:
                print(f"Product: {item[3]}, Quantity: {item[4]}, Unit Price: ${item[5]:.2f}")
            print(f"Total Cost: ${total_cost:.2f}")
        else:
            print("Order not found.")
    except Exception as e:
        print(f"Error: {e}")



# In[11]:


#3.
   
import mysql.connector


db_config = {
   "host": "localhost",
   "port": 3306,
   "user": "your_username",
   "password": "your_password",
   "database": "your_database"
}

try:
   
   db_connection = mysql.connector.connect(**db_config)
   
   
   cursor = db_connection.cursor()
   
   
   cursor.execute("SELECT id, name, quantity FROM your_table")
   records = cursor.fetchall()
   
   
   total_quantity = sum(record[2] for record in records)
   
   
   for record in records:
       new_quantity = record[2] * 2
       cursor.execute("UPDATE your_table SET quantity = %s WHERE id = %s", (new_quantity, record[0]))
   
   
   db_connection.commit()
   
   
   cursor.close()
   db_connection.close()
   
   print("Database operations completed successfully.")
   
except mysql.connector.Error as err:
   print(f"Error: {err}")
   if db_connection.is_connected():
       cursor.close()
       db_connection.close()
       print("Database connection closed due to error.")


# In[ ]:


#4.employee management sysytem
import mysql.connector

# Define the database connection parameters
db_config = {
    "host": "your_host",
    "port": 3306,
    "user": "your_username",
    "password": "your_password",
    "database": "employee_management"
}

try:
    # Connect to the MySQL database
    db_connection = mysql.connector.connect(**db_config)
    
    # Create a cursor object to interact with the database
    cursor = db_connection.cursor()
    
    # Define the department name you want to retrieve employees for
    department_name = "HR"  # Replace with the desired department
    
    # Retrieve employees in the specified department
    cursor.execute("""
        SELECT e.first_name, e.last_name, e.salary
        FROM employees e
        JOIN departments d ON e.department_id = d.department_id
        WHERE d.department_name = %s
    """, (department_name,))
    
    employees = cursor.fetchall()
    
    # Print the list of employees
    if employees:
        print(f"Employees in the {department_name} department:")
        for employee in employees:
            print(f"{employee[0]} {employee[1]} - Salary: ${employee[2]:.2f}")
    else:
        print(f"No employees found in the {department_name} department.")
    
    # Close the cursor and database connection
    cursor.close()
    db_connection.close()
    
except mysql.connector.Error as err:
    print(f"Error: {err}")
    if db_connection.is_connected():
        cursor.close()
        db_connection.close()
        print("Database connection closed due to error.")

######################################################################

def update_employee_salary(employee_id, new_salary):
    try:
        cursor.execute("UPDATE employees SET salary = %s WHERE employee_id = %s", (new_salary, employee_id))
        db_connection.commit()
        print("Employee's salary updated successfully.")
    except Exception as e:
        db_connection.rollback()
        print(f"Error: {e}")



# In[ ]:





# In[ ]:





# In[ ]:





# Python

Python Basics 🐍

A beginner-friendly Python repository covering the fundamentals of Python programming.

📚 Topics Covered

This repository covers the following Python basics:

Variables
Data Types
Numbers
Strings
Operators
📁 Project Structure
python-basics/
│
├── README.md
├── 01_variables.py
├── 02_data_types.py
├── 03_numbers.py
├── 04_strings.py
└── 05_operators.py

🐍 1. Variables

Variables are used to store data in Python.

Example:

name = "John"
age = 20
height = 5.8
is_student = True

🔤 2. Data Types

Python has several built-in data types.

Some commonly used data types are:

Data Type	Example
str	"Hello"
int	10
float	10.5
bool	True / False
list	[1, 2, 3]
tuple	(1, 2, 3)
dict	{"name": "John"}
set	{1, 2, 3}

You can check the data type of a value using type():

age = 20

print(type(age))

🔢 3. Numbers

Python supports different types of numbers, including:

Integers (int)
Floating-point numbers (float)
Complex numbers (complex)

Example:

age = 20
price = 99.99

print(age)
print(price)

Basic Mathematical Operations
a = 10
b = 3

print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division
print(a // b)  # Floor Division
print(a % b)   # Modulus
print(a ** b)  # Exponentiation

🔤 4. Strings

Strings are used to store text.

Example:

name = "John"

print(name)

String Operations
first_name = "John"
last_name = "Doe"

full_name = first_name + " " + last_name

print(full_name)

Useful String Methods
text = "hello world"

print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(len(text))

➕ 5. Operators

Operators are symbols used to perform operations on values.

Arithmetic Operators
Operator	Description
+	Addition
-	Subtraction
*	Multiplication
/	Division
//	Floor Division
%	Modulus
**	Exponent
Comparison Operators
Operator	Description
==	Equal to
!=	Not equal to
>	Greater than
<	Less than
>=	Greater than or equal to
<=	Less than or equal to
Logical Operators
Operator	Description
and	Returns True if both conditions are true
or	Returns True if at least one condition is true
not	Reverses the result

Example:

age = 20

print(age > 18 and age < 30)

Assignment Operators
number = 10

number += 5
number -= 2
number *= 2
number /= 2

🚀 How to Run

Make sure Python is installed on your computer.

Run any Python file using:

python 01_variables.py


Or:

python3 01_variables.py

🎯 Goal

The goal of this repository is to build a strong foundation in Python programming by learning the basic concepts step by step.

📌 Future Topics

More Python topics will be added as I continue learning, such as:

Conditional Statements
Loops
Functions
Lists and Tuples
Dictionaries and Sets
Exception Handling
File Handling
Object-Oriented Programming

⭐ If you find this repository useful, feel free to give it a star!

# Python Numbers

# Integer
a = 10

# Float
b = 5.5

print(a)
print(b)

# Basic calculations
print(a + b)
print(a - b)
print(a * b)
print(a / b)

# Other number types
print(10 // 3)  # Floor division
print(10 % 3)   # Modulus
print(2 ** 3)   # Exponentiation


# Python Strings

name = "John"
message = "Welcome to Python!"

print(name)
print(message)

# String concatenation
first_name = "John"
last_name = "Doe"

full_name = first_name + " " + last_name
print(full_name)

# String repetition
print("Python " * 3)

# String length
print(len(name))

# Accessing characters
word = "Python"

print(word[0])
print(word[1])
print(word[-1])

# String methods
text = "hello world"

print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())


# Python Operators

 An **operator** is used to perform an operation on values or variables.

```
a = 10
b = 5

print(a + b)   # 15
```

 Here, `+` is the operator.

 ## 1\. Arithmetic Operators

 Used for calculations.

```
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333
print(a % b)   # 1
print(a // b)  # 3
print(a ** b)  # 1000
```

 `+  -  *  /  %  //  **`

 ## 2\. Comparison Operators

 Used to compare values. Result is `True` or `False`.

```
age = 20

print(age == 20)   # True
print(age != 18)   # True
print(age > 18)    # True
print(age < 18)    # False
print(age >= 20)   # True
print(age <= 20)   # True
```

 `==  !=  >  <  >=  <=`

 ## 3\. Assignment Operators

 Used to store or update values.

```
x = 10

x += 5
print(x)   # 15

x -= 3
print(x)   # 12
```

 `=  +=  -=  *=  /=  %=  //=  **=`

 ## 4\. Logical Operators

 Used when working with multiple conditions.

```
age = 25

print(age > 18 and age < 60)  # True
print(age < 18 or age > 60)   # False
print(not age > 18)           # False
```

 `and` → both conditions\
 `or` → at least one condition\
 `not` → reverses the result

 ## 5\. Membership Operators

 Used to check whether a value exists in a collection.

```
fruits = ["apple", "banana", "mango"]

print("apple" in fruits)      # True
print("orange" not in fruits) # True
```

 `in` and `not in`

 ## 6\. Identity Operators

 Used to check whether two variables refer to the same object.

```
x = None

print(x is None)      # True
print(x is not None)  # False
```

 `is` and `is not`

 ## 7\. Bitwise Operators

 Used to work with numbers at the binary level.

```
a = 5
b = 3

print(a & b)  # 1
print(a | b)  # 7
print(a ^ b)  # 6
```

 `&` `|` `^` `~` `<<` `>>`

 ### Quick Revision

```
Arithmetic    → Calculate
Comparison    → Compare
Assignment    → Assign / Update
Logical       → Combine conditions
Membership    → Check inside
Identity      → Check same object
Bitwise       → Work with binary
```

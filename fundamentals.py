
 ## 1\. If / Else

```
age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

 ### `if / elif / else`

```
marks = 75

if marks >= 90:
    print("A")
elif marks >= 70:
    print("B")
else:
    print("C")
```

 ## 2\. For Loop

```
for i in range(5):
    print(i)
```

 Output:

```
0
1
2
3
4
```

 ## 3\. While Loop

```
count = 1

while count <= 5:
    print(count)
    count += 1
```

 ## 4\. Break

 Stops the loop completely.

```
for i in range(10):
    if i == 5:
        break

    print(i)
```

 Output:

```
0
1
2
3
4
```

 ## 5\. Continue

 Skips the current iteration.

```
for i in range(5):
    if i == 2:
        continue

    print(i)
```

 Output:

```
0
1
3
4
```

 **Remember:**

 - `break` → stops the loop
- `continue` → skips one iteration

 ## 6\. Array / List

 Python commonly uses a **list** as an array.

```
numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[2])
```

 Output:

```
10
30
```

 ### Add to array

```
numbers.append(60)
print(numbers)
```

 ### Remove from array

```
numbers.remove(30)
print(numbers)
```

 ### Loop through array

```
numbers = [10, 20, 30]

for number in numbers:
    print(number)
```

 ## 7\. 2D Array

 A 2D array is a list of lists.

```
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][0])  # 1
print(matrix[1][2])  # 6
```

 Looks like:

```
1  2  3
4  5  6
7  8  9
```

 ### Loop through 2D array

```
for row in matrix:

    for value in row:
        print(value)
```
# Function

def greet(name):
    return f"Hello, {name}!"

message = greet("John")
print(message)


# Class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."


person = Person("John", 25)
print(person.introduce())


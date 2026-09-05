# List, Tuple, Set & Dictionary

 ## 1\. List

 Stores multiple values and is **mutable (changeable)**.

```
fruits = ["apple", "banana", "mango"]

fruits.append("orange")
fruits[0] = "grapes"

print(fruits)
```

 ### Common Operations

```
fruits.append("orange")   # Add item
fruits.remove("banana")   # Remove item
fruits[0] = "grapes"      # Change item
print(fruits[0])          # Access item
```

---

 ## 2\. Tuple

 Stores multiple values and is **immutable (cannot be changed)**.

```
colors = ("red", "green", "blue")

print(colors[0])
```

 ### Common Operations

```
print(colors[0])       # Access item
print(colors.count("red"))   # Count item
print(colors.index("blue"))  # Find position
```

---

 ## 3\. Set

 Stores **unique values** and does not allow duplicates.

```
numbers = {1, 2, 3, 3}

print(numbers)
# {1, 2, 3}
```

 ### Common Operations

```
numbers.add(4)          # Add item
numbers.remove(2)       # Remove item

print(numbers)
```

 Set operations:

```
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)   # Union
print(a & b)   # Intersection
print(a - b)   # Difference
```

---

 ## 4\. Dictionary

 Stores data as **key-value pairs**.

```
student = {
    "name": "John",
    "age": 20
}

print(student["name"])
```

 ### Common Operations

```
student["city"] = "Delhi"     # Add
student["age"] = 21           # Update
student.pop("city")           # Remove

print(student.keys())         # Keys
print(student.values())       # Values
print(student.items())        # Key-value pairs
```

 ## Quick Difference

```
List   → []          → Mutable → Ordered collection
Tuple  → ()          → Immutable → Ordered collection
Set    → {}          → Unique values
Dict   → {key:value} → Key-value pairs
```

 ### Easy Memory

```
List   → Change
Tuple  → Cannot change
Set    → No duplicates
Dict   → Key : Value
```

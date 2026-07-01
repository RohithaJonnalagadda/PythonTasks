1. List
A list is a collection of items that are ordered and changeable.

Features:
• Written using []
• Allows duplicate values
• Can store different data types

Example:
fruits = ["apple", "banana", "mango"]
print(fruits)

Output:
['apple', 'banana', 'mango']


2. Nested List
A nested list is a list that contains one or more lists inside it.

Features:
• List inside another list
• Used to store data in rows and columns

Example:
student = [
    ["Raju", 20],
    ["Sita", 21],
    ["Ram", 22]
]

print(student)
print(student[0])
print(student[0][1])

Output:
[['Raju', 20], ['Sita', 21], ['Ram', 22]]
['Raju', 20]
20


3. Set
A set is a collection of unique items.

Features:
• Written using {}
• Does not allow duplicate values
• Unordered
• Changeable

Example:
numbers = {10, 20, 30, 20, 40}
print(numbers)

Output:
{10, 20, 30, 40}


4. Dictionary
A dictionary stores data in key-value pairs.

Features:
• Written using {}
• Keys are unique
• Values can be duplicated
• Changeable

Example:
student = {
    "Name": "Rohitha",
    "Age": 22,
    "Course": "Python"
}

print(student)
print(student["Name"])

Output:
{'Name': 'Rohitha', 'Age': 22, 'Course': 'Python'}
Rohitha


5. Tuple
A tuple is a collection of ordered items that cannot be changed (immutable).

Features:
• Written using ()
• Allows duplicate values
• Faster than lists
• Cannot add or remove items

Example:
colors = ("Red", "Green", "Blue")
print(colors)
print(colors[1])

Output:
('Red', 'Green', 'Blue')
Green
